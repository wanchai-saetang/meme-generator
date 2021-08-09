# Meme Generator

A multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Overview

Applications to generate memes, which consists of 2 types of application: 1. Web application - User can random generate meme or provide image and quote by themselves. 2. CLI tools - A Command line interface tools to generate meme base on image path and quote (default random)

## Getting Started

### Installing

clone the project to your local machine with `git clone`

### Dependencies

Using virtual environment.
`python -m venv <your_venv_name>`
`<your_venv_name>/Scripts/activate` (Windows)

Install dependencies using PIP with requirments.txt
`pip install -r requirements.txt`

### Running

set FLASK_APP=app.py
flask run --host 0.0.0.0 --port 3000 --reload

### Structure

#### MemeEngine

This module for generate memes base on image, and quotes.
It will resize image and draw text on the image.

#### QuoteEngine

IngestorInterface - Interface for provide necessary method and abstract method.
CSVIngestor - Class for parse CSV file.
DocxIngestor - Class for parse Docx file.
PDFIngestor - Class for parse PDF file.
TXTIngestor - Class for parse TXT file.
QuoteModel - Class for represent data model for store quote.
Ingestor - Encapsualte all ingestor class.

#### app.py

main endpoint for running flask

#### meme.py

CLI tools for generate meme
