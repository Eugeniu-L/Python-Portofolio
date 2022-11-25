import random


def get_random_words(file):
    with open(file, "r") as data:
        words = [word.split("\n")[0] for word in random.sample(data.readlines(), 100)]
    return words
