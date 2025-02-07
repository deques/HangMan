import hangy, random_word

play = "y"
while (play.lower() == "y"):
  # From json
  # word = random.choice(words)

  # From MongoDB
  word = random_word.get_random_word()  
  hangy.hangman(word)
  play = input("Play again? Y/N ").lower()


