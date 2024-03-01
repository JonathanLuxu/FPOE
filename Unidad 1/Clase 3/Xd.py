# Importando las respectivas librerías

import tkinter as tk
from tkinter import Frame, Tk
from tkinter.messagebox import askyesno
from tkcalendar import DateEntry



# Título de la ventana
principal = Tk()
principal.title('Sistema de registro')


# Tamaño de la ventana
principal.resizable(width = True, height = True)
principal.geometry("650x450")


# Función mostrar las coordenadas en donde se dió click
def mostrar_coordenadas(event):
    x = event.x
    y = event.y
    print("Se hizo clic en las coordenadas X={}, Y={}".format(x, y))


# Función mostrar la respectiva tecla que se presionó
def evento_presionar_tecla(evento):
	print("Se presionó la tecla ", repr(evento.char))


# Función cuadro preguntando "Quiere salir de la aplicación? al cerrar la ventana"
def el_usuario_quiere_salir():
	if askyesno('Salir de la aplicación', '¿Seguro que quieres salir?'):
		principal.destroy()


# Función para verificar nombre
def verificar_nombre():
    nombre_ingresado = cuadro_texto.get()
    if nombre_ingresado.isdigit():
        print("Error: Se ha ingresado un número en lugar de un nombre.")
    else:
        print("Nombre ingresado:", nombre_ingresado)


def obtener_fecha():
    fecha_seleccionada = calendario.get_date()
    print("Fecha seleccionada:", fecha_seleccionada)


def verificar_arroba():
    texto_ingresado = cuadro_texto.get()
    if '@' in texto_ingresado:
        print("Se ha detectado un arroba en el texto ingresado.")
    else:
        print("No se ha detectado un arroba en el texto ingresado.")




# Llamado de la función para mostrar las coordenadas
principal.bind("<Button-1>", mostrar_coordenadas)

# Llamado de la función para mostrar las teclas 
principal.bind("<Key>", evento_presionar_tecla)



#Creando un marco para agrupar Nombre
marco = tk.Frame(principal)
marco.pack(padx = 5, pady = 5, anchor = "w")


# Crear una etiqueta para mostrar el texto de Nombre
etiqueta_nombre = tk.Label(marco, text = "Nombre:")
etiqueta_nombre.pack(side = "left")


# Crear un cuadro de texto para Nombre
cuadro_texto = tk.Entry(marco)
cuadro_texto.pack(side = "left", padx = 90)



#Creando un marco para agrupar Apellido
marco = tk.Frame(principal)
marco.pack(padx = 5, pady = 5, anchor = "w")


# Crear una etiqueta para mostrar el texto de Apellido
etiqueta_nombre = tk.Label(marco, text="Apellido:")
etiqueta_nombre.pack(side="left")


# Crear un cuadro de texto para Apellido
cuadro_apellido = tk.Entry(marco)
cuadro_apellido.pack(side = "left", padx = 90)



#Creando un marco para agrupar Correo
marco = tk.Frame(principal)
marco.pack(padx = 5, pady = 5, anchor = "w")


# Crear una etiqueta para mostrar el texto de Correo
etiqueta_correo = tk.Label(marco, text = "Correo:")
etiqueta_correo.pack(side = "left")


# Crear un cuadro de texto para Correo
cuadro_texto_correo = tk.Entry(marco)
cuadro_texto_correo.pack(side = "left", padx = 97)



#Creando un marco para agrupar Edad
marco = tk.Frame(principal)
marco.pack(padx = 5, pady = 5, anchor = "w")


# Crear una etiqueta para mostrar el texto de Edad
etiqueta_edad = tk.Label(marco, text = "Edad:")
etiqueta_edad.pack(side = "left")


# Crear un cuadro de texto para Edad
cuadro_texto_edad = tk.Entry(marco)
cuadro_texto_edad.pack(side = "left", padx = 107)



#Creando un marco para agrupar Fecha de nacimiento
marco = tk.Frame(principal)
marco.pack(padx = 5, pady = 5, anchor = "w")


# Crear una etiqueta para mostrar el texto de Fecha de nacimiento
etiqueta_fecha = tk.Label(marco, text = "Fecha de nacimiento: ")
etiqueta_fecha.pack(side = "left")


# Crear un cuadro de texto para Fecha de nacimiento
calendario = DateEntry(principal, width = 15, background = 'darkblue', foreground = 'white', borderwidth = 2)
calendario.pack(padx = 5, pady = 1)



"""anchor="nw" se utiliza para anclar los widgets en la esquina superior izquierda de la ventana
padx y pady se utilizan para agregar un relleno horizontal y vertical, respectivamente"""


#Loop llamando el cuadro para salir de la ventana
principal.protocol('WM_DELETE_WINDOW', el_usuario_quiere_salir)

#Loop para crear la ventana
principal.mainloop()