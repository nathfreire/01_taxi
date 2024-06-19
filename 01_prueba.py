
import datetime
import time #tengo que importar este módulo para acceder a sus funciones y que nos permita trabajar con el tiempo.
class viaje:
    def __init__(self): #Aquí inicializo las variables
        self.movimiento = False
        self.inicio_tiempo = 0
        self.tarifa_total = 0
        self.fecha_inicio = 0
        self.contrasenya = 0 # o ''
        self.id=1 #
    def empieza_movimiento(self):#Cuando el coche está en movimiento.
        self.movimiento = True
        self.inicio_tiempo = time.time() #El módulo me da el tiempo en segundos
        #self.fecha_inicio = datetime.

    def parar_movimiento(self): #Cuando el coche está parado
        if self.movimiento: #Llamo al método "movimiento"
            tiempo_acumulado = time.time() - self.inicio_tiempo #el tiempo acumulado en movimiento hasta el momento - tiempo inicial
            self.tarifa_total += 0.05 * tiempo_acumulado #
            self.movimiento = False

    def stop(self): #Cuando el coche se detiene
        if self.movimiento:# si estás en el método "movimiento" entonces
            #Si el conductor ha pulsado por semáforo
            self.parar_movimiento() #llamas a la función "parar movimiento", lo que hace que la variable pase a False
            self.tarifa_total += 0.02 * (time.time() - self.inicio_tiempo)
                #IF pulsa continuar:
                    #self.parar_movimiento() #llamas a la función "parar movimiento", lo que hace que la variable pase a True
                    #Y vuelta otra vez.
                #IF  el conductor ha detenido definitivamente el viaje
                #self.id=1

#Un bucle ??
carrera = viaje()
input("Press Enter to start the taxi meter...")
try:
    while True:
        command = input("Enter 'm' to start moving, 's' to stop moving, or 'q' to quit: ")
        if command == 'm':
            carrera.empieza_movimiento()
        elif command == 's':
            carrera.parar_movimiento()
        elif command == 'q':
            carrera.stop()
            break
except KeyboardInterrupt:
    carrera.stop()

# Print the total fare
print("Tarifa Total: {:.2f} Euros".format(carrera.tarifa_total))