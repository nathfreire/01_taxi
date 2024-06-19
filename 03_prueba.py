        
def empieza_movimiento(self):#Cuando el coche está en movimiento.
    self.movimiento = True
    self.inicio_tiempo = time.time() #El módulo me da el tiempo en segundos
    #self.fecha_inicio = datetime.

def parar_movimiento(self): #Cuando el coche está parado
    if self.movimiento: #Llamo al método "movimiento"
        tiempo_acumulado = time.time() - self.inicio_tiempo #el tiempo acumulado en movimiento hasta el momento - tiempo inicial
        self.tarifa_total += 0.05 * tiempo_acumulado #
        self.movimiento = False