"""Module contains all the logic to manipulate an image and convert it to a MEME."""
from datetime import datetime

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """The meme engine."""

    def __init__(self, tmp_dir):
        """Initializing the meme engine."""
        self.tmp_folder = tmp_dir

    @staticmethod
    def resize_image(image_path, width):
        """Load image
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

    def add_text(self, image, author, quote):
        meme_font = ImageFont.truetype('_data/Chango-Regular.ttf', 20)
        meme_text = f"{quote} - {author}"
        image_editable = ImageDraw.Draw(image)
        image_editable.text((15, 15), meme_text, (237, 230, 211), font=meme_font)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """

        @param img_path:
        @param text:
        @param author:
        @param width:
        """
        # resize
        image = self.resize_image(img_path, width)

        # create meme
        self.add_text(image, author, text)
        image.save(f"{self.tmp_folder}/nombre-{datetime.now()}.jpg")
        print(image)
