from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from datetime import datetime
from threading import Thread

from biturl.util import generate_short_url
from biturl.repo import Repository


repository = Repository()

SHORT_URL_LENGTH = 7

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/create')
def create_url():
    url = request.args.get("url")
    id = generate_short_url(SHORT_URL_LENGTH)
    repository.add_url(url, id)

    return jsonify(id=id)


@app.route('/<id>')
def get_url_new(id):
    url = repository.get_url(id)
    dt = datetime.now()
    ip = request.remote_addr

    Thread(target=repository.increment_visit, args=(id,)).start()
    Thread(target=repository.insert_ip_address_and_its_visit, args=(ip, id, dt))

    return redirect(url)


@app.route("/get")
def get_original_url():
    short_url = request.args.get("id")
    url = repository.get_url(short_url)
    dt = datetime.now()
    ip = request.remote_addr

    Thread(target=repository.increment_visit, args=(short_url, )).start()
    Thread(target=repository.insert_ip_address_and_its_visit, args=(ip, short_url, dt))

    return redirect(url)


