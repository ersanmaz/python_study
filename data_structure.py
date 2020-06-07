import csv


def read_portfolio(filename, errors='warn'):
    """
    Read a CSV file with name, date, shares, price data into a list.
    :param filename: A csv file
    :return: Total cost
    """

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row_no, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', row_no, 'Bad row:', row)
                    print('Row:', row_no, 'Reason:', err)
                elif errors == 'raise':
                    raise  # Raises the last exception
                else:
                    pass  # Ignore
                continue  # Skips to the next row
            #record = tuple(row)
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)
    return portfolio
