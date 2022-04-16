import string
import random

PASSWORD_MIN_LENGTH = 14
PASSWORD_MAX_LENGTH = 20
ALL_SYMBOLS = string.ascii_letters + string.digits + string.punctuation


def generate_password():
    password = [random.choice(string.ascii_lowercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.digits),
                random.choice(string.punctuation)]
    for symbol in range(random.randint(PASSWORD_MIN_LENGTH - len(password), PASSWORD_MAX_LENGTH)):
        password.append(random.choice(ALL_SYMBOLS))
    random.shuffle(password)
    return password


if __name__ == '__main__':
    password = generate_password()
    print(''.join(password))

