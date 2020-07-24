from flask import Flask, request, render_template, session, jsonify
from uuid import uuid4

from boggle import BoggleWordList, BoggleBoard

SESS_BOARD_UUID_KEY = "board_uuid"

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

word_list = BoggleWordList()


# The boggle boards created, keyed by board uuid
boards = {}


@app.route("/")
def homepage():
    """Show board."""

    # get a unique identifier for the board we're creating
    uuid = uuid4()

    board = BoggleBoard()
    boards[uuid] = board

    # store the uuid for the board in the session so that later requests can
    # find it
    session[SESS_BOARD_UUID_KEY] = uuid

    return render_template(
        "index.html",
        board=board)

@app.route("/api/score-word", methods=["POST"])
def score_word():
    """not sure do later"""
    word = request.get_json() #not sure what format this is in, test when implemented
    print(word) #DEBUG


    is_word = word_list.check_word(word['word'])

    # session[SESS_BOARD_UUID_KEY] = uuid4()#Debugging; confirmed
    # print (session[SESS_BOARD_UUID_KEY])

    test_board = boards[session[SESS_BOARD_UUID_KEY]]

    is_in_board = test_board.check_word_on_board(word) #Debugging; unconfirmed

    if not is_word:
        return jsonify({result: "not-word"})
    elif not is_in_board:
        return jsonify({result: "not-on-board"})
    elif is_word:
        return jsonify({result: "ok", word: "[the word]"})
