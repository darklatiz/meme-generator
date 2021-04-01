"""Meme Maker Module."""
import os
import random
import argparse

from QuoteEngine.MemeEngine import MemeEngine
from QuoteEngine.QEngine import Ingestor
from QuoteEngine.QEngine import QuoteModel

INGESTOR = Ingestor()


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(INGESTOR.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(author, body)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.quote, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    arg_parser = argparse.ArgumentParser(description='Meme generator CLI Cool Tool')
    arg_parser.add_argument('--path', type=str, help='Image path to load, if not provided a random image will be chose', default=None)
    arg_parser.add_argument('--body', type=str, help='Quote\'s Body, If not provided a random quote will be chose.', default=None)
    arg_parser.add_argument('--author', type=str, help='Quote\'s Author, If not provided a random quote will be chose.', default=None)
    args = arg_parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
