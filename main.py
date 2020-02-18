from flask import Flask, escape, request

from util import generate_short_url
from repo import Repository


repository = Repository()

SHORT_URL_LENGTH = 7

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello, World!")


@app.route('/create')
def create_url():
    url = request.args.get("url")
    short_url = generate_short_url(SHORT_URL_LENGTH)
    repository.add_url(url, short_url)
    return short_url




