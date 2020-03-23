from flask import Flask, request, redirect
from datetime import datetime
from threading import Thread

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
    return short_url


@app.route("/get")
def get_original_url():
    short_url = request.args.get("id")
    url = repository.get_url(short_url)
    dt = datetime.now()
    ip = request.remote_addr

    Thread(target=repository.increment_visit, args=(short_url, )).start()
    Thread(target=repository.insert_ip_address_and_its_visit, args=(ip, short_url, dt))

    return redirect(url)


