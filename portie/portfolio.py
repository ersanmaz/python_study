import csv

from holding import Holding


class Portfolio:
    def __init__(self):
        self.holdings = []

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)  # Skip header
            for row in rows:
                self.holdings.append(Holding(row[0], row[1], row[2], row[3]))
        return self

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, n):
        if isinstance(n, str):
            return [h for h in self.holdings if h.name == n]
        else:
            return self.holdings[n]

    def __iter__(self):
        return self.holdings.__iter__()

    def total_cost(self):
        return sum([h.shares * h.price for h in self.holdings])

    def current_value(self):
        ...
