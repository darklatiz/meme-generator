"""Main App server for Meme Creator Web application."""
import random
import os
import requests
import pathlib
import logging
from flask import Flask, render_template, request

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.QEngine import Ingestor

INGESTOR = Ingestor()
app = Flask(__name__)
meme = MemeEngine('static')

ROOT_DIRECTORY = (pathlib.Path(__file__).parent).resolve()

MESSAGE_404 = 'We had technical problems while' \
              ' rendering your meme, it could be a 404!!, ' \
              'you put a link to a page with text. Please try again... :)'
MESSAGE_CONNECTION_ERROR = 'A Connection error happened,' \
              ' it is possible that the image url does not exist at all...'

logging.basicConfig(level=logging.INFO)


def setup():
    """Load all resources."""
    quote_files = [ROOT_DIRECTORY / '_data/DogQuotes/DogQuotesTXT.txt',
                   ROOT_DIRECTORY / '_data/DogQuotes/DogQuotesDOCX.docx',
                   ROOT_DIRECTORY / '_data/DogQuotes/DogQuotesPDF.pdf',
                   ROOT_DIRECTORY / '_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(INGESTOR.parse(str(f)))

    quote = random.choice(quotes)

    images_path = "_data/photos/dog/"

    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.quote, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form parameters.
    # 3. Remove the temporary saved image.

    img_url = request.form['image_url']
    quote = request.form['body']
    author = request.form['author']
    random_img = False
    if img_url is not None and len(img_url) > 0:
        try:
            r = requests.get(img_url)
            content_type = r.headers.get('content-type', '')
            logging.info(f"Content type: {content_type}")
            if r.ok and "image" in content_type:
                path = "tmp/download.jpg"
                with open(path, "wb") as f:
                    f.write(r.content)
            else:
                return render_template('404.html',
                                       message=MESSAGE_404)
        except Exception as e:
            logging.error(f'A connection error has '
                          f'happened due to {e} resource {img_url}')
            logging.info(f'Choosing a random image...')
            return render_template('404.html',
                                   message=MESSAGE_CONNECTION_ERROR)
    else:
        logging.info(f'Choosing a random image...')
        random_img, path = get_random_img()

    if (quote is None or len(quote) <= 0) or \
            (author is None or len(author) <= 0):
        logging.info(f'Choosing a random QUOTE...')
        q = random.choice(quotes)
        quote = q.quote
        author = q.author

    res = meme.make_meme(path, quote, author)

    if not random_img:
        if os.path.exists(path):
            os.remove(path)

    return render_template('meme.html', path=res)


def get_random_img():
    return True, random.choice(imgs)


if __name__ == "__main__":
    app.run()
