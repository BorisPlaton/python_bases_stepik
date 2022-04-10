def memo(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if tuple(args) in cache:
            return cache[tuple(args)]
        cache[tuple(args)] = func(*args, **kwargs)
        return cache[tuple(args)]
    return wrapper


@memo
def func_combination(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    c = func_combination(n - 1, k) + func_combination(n - 1, k - 1)
    return c


n, k = map(int, input().split())
print(func_combination(n, k))
