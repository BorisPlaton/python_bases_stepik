def find_occurrences(string: str, word: str):
    counter, current_index = 0, 0
    while current_index + len(word) <= len(string):
        if string[current_index:].startswith(word):
            counter += 1
        current_index += 1
    print(counter)


find_occurrences(input(), input())

assert find_occurrences('abababa', 'aba') == 3
assert find_occurrences('abababa', 'abc') == 0
assert find_occurrences('abc', 'abc') == 1
assert find_occurrences('aaaaa', 'a') == 5
