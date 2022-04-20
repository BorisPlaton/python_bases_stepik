import itertools


def primes():
    num = 2
    while True:
        f = True
        for i in range(2, num):
            if num % i == 0:
                f = False
                break
        if f:
            yield num
        num += 1


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
