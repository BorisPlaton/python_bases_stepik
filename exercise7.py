class ExtendedStack(list):

    def sum(self):
        if self.is_two():
            self.append(self.pop() + self.pop())

    def sub(self):
        if self.is_two():
            self.append(self.pop() - self.pop())

    def mul(self):
        if self.is_two():
            self.append(self.pop() * self.pop())

    def div(self):
        if self.is_two():
            self.append(self.pop() // self.pop())

    def append(self, element):
        super().append(element)

    def pop(self, *args, **kwargs):
        return super().pop()

    def is_two(self):
        return len(self) >= 2


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0


test()
