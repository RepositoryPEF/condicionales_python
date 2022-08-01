# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos


# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))
if (numero_1 > numero_2):
    print("El numero", numero_1, "es mayor")
else:
    print ("El numero", numero_2, "es mayor")
# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

if (numero_1 > 0):
    print("El numero", numero_1, "es positivo")
elif (numero_1 < 0):
    print("El numero", numero_1, "es negativo")
else:
    print("El numero", numero_1, "es cero")

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

if (numero_1 > 0 and numero_1 < 100):
    print("El numero", numero_1, "es mayor a cero y el numero", numero_1,"menor que 100")
    print("Si cumple con la condicion")
else:
    print("no cumple su condicion")

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

if(numero_1 < 10 or numero_2 > -2):
    print('si cumple con la condicion numero 1 menor a 10 o numero 2 mayor a -2')

else:
    print('no se cumple con la condicion numero 1 menor a 10 o numero 2 mayor a -2')