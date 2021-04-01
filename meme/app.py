"""Main App server for Meme Creator Web application."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine.MemeEngine import MemeEngine
from QuoteEngine.QEngine import Ingestor

INGESTOR = Ingestor()

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(INGESTOR.parse(f))

    quote = random.choice(quotes)

    images_path = "./_data/photos/dog/"

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
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    img_url = request.form['image_url']
    quote = request.form['body']
    author = request.form['author']

    r = requests.get(img_url)
    path = "./tmp/download.jpg"
    with open(path, "wb") as f:
        f.write(r.content)

    res = meme.make_meme(path, quote, author)

    if os.path.exists(path):
        os.remove(path)

    return render_template('meme.html', path=res)


if __name__ == "__main__":
    app.run()
