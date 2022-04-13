try:
    foo()
except BaseException:
    print("BaseException")
except ArithmeticError as e:
    print(e)
except AssertionError as e:
    print(e)




