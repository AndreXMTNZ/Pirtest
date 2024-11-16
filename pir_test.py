from gpiozero import MotionSensor
from time import sleep

# Configuración del sensor PIR
pir = MotionSensor(17)  # GPIO 17

try:
    print("Esperando detección de movimiento...")
    while True:
        pir.wait_for_motion()
        print("¡Movimiento detectado!")
        sleep(1)  # Espera para evitar múltiples detecciones rápidas
        pir.wait_for_no_motion()
        print("No hay movimiento detectado.")
except KeyboardInterrupt:
    print("Programa terminado.")
finally:
    print("Limpiando recursos...")
