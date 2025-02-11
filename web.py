from flask import Flask, render_template, request, session
import random_word

app = Flask(__name__)
app.secret_key = "hangyman_wai"

def new_word():
  global game_data

  guess_word = random_word.get_random_word()

  # Hide word
  hide_word = ""
  for i in (range(0, len(guess_word))):
    hide_word += "_"

  # Session
  session['word'] = guess_word
  session['num_incorrect_guesses'] = 0
  session['guesses'] = []
  session['hide_word'] = hide_word
  
  # Game data
  game_data.append(guess_word)
  game_data.append(0)
  game_data.append([])
  game_data.append(hide_word)

  return guess_word

def get_game_data():
  global game_data
  game_data = []
  game_data.append(session['word'])
  game_data.append(session['num_incorrect_guesses'])
  game_data.append(session['guesses'])
  game_data.append(session['hide_word'])

def letter_guess(letter):
  global game_data

  word = game_data[0]
  num_incorrect_guesses = int(game_data[1])
  guesses = game_data[2]
  hide_word = game_data[3]

  if letter in word and letter not in guesses:
    position = -1
    while True:
      position = word.find(letter, position + 1)
      if position == -1:
        break
      hide_word = hide_word[:position] + letter + hide_word[position + 1:]
  elif letter not in guesses:
    guesses.append(letter)
    num_incorrect_guesses +=1

  game_data[1] = num_incorrect_guesses
  game_data[2] = guesses
  game_data[3] = hide_word

  session['num_incorrect_guesses'] = num_incorrect_guesses
  session['guesses'] = guesses
  session['hide_word'] = hide_word

@app.route("/", methods=["POST", "GET"])
def home():
  global game_data
  game_data = []
  if request.method == "POST":
    # Get new word
    if "new_word" in request.form:
      new_word()
    elif "guess" in request.form:
      get_game_data()
      letter = request.form["letter"].lower()
      letter_guess(letter)

  elif request.method == "GET":
    if not session.get('word'):
      new_word()
    else:
      get_game_data()

  return render_template("index.html", data=game_data)
  

if __name__ == "__main__":
  app.run(debug=True)