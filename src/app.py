"""Endpoint for flask application to serve web application."""

import random
import os
import requests
from flask import Flask, render_template, abort, request


from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for q in quote_files:
        quotes.extend(Ingestor.parse(q))

    images_path = "./_data/photos/dog/"
    imgs = []
    dirs = os.listdir(images_path)
    for image_file in dirs:
        imgs.append(os.path.join(images_path, image_file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    print(image_url)
    r = requests.get(image_url)
    tmp_path = f'./tmp/{random.randint(0, 1000000000)}.jpg'
    with open(tmp_path, "wb") as f:
        f.write(r.content)

    path = meme.make_meme(tmp_path, body, author)

    os.remove(tmp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
