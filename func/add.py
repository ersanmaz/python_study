def add(x, y):
    def do_add():
        print('Adding {} + {} -> {}'.format(x, y, x + y))
        return x + y

    return do_add


a = add(3, 5)

a()
