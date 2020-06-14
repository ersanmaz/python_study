class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise TypeError('Expected float')
        if new_price < 0:
            raise ValueError('Must >=0')
        self._price = new_price

    def __repr__(self):
        return 'Holding({!r}, {!r}, {!r}, {!r})'.format(self.name, self.date, self.shares, self.price)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares
