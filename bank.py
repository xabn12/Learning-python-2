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

smooth(f"Hola {name} que operacion deseas realizar")

while True:
    print("----Menu de opciones----")
    operacion= int(input("1.- Retiro  2.- Deposito :    "))
    
    match operacion:
        case 1: 
             print("Seleccionaste: Retiro")
             retiro=int(input("Cuanto desea retirar:    "))
             if retiro < 10:
                 print("El monto no puede ser menor de 10")
                 smooth("Desea salir? 1.-Si  2.-No:    ")
                 salir=int(input())
                 if salir == 1:
                     print ("VUELVA PRONTO!")
                     break
             else:
                 print(f"Retiro de {retiro} exitoso")
                 break
        case 2:
             print("Seleccionaste: Depósito")
             deposito=int(input("Cuanto desea depsoitar:    "))
             if deposito < 20:
                 print("el monto no puede ser menor de 20")
                 smooth("Desea salir? 1.-Si  2.-No:    ")
                 salir=int(input())
                 if salir == 1:
                     print ("VUELVA PRONTO!")
                     break
             else:
                 print(f"Deposito de {deposito} exitoso")
                 break
        case _:
             print("Esa operación no existe")
             break
    


