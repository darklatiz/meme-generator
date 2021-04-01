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

![Meme generated sample](https://github.com/darklatiz/meme-generator/blob/main/meme/tmp/meme-maker-2021-04-01%2000:12:59.839551.jpg)

## Installation
1. Clone this project or fork it
2. Install [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
```shell
python3 -m pip install --upgrade pip
```

```shell
python3 -m pip install --upgrade Pillow
```
3. Install [Python DOCX](https://python-docx.readthedocs.io/en/latest/user/install.html#install)
```shell
pip install python-docx
```
4. Install [xpdfreader](https://www.xpdfreader.com/download.html)
5. Install [Flask](https://pypi.org/project/Flask/)
```shell
pip install -U Flask
```

# Meme Creator web application
1. Start web server
```shell
python3 app.py
```
2. Access the application using the next url http://127.0.0.1:5000/ you will see a meme being generated and display
in your browser. The meme is generated randomly, the meme engine will select an image, a quote, and the author randomly
tou can pres F5 and every time a new meme will be generated.
  
3. We can generate a custom meme by accessing the next url http://127.0.0.1:5000/create a html page will ask you:
   - A valid URL like [this image](https://cdn.pixabay.com/photo/2020/05/12/17/04/wind-turbine-5163993_960_720.jpg)
   - The quote's body
   - The quote's author
   - when you click "create" a meme with the input provided will be displayed.
   
# CLI application
1. To see command's help
```shell
python -m meme -h 
 
usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]

Meme generator CLI Cool Tool

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      Image path to load, if not provided a random image will be chose
  --body BODY      Quote's Body, If not provided a random quote will be chose.
  --author AUTHOR  Quote's Author, If not provided a random quote will be chose.
```   
2. Execute the next command to execute a command line program and generate your meme, the program will give you the path of meme generated.
```shell
python -m meme --body="A good quote..." --author="El Luigi"
./tmp/meme-maker-2021-04-01 01:06:59.613848.jpg
```

# Overview

The application has the next modules

1. QEngine, this module has all the ingestors, an ingestor will extract quotes from PDF, text files, Docx files and CSV files.
Every ingestor will implement the parse method.
   
2. MemeEngine will use 
   - all the ingestors to create the quotes
   - Pillow library to load, add the text to the image and save the image to the disk
   
3. app.py is the web application and will use QEngine and MemeEngine to provide the web server to create the memes.
4. meme.py is the cli application and will use QEngine and MemeEngine to provide the web server to create the memes, we use
argsparse module to create the optional arguments of the command.


## Tests

- To execute tests
```shell
python -m unittest --verbose meme.tests.QuoteEngineTests  
```

## To check code Style - PEP8
```shell
pydocstyle meme/QuoteEngine/QEngine.py  
```
