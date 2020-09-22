'''
#Ejercicio 1: Entras o no entras
x = int(input('Ingresa tu edad: '))
if x >= 18:
    print('Bienvenido :D')
else:
    print('No puedes.')
#Ejercicio 2: Contraseñas iguales o no
password = input('Ingresa la contraseña: ')
contra = 'pitoloco'

if password == contra:
    print('Nice.')
else:
    print('shit, no')
#Ejercicio 3: División de dos números con divisor imposible en 0
n1 = int(input('Primer número: '))
n2 = int(input('Segundo número: '))

if n2 == 0:
    print('Bruh, wtf???')
else:
    print(f'El resultado de la operación es: {n1/n2}')
#Ejercicio 4: Número par o impar.
num = int(input('Ingresa un número :D\n'))
if num % 2 == 0:
    print('Par')
else:
    print('Impar')
#Ejercicio 5: Edad e ingresos mensuales.  
edad = int(input('¿Qué edad tienes?\n'))
ing = int(input('¿Cuáles son tus ingresos mensuales?\n'))
if edad > 16 and ing >= 1000:
    print('Nigga u fucked')
else:
    print('Nigga u ain\'t ready to be fucked...')
    
#Ejercicio 6: Sexo y nombre.
Nom = input('Nombre. ')
Sex = input('Sexo (M/H). ')
if Sex == 'M':
    if Nom < 'M':
        print('Vas al grupo A.')
    else:
        print('Vas al grupo B')
if Sex == 'H':
    if Nom < 'N':
        print('Vas al grupo B')
    else:
        print('Vas al grupo A')
elif Sex != 'H' and Sex != 'M':
    print('Opción incorrecta')

#Ejercicio 6: Pago de impuestos
renta = int(input('Cuánto tienes de renta?\n'))
if renta < 10000:
    print(f'Pagarás un tipo impositivo de 5%, es decir, ${renta*.05}')
elif renta >= 10000 and renta < 20000:
    print(f'Pagarás un tipo impositivo de 15%, es decir, ${renta*.15}')
elif renta >= 20000 and renta < 35000:
    print(f'Pagarás un tipo impositivo de 20%, es decir, ${renta*.20}')
elif renta >= 35000 and renta < 60000:
    print(f'Pagarás un tipo impositivo de 30%, es decir, ${renta*.30}')
else:
    print(f'Pagarás un tipo impositivo de 45%, es decir, ${renta*.45}')

#Ejercicio 9: Pago por edad.
edad = int(input('Ingresa la edad '))
if edad < 4:
    print('Entras gratis!')
elif edad >= 4 and edad <= 18:
    print('Pagas $4.')
else:
    print('Pagas $10')
'''
    


    
