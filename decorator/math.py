from logcall import logformat

logged = logformat('Calling my {func.__name__}')


@logged
# @logformat('Calling my {func.__name__}')
def add(x, y):
    """
    Adds two numbers
    :param x: first number
    :param y: second number
    :return: Total
    """
    return x + y


@logged
def sub(x, y):
    return x - y


@logged
def mul(x, y):
    return x * y
