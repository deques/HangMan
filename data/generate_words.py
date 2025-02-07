from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hangman"]
collection = db["words"]

# Define 20 fruits
fruits = [
    "Apple", "Banana", "Cherry", "Dragonfruit", "Elderberry",
    "Fig", "Grape", "Honeydew", "Jackfruit", "Kiwi",
    "Lemon", "Mango", "Nectarine", "Orange", "Papaya",
    "Quince", "Rambutan", "Starfruit", "Tangerine", "Ugli fruit"
]

# Define 20 berries
berries = [
    "Strawberry", "Raspberry", "Blueberry", "Blackberry", "Gooseberry",
    "Cranberry", "Boysenberry", "Mulberry", "Cloudberry", "Lingonberry",
    "Salmonberry", "Huckleberry", "Loganberry", "Marionberry", "Tayberry",
    "Wineberry", "Youngberry", "Serviceberry", "Chokeberry", "Elderberry"
]

# Create category documents
data = [
    {"category": "fruits", "words": fruits},
    {"category": "berries", "words": berries}
]

# Insert into MongoDB
collection.insert_many(data)

# Confirm insertion
for doc in collection.find():
    print(doc)