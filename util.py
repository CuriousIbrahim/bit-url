import string
import random


def _create_letters():
    temp = string.ascii_letters + string.digits
    chars = []
    for l in temp:
        chars.append(l)
    return chars


characters = _create_letters()


def generate_short_url(length):
    short_url = ""
    for i in range(length):
        short_url += characters[random.randrange(len(characters))]
    return short_url



