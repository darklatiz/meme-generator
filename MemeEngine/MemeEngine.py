"""Module contains all the logic to manipulate an image."""
from datetime import datetime

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """The meme engine."""

    def __init__(self, tmp_dir):
        """Initialize the meme engine."""
        self.tmp_folder = tmp_dir

    @staticmethod
    def resize_image(image_path, width):
        """Load image.

        @param image_path:
        @param width:
        """
        try:
            with Image.open(image_path) as image_in:
                w, h = image_in.size
                print(f"Image width = {w} and height = {h}")
                resized_im = image_in.resize((width, width))
                return resized_im
        except OSError:
            pass

    @staticmethod
    def add_text(image, author: str, quote: str):
        """Add text to an image, in this case an author and a quote."""
        meme_font = ImageFont.truetype('_data/Chango-Regular.ttf', 20)

        # adjusting text in case of text too long
        if len(quote) > 29:
            logging.info(f'Text is too long for image size,'
                         f' lets cut the text in rows...')
            counter_len = 1
            rows = []
            row = ''
            for part_quote in quote.split(' '):
                row = row + part_quote + " "
                if len(row) > (counter_len * 30):
                    row += '\n'
                    counter_len += 1
            quote = row

        meme_text = f"{quote}\n By {author}"
        image_editable = ImageDraw.Draw(image)
        image_editable.text((5, 15), meme_text, fill=(0, 0, 0), font=meme_font)

    def make_meme(self, img_path, quote, author, width=500) -> str:
        """Make a meme from an image and a quote.

        @param img_path:
        @param quote:
        @param author:
        @param width:
        """
        # resize
        image = self.resize_image(img_path, width)
        # create meme
        self.add_text(image, author, quote)
        file_name = f"{self.tmp_folder}/meme-maker-{datetime.now()}.jpg"
        image.save(file_name)
        return file_name
