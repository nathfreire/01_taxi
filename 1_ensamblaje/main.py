import saludar
import entrar_con_password
import mostrar_menu

saludar.saludar()
entrar_con_password.entrar_con_password()
mostrar_menu.mostrar_menu()



import streamlit as st

    
def main():

    st.title("My App")
    st.write(saludar.saludar())  # Pasa el resultado de saludar.saludar() a st.write()
    st.write(entrar_con_password.entrar_con_password())  # Pasa el resultado de entrar_con_password.entrar_con_password() a st.write()
    st.write(mostrar_menu.mostrar_menu())  # Pasa el resultado de mostrar_menu.mostrar_menu() a st.write()

if __name__ == "__main__":
    main()