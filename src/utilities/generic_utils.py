import logging as logger
import random
import string


def generate_random_string(prefix=None, suffix=None, length=10):
    random_string = "".join(random.choices(string.ascii_lowercase, k=length))
    if prefix:
        random_string = str(prefix) + "_" + random_string
    elif suffix:
        random_string += str(suffix)
    return random_string


def generate_random_email(domain=None, prefix=None):
    if not domain: domain = 'gmail.com'
    if not prefix: prefix = "testuser"

    email_length = 10
    random_string = "".join(random.choices(string.ascii_lowercase, k=email_length))
    random_email = prefix + '_' + random_string + '@' + domain
    logger.debug(f"generating random email: {random_email}")
    return random_email


def generate_random_password(length=16):
    LOWERCASE = string.ascii_lowercase
    UPPERCASE = string.ascii_uppercase
    NUMBERS = string.digits
    PUNCTUATION = string.punctuation

    random_lower = random.choices(LOWERCASE, k=length // 6)
    random_upper = random.choices(UPPERCASE, k=length // 6)
    random_numbers = random.choices(NUMBERS, k=length // 3)
    random_p = random.choices(PUNCTUATION, k=length // 3)
    random_password = random_lower + random_numbers + random_upper + random_p
    return "".join(random_password)


if __name__ == '__main__':
    print(generate_random_password())