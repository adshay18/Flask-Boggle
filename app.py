from boggle import Boggle
from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "boggleme"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

boggle_game = Boggle()

@app.route('/')
def start_game():
    board = boggle_game.make_board()
    session["game_board"] = board
    saved_board = session["game_board"]
    return render_template('index.html', board=saved_board)