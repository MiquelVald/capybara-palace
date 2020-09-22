
#Ejercicio 5: Contar letras en un nombre ingresado
nombre = input('Ingresa tu nombre, m\'nigga: ')
print('Tu nombre m\'nigga tiene ' + str(len(nombre)) + ' letras.')
#Ejercicio 6: Simple operación aritmética.
sup = 3+2
inf = 2*5
print('El resultado de la operación es: ' + str((sup/inf)**2))
#Ejercicio 7: Calcular pago por horas de trabajo
horas = int(input('¿Cuántas horas trabajaste? '))
costo = int(input('¿Cuánto vale cada hora? '))
pago = horas * costo
print('Pos tu ganarías ' + str(pago) + ' por la chambita.')
#Ejercicio 8: Suma de números anteriores y hasta n'
n = int(input('Ingresa un número bro '))
sum = 0
for a in range(n+1):
    sum+= a 
print('La suma de los números anteriores a [' + str(n) +'] es de: ' + str(sum))
#Ejercicio 9: Calculador de índice de masa corporal
kg = int(input('Ingresa tu peso en kilogramos '))
m = float(input('Ingresa tu estatura '))
imc = kg*m
print(f'Tu imc es de {imc}')
