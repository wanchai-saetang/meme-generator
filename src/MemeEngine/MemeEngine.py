"""Represent meme engine to create meme with quote."""

from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap
import pathlib


class MemeEngine():
    """A MemeEngine class for auto generate meme with quote base on directory that is given."""

    def __init__(self, directory) -> None:
        """Create a MemeEngine object to store directory.
        
        :param directory: A directory for store meme
        """
        self.directory = directory
        pathlib.Path(self.directory).mkdir(exist_ok=True)

    def make_meme(
            self,
            img_path: str,
            body: str,
            author: str,
            width=500) -> str:
        """Make meme base on parameter include img_path, body and author and optional parameter width.

        param img_path: image for generate meme
        param body: sentence for meme        
        param author: set author 
        param width: image resize default 500
        """
        img = Image.open(img_path)

        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        self.path = os.path.join(
            self.directory,
            f"{random.randint(0, 100000000)}.jpg")

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('fonts/MonteCarlo-Regular.ttf', size=35)

        lines = textwrap.wrap(f"{body}\n- {author}", 20)
        y_text = height
        for line in lines:
            w, h = font.getsize(line)
            draw.text(((width - w) / 2 + 30, y_text / 2),
                      line, font=font, fill="yellow")
            draw.text(((width - w) / 2 + 30, y_text / 2 + 30),
                      " ", font=font, fill="yellow")
            y_text += h

        img.save(self.path)

        return self.path
