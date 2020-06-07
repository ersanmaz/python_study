import csv


def portfolio_cost(filename, errors='warn'):
    """
    Computes total shares * price for a CSV file with name, date, shares, price data
    :param errors: display error
    :param filename: A csv file
    :return: Total cost
    """

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")
    total_cost = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)    # Skip header
        for row_no, row in enumerate(rows, start=1):
            print(row)
            try:
                shares = int(row[2])
                price = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', row_no, 'Bad row:', row)
                    print('Row:', row_no, 'Reason:', err)
                elif errors == 'raise':
                    raise       # Raises the last exception
                else:
                    pass        # Ignore
                continue        # Skips to the next row
            total_cost += shares * price
    return total_cost


total = portfolio_cost('../data/missing.csv', errors='ignore')
print('Total cost: ', total)
