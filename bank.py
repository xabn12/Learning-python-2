import sys
import time

def smooth(texto, velocidad=0.05):
    for caracter in texto:
        # sys.stdout.write permite escribir sin saltos de línea automáticos
        sys.stdout.write(caracter)
        # flush=True asegura que el texto aparezca en pantalla al instante
        sys.stdout.flush()
        # Pausa entre cada letra
        time.sleep(velocidad)
    print() # Al terminar, hace un salto de línea final
    
name="Fabricio"

smooth("Hola " + name + " que operacion deseas realizar")

while True:
    operacion= int(input("1.- Retiro  2.- Deposito :    "))
    
    match operacion:
        case 1: 
             print("Seleccionaste: Retiro")
             retiro=input("Cuanto desea retirar:   ")
             if retiro < 10:
                 print("El monto no puede ser menor de 10")
             else:
                 print("Retiro exitoso")
             break
        case 2:
             print("Seleccionaste: Depósito")
             break
        case _:
             print("Esa operación no existe")
             break
    


