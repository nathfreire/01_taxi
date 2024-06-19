""" class Taximetro():
    def __init__(self, interruptor,euros_parada):
        self.interruptor=interruptor
        self.__encendido=False
         
    def movimiento(self):
        self.incial=True
        self.contador+=1
        
   
    def reinicia(self):
        self.km_relativo=0
    def display_data(self):
        print(f'Características:\nmarca:{self.interruptor}|km_total:{self.km_total}|km_rel:{self.km_relativo}')
    def encender(self):
        self.__encendido=True
        
    def apago(self):
        self.__encendido=False
    def estado(self):
        if self.__encendido:
            mensaje+='Estado encendido'
        else:
            mensale+='Estado Apagado'
#Un ID propio

class TaxiMeter:
    def __init__(self):
        self.is_running = False
        self.distance = 0
        self.fare = 0

    def start_race(self):
        if not self.is_running:
            self.is_running = True
            print("Carrera iniciada")
        else:
            print("La carrera ya está en curso")

    def stop_at_traffic_light(self):
        if self.is_running:
            self.is_running = False
            print("Carrera detenida en semáforo")
        else:
            print("La carrera no ha iniciado")

    def end_race(self):
        if self.is_running:
            self.is_running = False
            print("Carrera finalizada")
            print(f"Distancia recorrida: {self.distance} km")
            print(f"Tarifa total: ${self.fare:.2f}")
        else:
            print("La carrera no ha iniciado")

    def update_distance(self, km):
        if self.is_running:
            self.distance += km
            self.fare += km * 0.5  # supongamos que la tarifa es de $0.5/km
        else:
            print("La carrera no ha iniciado")

# Creamos un objeto TaxiMeter
taxi = TaxiMeter()

# Iniciamos la carrera
taxi.start_race()

# Actualizamos la distancia recorrida
taxi.update_distance(5)

# Paramos en un semáforo
taxi.stop_at_traffic_light()

# Actualizamos la distancia recorrida nuevamente
taxi.update_distance(3)

# Finalizamos la carrera
taxi.end_race()

 """








#////////////////////////////////////////////////////
import time
class TaxiMeter:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.distance = 0
        self.rate = 0.05

    def start_race(self):
        self.running = True 
        self.start_time = time.time()

    def stop_at_traffic_light(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.distance += elapsed_time * self.rate
            self.running = False

    def end_race(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.distance += elapsed_time * self.rate
        print(f"Total distance: {self.distance} km")
        print(f"Total distance: {self.distance} km")
        self.running = False
        
taxi = TaxiMeter()
taxi.start_race()
# some time later
taxi.stop_at_traffic_light()
# some time later
taxi.end_race()





import time

class TaxiMeter:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.distance = 0
        self.rate = 0.05

    def start_race(self):
        self.running = True 
        self.start_time = time.time()
        print(self.start_time)

    def stop_at_traffic_light(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.distance += elapsed_time * self.rate
            self.running = False

    def end_race(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.distance += elapsed_time * self.rate
        print(f"Total distance: {self.distance:.2f} km")
        self.running = False

taxi = TaxiMeter()
taxi.start_race()
time.sleep(5)  # wait for 5 seconds
taxi.stop_at_traffic_light()
time.sleep(3)  # wait for 3 seconds
taxi.end_race()