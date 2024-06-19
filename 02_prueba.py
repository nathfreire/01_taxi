
import datetime
import time #tengo que importar este módulo para acceder a sus funciones y que nos permita trabajar con el tiempo.
class carrera:
    precio_parada=0.02
    precio_movimiento=0.05
    precio_parada_nocturno=precio_parada*2
    fecha_inicio=0
    fecha_final=0
    id=0
    tiempo_acumulado_parado=0
    tiemopi_acumulado_movimiento=0
    
    def __init__(self): #Aquí inicializo las variables
        self.movimiento = False
        self.inicio_tiempo = 0
        self.tarifa_total = 0
        self.fecha_inicio = 0
        self.contrasenya = 0 # o ''

    
    def stop(self): #Cuando el coche se detiene
        if self.movimiento:# si estás en el método "movimiento" entonces
            #Si el conductor ha pulsado por semáforo
            self.parar_movimiento() #llamas a la función "parar movimiento", lo que hace que la variable pase a False
            self.tarifa_total += 0.02 * (time.time() - self.inicio_tiempo)
                #IF pulsa continuar:
                    #self.movimiento() #llamas a la función "movimiento", lo que hace que la variable pase a True
                    #Y vuelta otra vez.
                #IF  el conductor ha detenido definitivamente el viaje
                #self.id=1



# Print the total fare
print("Tarifa Total: {:.2f} Euros".format(carrera.tarifa_total))