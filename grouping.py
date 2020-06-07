import itertools

import data_structure

# With Sorting
portfolio = data_structure.read_portfolio('Data/portfolio.csv')
portfolio.sort(key=lambda item: item['name'])
by_name = {name: list(items) for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name'])}
print('Group IBM: ', by_name['IBM'])

# Without sorting
portfolio = data_structure.read_portfolio('Data/portfolio.csv')
by_name = {name: [p for p in portfolio if p['name'] == name] for name, items in
           itertools.groupby(portfolio, lambda x: x['name'])}
print('Group IBM: ', by_name['IBM'])
