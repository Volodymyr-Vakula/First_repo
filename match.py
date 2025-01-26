x = 0
y = 2

match x:
    case 1 | 2 | 0 if y == 2 or y == 3:
        print(x)
    case _:
        print(None)