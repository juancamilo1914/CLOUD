x = int(input("x : "))
y = int(input("y : "))

if x > y:
    print("x es mayor que y")
else:
    if x < y:
        print("x es menor que y")
    else:
        print("x es igual que y")

if x > y:
    print("x es mayor que y")
elif x < y:
    print("x es menor que y")
else:
    print("x es iual a y")