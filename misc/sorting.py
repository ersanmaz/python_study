from misc.port import read_portfolio

portfolio = read_portfolio('data/portfolio.csv')
print('In file order:')
for p in portfolio: print(p)


def holding_name(holding):
    return holding['name']


portfolio.sort(key=holding_name)
print('Sort by name in asc order: ')
for p in portfolio: print(p)

portfolio.sort(key=lambda holding: holding['shares'])
print('Sort by shares in asc order: ')
for p in portfolio: print(p)
