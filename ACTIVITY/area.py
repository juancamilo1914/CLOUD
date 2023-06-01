#area del rectangulo

base = int(input("ingrese base:"))
altura = int(input("ingrese altura"))
area1 = (base * altura)
print("el area es: " + str(area1))

#area del triangulo

base = int(input("ingrese la base: "))
altura = int(input("ingrese la altura: "))
area2 = (base * altura)/2 
print("el area del triangulo es: " + str(area2))


print("----------------------------------------")

if area1 > area2:
    print("rectangulo es mayor que triangulo")
else:
    if area1 < area2:
        print("rectangulo es menor que triangulo")
    else:
        print("rectangulo es igual que triangulo")