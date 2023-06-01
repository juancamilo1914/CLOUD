from codecs import latin_1_decode


n1 = float(input("Introduce tu primer número: ") )
n2 = float(input("Introduce tu segundo número: ") )

suma = (n1 + n2)
resta = ( n1 - n2)
producto = (n1 * n2)
division = (n1 / n2)
exponenciacion = (n1 ** n2)
modulodeladivision = (n1 % n2)

print("XXXXXXXXXXXXXXXXX")

print("el resultado de la suma es:" + str(suma))
print("el resultado de la resta es:" + str(resta))
print("el resultado de el producto es:" + str(producto))
print("el resultado de la division es:" + str(division))
print("el resultado de la exponenciacion es:" + str(exponenciacion))
print("el resultado de el modulo de divison  es:" + str(modulodeladivision))
