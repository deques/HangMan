from pathlib import Path
import json, random

words_data = Path("data") / "random_words.json"

# Read the file
with open(words_data, "r") as file:
    words = json.load(file)

def hangman(word):
  word_length = len(word)

  hide_word = ""
  for i in (range(0, word_length)):
    hide_word += "_"

  print(f"Guess the word: {hide_word}")

  wrong_guesses = 0
  max_wrong_guesses = 5
  guesses = []

  while wrong_guesses < max_wrong_guesses:
    letter = input("Guess a letter: ")
    if len(letter) > 1:
      print("Just one letter please")
      continue
    letter = letter.lower()
    
    if letter in word and letter not in guesses:
      position = -1
      while True:
        position = word.find(letter, position + 1)
        if position == -1:
          break
        hide_word = hide_word[:position] + letter + hide_word[position + 1:]
    
      print(hide_word)
      if "_" not in hide_word:
        print("You won")
        break
    else:
      wrong_guesses += 1
      print(f"You have guess wrong {wrong_guesses} times")

    if letter not in guesses:
      guesses.append(letter)

  if wrong_guesses == max_wrong_guesses:
    print("You lost")

play = "y"
while (play.lower() == "y"):
  word = random.choice(words)
  hangman(word.lower())
  play = input("Play again? Y/N ").lower()
