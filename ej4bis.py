def calcular_tiempo_total(tiempos_tramos):
  
  tiempo_suma_minutos = 0

  for tiempo_tramo in tiempos_tramos:
    if not isinstance(tiempo_tramo, int) or tiempo_tramo < 0:
      raise ValueError("El tiempo de un tramo tieneque ser un número entero.")

    tiempo_suma_minutos += tiempo_tramo

  horas, minutos = divmod(tiempo_suma_minutos, 60)
  tiempo_total_str = f"{horas}:{minutos:02d}"
  return tiempo_total_str


suma_tramos = []
while True:
  tiempo_tramo = int(input("Ingrese el tiempo del tramo en minutos (0 para terminar): "))
  if tiempo_tramo == 0:
    break
  suma_tramos.append(tiempo_tramo)

tiempo_total_str = calcular_tiempo_total(suma_tramos)

print(f"El tiempo total de viaje es: {tiempo_total_str}")

  

  

  





      



