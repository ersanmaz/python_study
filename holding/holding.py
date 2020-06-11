class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Holding({!r}, {!r}, {!r}, {!r})'.format(self.name, self.date, self.shares, self.price)

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares
