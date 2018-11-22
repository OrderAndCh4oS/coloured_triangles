import time


def current_micro_time():
    return time.time()


def current_milli_time():
    return int(round(time.time() * 1000))
