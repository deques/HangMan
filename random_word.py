import pymongo, random

def get_random_word():
  # MongoDB Connect
  client = pymongo.MongoClient("mongodb://localhost:27017")
  db = client["hangman"]
  words_db = db["words"]

  # Get random category
  categories = words_db.distinct("category")
  random_category = random.choice(categories)

  # Get random word from the category
  words = words_db.find_one({"category" : random_category})
  word = random.choice(words['words'])

  return word.lower()

