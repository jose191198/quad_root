
#Actividad: Básica

#Crea una función en la cual recibas como argumentos los parámetros reales de una función cuadrática, 
#y te regrese los valores de x1 y x2

#En caso de que el resultado sea un valor imaginario, el programa debe imprimir alguna frase informando 
#al usuario que la respuesta cuenta con un valor imaginario.

#Es indispensable hacer la actividad creando funciones dentro de python (para esto se utiliza el 
#comando def), y regresando algún valor utilizando la función return.

def numeros_fun (a, b, c):
    raiz1 = (b**2)-(4*a*c)
    raiz2 = raiz1**0.5
    x1 = ((-b) + raiz2)/(2*a)
    x2 = ((-b) - raiz2)/(2*a)
    return x1, x2, raiz1

x1, x2, raiz = numeros_fun(1, -4, 10)

if raiz < 0:
    print (f'Tu resultado tiene numeros complejos: x1:{x1} y x2:{x2}')
else:
    print (f'Tu resultado es x1:{x1} y x2:{x2}')

