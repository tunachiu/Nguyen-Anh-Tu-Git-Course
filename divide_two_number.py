def divide(a, b):
    if b == 0:
        raise ValueError('Divide by zero')
    else:
        return a/b

divide(2, 0)