# Hangman

Very simple game
For the moment only 20 words are in the database

## Prerequisites

### MongoDB

1. Open `config.py` and change the `db` line to `mongo`
2. Install MongoDB from https://www.mongodb.com/try/download/community
3. Open Terminal
4. Install pymongo using command `pip install pymongo`
5. Run `py ./data/generate_words.py` to create a database and insert words into the database

### JSON

1. Open `config.py` and change the `db` line to `json`

### Web version 
1. Install flask using command `pip install flask`

## How to play

### Terminal version

1. Open terminal
2. Run with `py ./main.py`

### Web version

1. Open terminal
2. Run with `py ./web.py`
