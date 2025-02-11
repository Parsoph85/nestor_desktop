import base64
import os
import random
import string


def generate_key():
    secret_key = os.urandom(32)
    return base64.b64encode(secret_key).decode('utf-8')


def generate_random_alphanumeric():
    alphanumeric_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanumeric_chars) for _ in range(15))
