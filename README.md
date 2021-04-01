# Meme Generator

The meme generator is a fun python 3 application, with this application we can generate a meme using:
- Command line
- [Flask Application](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

The generated meme is made of:
1. A random dog image
2. A quote, the quote has
    - Author
    - Body
    - Example: To be or not to be by Homer
3. Meme generated sample

![Meme generated sample](meme/tmp/meme-maker-2021-04-01 00:12:59.839551.jpg)

## Installation
1. Clone this project or fork it

## [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)

- Installation
```shell
python3 -m pip install --upgrade pip
```

```shell
python3 -m pip install --upgrade Pillow
```

## [Python DOCX](https://python-docx.readthedocs.io/en/latest/user/install.html#install)

```shell
pip install python-docx
```

## Tests

- To execute tests
```shell
python -m unittest --verbose meme.tests.QuoteEngineTests  
```

## To check code Style - PEP8
```shell
pydocstyle meme/QuoteEngine/QEngine.py  
```
