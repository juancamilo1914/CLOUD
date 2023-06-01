''' cree las variables y asigne los siguentes valores y muestre la informacion en consola de los datos ingresados'''

Nombre = str(input("NOMBRE: "))

if Nombre == 'juan camilo' :
    print ('BIENVENIDO MANO')
else:
    print('VOS QUIEN SOS?')

identificacion = int(input("IDENTIFICACION: "))

if  identificacion == 1118363413:
    print('si sos vos')
else:
    print("TE DEVOLVÉS!")
    
edad = int(input("EDAD: "))


if edad >= 18:
    print('si entra')
else:
    print("Adios!")
    
