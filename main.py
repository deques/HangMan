from pathlib import Path
import json, random
import hangy

words_data = Path("data") / "random_words.json"

# Read the file
with open(words_data, "r") as file:
    words = json.load(file)

play = "y"
while (play.lower() == "y"):
  word = random.choice(words)
  hangy.hangman(word.lower())
  play = input("Play again? Y/N ").lower()