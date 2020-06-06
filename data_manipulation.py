import urllib.request

import data_structure


def get_highest_prices(stock_names):
    prices = []
    for stock_name in stock_names:
        data = urllib.request.urlopen(url.format(stock_name)).read().decode()
        price_data = data.split()
        prices.append(price_data[1].split(',')[2])
    return prices


portfolio = data_structure.read_portfolio('Data/portfolio.csv')

cost = [holding['shares'] * holding['price'] for holding in portfolio]
print('Costs: ', cost)

names = [holding['name'] for holding in portfolio]  # List
print('Names: ', names)

unique_names = {holding['name'] for holding in portfolio}  # Set
print('Unique Names: ', unique_names)

more100 = [holding for holding in portfolio if holding['shares'] > 100]
print('Shares more than 100: ', more100)
namesMore100 = [holding['name'] for holding in portfolio if holding['shares'] > 100]
print('Name of Shares more than 100: ', namesMore100)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey=HQMH8SGNJ98IL7D9&datatype=csv'
highest_prices = get_highest_prices(unique_names)

#for name, price in zip(unique_names, highest_prices):
#    print(name, '=', price)

prices = dict(zip(unique_names, highest_prices))
print('Prices: ', prices)

total = sum(cost)
print(total)
