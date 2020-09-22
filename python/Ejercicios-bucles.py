'''
#Ejemplo 1: Impresión de palabra 10 veces.
Pal= input('¿Palabra?\n')
for x in range(10):
    print(Pal, x+1)    

#Ejemplo 2: Imprimir número separado por comas
num = int(input('Número positivo '))
for x in range(num, -1, -1): #RECUERDA: start, stop, step size
    print(x, end=', ')

#Ejemplo 3: Triángulo
h = int(input('Ingresa la altura\n'))
for x in range(0, h+1, 1):
    print(x*'*')

#Ejemplo 4: Ingreso de contraseña hasta que funcione
contra = input('Ingresa la contraseña:\n')
c = input('Ingrésala de nuevo:\n')
if c == contra:
    print('k')
else:
    while c != contra:
        c = input('Ingresa de nuevo, hay error.\n')
    print('Hey, éxito.')

#Ejemplo 5: Imprimir palabra letra por letra
pal = input('Ingresa una palabra\n')
for x in pal:
    print(x)
'''
#Ejemplo 6: Contar letras repetidas en una oración
orac = input('Ingresa la oración.\n') #Esto hace que se imprima letra por letra
L = input('¿Cuál letra buscas? ') #Se realiza la comparaicón
c = 0
for i in orac:
    print(i)
    if L == i:
        c+=1
print(f'En la oración se repite {c} veces la letra {L}.')