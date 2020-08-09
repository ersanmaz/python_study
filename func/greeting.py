import time


def after(seconds, func):
    time.sleep(seconds)
    func()


def hello():
    print('Hello World')


after(3, hello)
