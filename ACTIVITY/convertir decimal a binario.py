#Elaborar un programa  que  convierta  un  numero decimal ingresado  por teclado a numero  binario

x = int(input("ingrese el numero:"))

modulos = [] # la lista para guardar los módulos

while x != 0: # mientras el número de entrada sea diferente de cero
    # paso 1: dividimos entre 2
    modulo = x % 2
    cociente = x // 2
    modulos.append(modulo) # guardamos el módulo calculado
    x = cociente # el cociente pasa a ser el número de entrada

rev = list(reversed(modulos))
print(rev)

