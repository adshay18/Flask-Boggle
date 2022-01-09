from boggle import Boggle
from flask import Flask, render_template, session, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
import pdb

app = Flask(__name__)
app.config['SECRET_KEY'] = "boggleme"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

boggle_game = Boggle()

@app.route('/')
def start_game():
    '''Method to display index.html and start the game'''
    board = boggle_game.make_board()
    session["game_board"] = board
    saved_board = session["game_board"]
    return render_template('index.html', board=saved_board)

@app.route('/validate-word')
def test_word():
    '''Check if the word is in the dictionary'''
    
    word = request.args["word"]
    game_board = session["game_board"]
    response = boggle_game.check_valid_word(game_board, word)

    return jsonify({'result': response})

@app.route('/score-game', methods=["POST"])
def update_score():
    '''Takes game score, compares it to high score, and updates number of games played.'''
    
    score = request.json["score"]
    plays = session.get("plays", 0)
    high_score = session.get("high_score", 0)
    
    session["score"] = score
    session["plays"] = plays + 1
    if score > high_score:
        high_score = score
        session["high_score"] = high_score
    
    return jsonify({'score': score, 'plays': session["plays"], 'high_score': high_score})