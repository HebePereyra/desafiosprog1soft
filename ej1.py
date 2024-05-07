# 1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
# número con los dígitos en orden inverso:

numeros=int(input("Ingrese un numero de tres digitos: "))
numerosacadena=str(numeros)
listadenumeros=list(numerosacadena)
invertir_orden=""

for n in listadenumeros:
    invertir_orden=n+invertir_orden
    
print("El numero invertido es: ", invertir_orden)    



     #convertir el numero en elementos separados de la lista para poder revertirlos
   
# numerosacadena=str(numeros)
# listadenumeros=list(numerosacadena)
# invertir_orden=""

# for n in listadenumeros:
#     invertir_orden=n+invertir_orden
    
# print("El numero invertido es: ", invertir_orden)    


  