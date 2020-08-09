from functools import wraps


def logged(func):
    # Idea: Give me a function, I'll put logging around it

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


def logformat(fmt):
    def logged(func):
        # Idea: Give me a function, I'll put logging around it

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__
        return wrapper

    return logged


def logmethods(cls):
    for key, value in list(vars(cls).items()):
        if callable(value):  # Is it a method? If so, decorate
            setattr(cls, key, logged(value))
    return cls
