"""4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0."""
print("Calculemos tu viaje en horas! ")
tramo1= int(input("Ingrese cantidad de minutos de tramo 1: "))
tramo2= int(input("Ingrese cantidad de minutos de tramo 2: "))
tramo3= int(input("Ingrese cantidad de minutos de tramo 3: "))
tramo4= int(input("Ingrese cantidad de minutos de tramo 4: "))

sumaTramos= tramo1 + tramo2 + tramo3 + tramo4

if sumaTramos<60:
    print(f"Ud recorrio {sumaTramos} minutos en total")

if sumaTramos>=60:
    horas, minutos = divmod(sumaTramos, 60) 
    sumaTramos_str = f"{horas}:{minutos:02d}" 
    print(f"Ud recorrio {sumaTramos_str} hs en total")  

  # El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
  # probar un while ver ej4bis.py
   




