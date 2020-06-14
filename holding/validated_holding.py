from holding.validate import String, Integer, Float


class Holding(object):
    name = String('name')
    shares = Integer('shares')
    price = Float('float')

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        if name not in {'name', 'date', 'shares', 'price'}:
            raise AttributeError('No attribute {}', name)
        super().__setattr__(name, value)

    def __repr__(self):
        return 'Holding({!r}, {!r}, {!r}, {!r})'.format(self.name, self.date, self.shares, self.price)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares
