
from flask import Flask, render_template, request, make_response, Response, jsonify
import json
import scrabee

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Enter 7 letters after the /"


@app.route('/fun/<word>')
def fun_time(word):
    wordlist=scrabee.scrabble(word)
    return jsonify(wordlist)
