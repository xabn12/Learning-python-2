import sys
import time

def escribir_suave(texto, velocidad=0.05):
    for caracter in texto:
        # sys.stdout.write permite escribir sin saltos de línea automáticos
        sys.stdout.write(caracter)
        # flush=True asegura que el texto aparezca en pantalla al instante
        sys.stdout.flush()
        # Pausa entre cada letra
        time.sleep(velocidad)
    print() # Al terminar, hace un salto de línea final

# Ejemplo de uso
escribir_suave("Hola, estoy escribiendo de izquierda a derecha... 🚀")