#!/usr/bin/env python

from flask import Flask, render_template
from random import randint

app = Flask(__name__)

WAYS_TO_SAY_NO = [
    'No.',
    'Nope.',
    'No. Thanks.',
    'Not today.',
    'Not this month.',
    'Not ever.',
    'Maybe. But No.',
    'Never.'
]

@app.route('/')
def index():
    index = randint(0, len(WAYS_TO_SAY_NO) - 1)
    no = WAYS_TO_SAY_NO[index]
    return render_template('index.html', nope=no)

if __name__ == '__main__':
    app.run(debug=True)