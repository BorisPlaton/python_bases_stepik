def replace_characters(string: str, old: str, new: str):
    operations_amount = 0
    while operations_amount <= 1000:
        if string.find(old) == -1:
            return print(operations_amount)
        string = string.replace(old, new)
        operations_amount += 1
    return print('Impossible')


replace_characters(input(), input(), input())

assert replace_characters('ababa', 'a', 'b') == 1
assert replace_characters('ababa', 'a', 'b') == 1
assert replace_characters('ababa', 'b', 'a') == 1
assert replace_characters('ababa', 'c', 'c') == 0
assert replace_characters('ababac', 'c', 'c') == 'Impossible'
