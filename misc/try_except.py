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
        for row_no, row in enumerate(rows, start=1):
            print(row)
            try:
                shares = int(row[2])
                price = float(row[3])
            except ValueError as err:
                print('Row:', row_no, 'Bad row:', row)
                print('Row:', row_no, 'Reason:', err)
                continue  # Skips to the next row
            total_cost += shares * price
    return total_cost


total = portfolio_cost('../data/missing.csv')
print('Total cost: ', total)
