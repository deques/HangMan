def hangman(word):
  word_length = len(word)

  hide_word = ""
  for i in (range(0, word_length)):
    hide_word += "_"

  wrong_guesses = 0
  max_wrong_guesses = 10
  guesses = []

  while wrong_guesses < max_wrong_guesses:
    print(f"Guess the word: {hide_word}")
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
    
      print(f"Correct guess!")
      if "_" not in hide_word:
        print(f"You won\nThe word was {word}")
        break
    elif letter not in guesses:
      wrong_guesses += 1
      print(f"You have guess wrong {wrong_guesses} times")
    else:
      print("You already have guessed this letter. Guess again")

    if letter not in guesses:
      guesses.append(letter)
    
    print(f"Your guesses: {guesses}\n")

  if wrong_guesses == max_wrong_guesses:
    print(f"You lost\n The word was {word}")
