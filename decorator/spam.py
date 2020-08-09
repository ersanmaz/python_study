from logcall import logmethods


@logmethods
class Spam(object):
    def __init__(self, value):
        self.value = value

    def yow(self):
        print('Yow!')

    def grok(self):
        print('Grok!')
