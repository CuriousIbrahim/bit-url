from flask import Flask, request, redirect

from util import generate_short_url
from repo import Repository


repository = Repository()

SHORT_URL_LENGTH = 7

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/create')
def create_url():
    url = request.args.get("url")
    short_url = generate_short_url(SHORT_URL_LENGTH)
    repository.add_url(url, short_url)
    repository.get_url(short_url)
    return short_url


@app.route("/get")
def get_original_url():
    short_url = request.args.get("id")
    url = repository.get_url(short_url)
    return redirect(url)


