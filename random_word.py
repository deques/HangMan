import json, random
from pathlib import Path
import config, mongo

def get_from_json():
  words_data = Path("data") / "random_words.json"

  # Read the file
  with open(words_data, "r") as file:
    words = json.load(file)
  
  word = random.choice(words)
  return word.lower()

def get_random_word():
  if config.db == 'mongo':
    word = mongo.get_from_mongoDB()
  elif config.db == 'json':
    word = get_from_json()
  
  return word