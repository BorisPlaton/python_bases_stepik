class multifilter:

    def __init__(self, iterable, *funcs, judge=None):
        self.funcs = funcs
        self.judge = judge or self.judge_any
        self.iterable = iterable
        self.filter_iterable()

    def filter_iterable(self):
        mas = []
        for elem in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(elem):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                mas.append(elem)
        self.iterable = mas

    @staticmethod
    def judge_half(pos, neg):
        return pos >= neg

    @staticmethod
    def judge_any(pos, neg):
        return pos >= 1

    @staticmethod
    def judge_all(pos, neg):
        return neg == 0

    def __iter__(self):
        return iter(self.iterable)


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
