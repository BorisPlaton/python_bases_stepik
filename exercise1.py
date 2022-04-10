# objects уже существует вне программы (такое условие задания)
print(len({id(i) for i in objects}))
