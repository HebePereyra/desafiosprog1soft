#3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es un número primo o no.

def es_primo(numeroIngresado):
  
    if numeroIngresado <= 1:
        return False

    for i in range(2, numeroIngresado): #itera desde el 2 hasta el numero anterior al ingresado.
        if numeroIngresado % i == 0:   #si el resto es 0 cuando divide el nro ingresado por cualquier numero, no es primo. 
            return False
    
    return True

# Solicitar el número al usuario
numeroIngresado = int(input("Ingrese un número entero: "))

# Evaluar si el número es primo
if es_primo(numeroIngresado):
  print(f"Ud. ingreso: {numeroIngresado} que es un numero primo.")
else:
  print(f"Ud. ingreso:{numeroIngresado} no es un número primo.")
