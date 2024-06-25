import streamlit as st

""" def main():
    st.title("Hola, mundo!")
    st.write("Este es un ejemplo sencillo de Streamlit.")
    nombre = st.text_input("Ingresa tu nombre:")
    if nombre:
        st.write(f"Hola, {nombre}!")

if __name__ == "__main__":
    main() """
    
import streamlit as st
from datetime import datetime
import pytz

class Tarifa:
    precio_parada = 0.02
    precio_movimiento = 0.05
    precio_parada_nocturno = precio_parada * 2
    precio_movimiento_nocturno = precio_movimiento * 2

    def calcular_costo(self, tiempo_transcurrido, hora_inicio, es_movimiento):
        if 22 <= hora_inicio.hour or hora_inicio.hour < 6:
            if es_movimiento:
                return tiempo_transcurrido * self.precio_movimiento_nocturno
            else:
                return tiempo_transcurrido * self.precio_parada_nocturno
        else:
            if es_movimiento:
                return tiempo_transcurrido * self.precio_movimiento
            else:
                return tiempo_transcurrido * self.precio_parada


class Recorrido:
    def __init__(self, inicio_tiempo):
        self.inicio_tiempo = inicio_tiempo
        self.tiempo_transcurrido = 0

    def parada(self, tarifa):
        self.tiempo_transcurrido = (datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
        costo = tarifa.calcular_costo(self.tiempo_transcurrido, self.inicio_tiempo, False)
        return costo

    def movimiento(self, tarifa):
        self.tiempo_transcurrido = (datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
        costo = tarifa.calcular_costo(self.tiempo_transcurrido, self.inicio_tiempo, True)
        return costo

    def finalizar(self, tarifa):
        self.tiempo_transcurrido = (datetime.now(pytz.timezone('Europe/Madrid')) - self.inicio_tiempo).total_seconds()
        costo = tarifa.calcular_costo(self.tiempo_transcurrido, self.inicio_tiempo, True)
        return costo


class Carrera:
    def __init__(self, ID, tarifa):
        self.ID = ID
        self.tarifa = tarifa
        self.recorrido = Recorrido(datetime.now(pytz.timezone('Europe/Madrid')))
        self.precio_total = 0
        self.estado = 0

    def parada(self):
        costo = self.recorrido.parada(self.tarifa)
        self.precio_total += costo
        return costo

    def movimiento(self):
        costo = self.recorrido.movimiento(self.tarifa)
        self.precio_total += costo
        return costo

    def finalizar(self):
        costo = self.recorrido.finalizar(self.tarifa)
        self.precio_total += costo
        return costo


def main():
    st.title("Taxi Meter")
    st.write("Bienvenido al taxi meter")

    if 'carrera' not in st.session_state:
        st.session_state.carrera = None

    carrera_id = st.text_input("Ingrese el ID de la carrera")
    if carrera_id:
        if st.session_state.carrera is None:
            st.session_state.carrera = Carrera(ID=int(carrera_id), tarifa=Tarifa())
            st.write(f"Carrera {carrera_id} creada")
        else:
            st.write(f"Carrera {carrera_id} ya existe")

        command = st.selectbox("Seleccione una opción", ["Iniciar carrera", "Parar", "Mover", "Finalizar"])

        if command == "Iniciar carrera":
            st.session_state.carrera.recorrido.inicio_tiempo = datetime.now(pytz.timezone('Europe/Madrid'))
            st.write(f"Carrera iniciada a las {st.session_state.carrera.recorrido.inicio_tiempo.strftime('%Y-%m-%d %H:%M:%S')}.")

        elif command == "Parar":
            costo = st.session_state.carrera.parada()
            st.write(f"Costo por parada: {costo:.2f}€")
            st.write(f"Total: {st.session_state.carrera.precio_total:.2f}€")

        elif command == "Mover":
            costo = st.session_state.carrera.movimiento()
            st.write(f"Costo por movimiento: {costo:.2f}€")
            st.write(f"Total: {st.session_state.carrera.precio_total:.2f}€")

        elif command == "Finalizar":
            costo = st.session_state.carrera.finalizar()
            st.write(f"Total a pagar: {st.session_state.carrera.precio_total:.2f}€")
            st.write(f"Carrera finalizada a las {datetime.now(pytz.timezone)}")
            
            

if __name__ == "__main__":
    main()