def params(*args, **kwargs):
    return len(args) + len(kwargs)

print(params(7, "a", 0, k = 'b', c = 'd'))