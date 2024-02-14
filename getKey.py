import random
import string
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_key(length, chars):
    doneKey = []

    for _ in range(1):
        genKey = "".join(random.choice(chars) for _ in range(length))

        doneKey.append(genKey)

    return doneKey


def create_key():
    # Get Chars #
    char = "".join(str(string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation))

    characters = list(char)
    random.shuffle(characters)

    # Get Length #
    keyLength = random.randint(15, 20)

    # Create Key #
    createdKey = generate_key(length=keyLength, chars=characters)

    return createdKey


key = ''.join(create_key())
