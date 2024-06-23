'''
1ra Parte:

Suponer un sistema de reserva de asientos para un anfiteatro. El teatro cuenta con 10 filas y 10 asientos cada una. Se necesita desarrollar un sistema (sin uso de base de datos, unicamente manejo de datos de forma lógica) que permita llevar a cabo lo siguiente:

1. Cargar el 'mapa' de las filas y asientos. Indicando con un 'X' los asientos ocupados y con una 'L' los asientos libres. Al iniciar el programa, todos los asientos deben estar libres.

2. Manejar la reserva de asientos contemplando que un asiento SOLO PUEDE SER RESERVADO si se encuentra en estado 'L' en caso de que esté en estado 'X' se deberá permitir al comprador elegir otro asiento. Si se encuentra en estado 'L' deberá pasar automáticamente al estado 'X'.

3. Para finalizar el programa se deberá ingresar un valor en particular. Comtemplar que no existe una cantidad exacta de veces que el programa se pueda ejecutar.

4. Contemplar que SOLO EXISTEN 10 FILAS y 10 ASIENTOS No se pueden vender asientos fuera de esas numeraciones. No se permite 'sobreventa'.

CONSIDERACIONES: No es necesaria implementación ni de IGU ni de BD. Se evaluará 100% el manejo lógico del desarrollo de la aplicación.

EXTRA: En caso de que un cliente solicite visualizar cuáles son los asientos libres, el sistema debe permitir mostrar de forma gráfica el mapa de asientos. NO UTILIZAR IGU para este caso. Utilizar UNICAMENTE lógica y la salida por consola.

'''  
import numpy as np

def reservaAsient(matrix):
  dibujar = input('Desea visualizar el mapa de asientos antes de reservar? (s/n): ')
  if dibujar == 's':
    print(matrix)
    seleccionar(matrix)
  elif dibujar == 'n':
    seleccionar(matrix)
  return (matrix)

def seleccionar(matrix):
  fila = int(input('Que número de fila desea reservar?'))
  asiento = int(input('Que número de asiento desea reservar?'))
  if matrix[fila -1][asiento -1] == 'L':
    matrix[fila -1][asiento -1] = 'X'
    print('Asiento reservado con éxito')
  else :
    print('Asiento ocupado, elija otro')
    seleccionar(matrix)
  cont = input('Desea continuar con otra reserva? (s/n)')
  if cont == 's':
    reservaAsient(matrix)
  
  return(matrix)
 
def run():
  #quiero crear una matriz de 10x10 llena de L
  matrix = np.empty((10, 10), dtype=str)
  for i in range(10):
    for j in range(10):  
      matrix[i][j] = "L"
  while True:
    reservaAsient(matrix)
    print('Mapa de disponibilidad, L = Libre, X = Asiento reservado')
    print(matrix)
    break

print("*****************Bienvenido al sistema de reserva de asientos*****************")
run()









