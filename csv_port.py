import csv


def portfolio_cost(filename):
    """
    Computes total shares * price for a CSV file with name, date, shares, price data
    :param filename: A csv file
    :return: Total cost
    """

    total_cost = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            print(row)
            shares = int(row[2])
            price = float(row[3])
            total_cost += shares * price
    return total_cost


total = portfolio_cost('Data/portfolio2.csv')
print('Total cost: ', total)
