x = 0
y = 3

match x:
    case 1 | 2 | 0 if y == 2 | y == 3:
        print(x)
    case _:
        print(None)