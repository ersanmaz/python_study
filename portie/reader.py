import csv


def read_csv(filename, types, *, errors='warn'):
    """
    Read a CSV file with type conversion into a list of dicts
    """

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn', 'silent', 'raise'")

    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row_no, row in enumerate(rows, start=1):
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', row_no, 'Bad row:', row)
                    print('Row:', row_no, 'Reason:', err)
                elif errors == 'raise':
                    raise  # Raises the last exception
                else:
                    pass  # Ignore
                continue  # Skips to the next row
            # record = tuple(row)
            record = dict(zip(headers, row))
            records.append(record)
    return records
