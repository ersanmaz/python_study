import csv

import data_structure
import urllib.request

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

for unique_name in unique_names:
    data = urllib.request.urlopen(url.format(unique_name)).read()
    print('Data: ', data)
    price_data = data.split()
    print('Price Data: ', price_data)
    first_row = price_data[2]
    print('First Row: ', price_data)
    # for row in price_data:
    #     r = row.split()
    #     print('Split Row: ', r)
    #

    #high = price_data[1][2]
    #print('High Value: ', high)
    #rows = csv.reader(io.StringIO(data))
    #headers = next(rows)  # Skip header
    #for row in rows:
    #    print(row)

total = sum(cost)
print(total)
