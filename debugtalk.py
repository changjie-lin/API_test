import time
import random
import string

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_random_str():
    LEN_LIMIT=20
    return ''.join(random.sample(string.ascii_letters, random.randint(1, LEN_LIMIT)))


def get_random_positive():
    LIMIT = 1000
    return random.randint(0, LIMIT)


def get_random_negative():
    LIMIT = -1000
    return random.randint(LIMIT, 0)


def get_long_str(chars = string.ascii_uppercase + string.digits, N=200):
	return ''.join(random.choice(chars) for _ in range(N))