from misc import reader


def read_portfolio(filename, *, errors='warn'):
    """
    Read a CSV file with name, date, shares, price data into a list.
    :param errors: errors while parsing csv
    :param filename: A csv file
    :return: Total cost
    """
    return reader.read_csv(filename, [str, str, int, float], errors=errors)
