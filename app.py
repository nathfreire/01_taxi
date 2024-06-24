import streamlit as st

def main():
    st.title("Hola, mundo!")
    st.write("Este es un ejemplo sencillo de Streamlit.")
    nombre = st.text_input("Ingresa tu nombre:")
    if nombre:
        st.write(f"Hola, {nombre}!")

if __name__ == "__main__":
    main()