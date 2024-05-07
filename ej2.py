#Escriba un programa que pregunte al usuario 
#la hora actual t del reloj y un número
#entero de horas h, que indique qué hora 
#marcará el reloj dentro de h horas:

hora_actual=int(input("Ingrese la hora actual entre las 00hs y las 23hs: "))
horas_a_sumar=int(input("Ingrese un numero de horas a sumar: "))

suma_horas= hora_actual+horas_a_sumar 
if suma_horas>=0 and suma_horas<=23:
    reloj_marca= suma_horas
    print("el reloj marca: ",reloj_marca)
if suma_horas>23:
    reloj_marca=suma_horas%24
    print("el reloj marca: ", reloj_marca) 

  #armar para los minutos ver import data time
       






