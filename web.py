from flask import Flask, render_template, request, session
import random_word

app = Flask(__name__)
app.secret_key = "hangyman_wai"

def new_word():
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
  session['won'] = False
  session['lost'] = False

  return guess_word

def get_game_data():
  global game_data
  game_data = []
  game_data.append(session['word'])
  game_data.append(session['num_incorrect_guesses'])
  game_data.append(session['guesses'])
  game_data.append(session['hide_word'])
  game_data.append(session['won'])
  game_data.append(session['lost'])

def letter_guess(letter):
  word = session['word']
  num_incorrect_guesses = int(session['num_incorrect_guesses'])
  guesses = session['guesses']
  hide_word = session['hide_word']
  if letter == "":
    return
  if letter in word and letter not in guesses:
    position = -1
    while True:
      position = word.find(letter, position + 1)
      if position == -1:
        break
      hide_word = hide_word[:position] + letter + hide_word[position + 1:]

      if "_" not in hide_word:
        session['won'] = True
  elif letter not in guesses:
    guesses.append(letter)
    num_incorrect_guesses +=1

  if num_incorrect_guesses == 10:
    session['lost'] = True

  session['num_incorrect_guesses'] = num_incorrect_guesses
  session['guesses'] = guesses
  session['hide_word'] = hide_word

@app.route("/", methods=["POST", "GET"])
def home():
  global game_data
  if request.method == "POST":
    # Get new word
    if "new_word" in request.form:
      new_word()
    elif "guess" in request.form:
      letter = request.form["letter"].lower()
      letter_guess(letter)

  elif request.method == "GET":
    if not session.get('word'):
      new_word()

  
  get_game_data()
  return render_template("index.html", data=game_data)
  

if __name__ == "__main__":
  app.run(debug=True)