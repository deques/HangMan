import pymongo, json, random
from pathlib import Path
import config

def get_from_mongoDB():
  # MongoDB Connect
  client = pymongo.MongoClient(config.db_string)
  db = client["hangman"]
  words_db = db["words"]

  # Get random category
  categories = words_db.distinct("category")
  random_category = random.choice(categories)

  # Get random word from the category
  words = words_db.find_one({"category" : random_category})
  word = random.choice(words['words'])

  return word.lower()


def get_from_json():
  words_data = Path("data") / "random_words.json"

  # Read the file
  with open(words_data, "r") as file:
    words = json.load(file)
  
  word = random.choice(words)
  return word.lower()

def get_random_word():
  if config.db == 'mongo':
    word = get_from_mongoDB()
  elif config.db == 'json':
    word = get_from_json()
  
  return word