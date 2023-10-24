# Yb    dP 88 .dP"Y8 88  dP"Yb  88b 88 888888 Yb  dP Yb        dP    db    Yb    dP 888888 
#  Yb  dP  88 `Ybo." 88 dP   Yb 88Yb88 88__    YbdP   Yb  db  dP    dPYb    Yb  dP  88__   
#   YbdP   88 o.`Y8b 88 Yb   dP 88 Y88 88""    dPYb    YbdPYbdP    dP__Yb    YbdP   88""   
#    YP    88 8bodP' 88  YbodP  88  Y8 888888 dP  Yb    YP  YP    dP""""Yb    YP    888888 


# Program: VisioNexWave
# Supportes by: FvhirNex

#!C:\python
# -*- coding:utf-8 -*-
# Author: Nisamov
# Personal Use Only

# Code Under MIT License

# Read the README.md to know more info


import tkinter as tk
import subprocess
import time

# Función para ejecutar device.py en segundo plano
def ejecutar_device():
    subprocess.Popen(["python", "device.py"])

# Función para cerrar la ventana después de 5 segundos
def cerrar_ventana():
    ventana_precarga.destroy()

if __name__ == "__main__":
    # Crear la ventana de precarga
    ventana_precarga = tk.Tk()

    # Establecer un título para la ventana de precarga
    ventana_precarga.title("Cargando...")

    # Deshabilitar los botones de cerrar, minimizar y ampliar
    ventana_precarga.overrideredirect(True)

    try:
        # Intentar cargar el GIF animado
        loading_gif = tk.PhotoImage(file="_media/preloader.gif")

        label_cargando = tk.Label(ventana_precarga, image=loading_gif)
        label_cargando.pack(padx=10, pady=10)

        # Centrar la ventana en la pantalla
        ventana_precarga.geometry("+{}+{}".format(
            ventana_precarga.winfo_screenwidth() // 2 - loading_gif.width() // 2,
            ventana_precarga.winfo_screenheight() // 2 - loading_gif.height() // 2
        ))

    except tk.TclError:
        # Si no se encuentra el GIF, muestra el mensaje "Cargando..." con una animación
        mensaje_cargando = tk.Label(ventana_precarga, text="Cargando...")
        mensaje_cargando.pack(padx=10, pady=10)

        # Centrar la ventana en la pantalla
        ventana_precarga.geometry("+{}+{}".format(
            ventana_precarga.winfo_screenwidth() // 2 - 100,  # Ancho de la ventana de mensaje
            ventana_precarga.winfo_screenheight() // 2 - 20  # Altura de la ventana de mensaje
        ))

    # Ejecutar device.py en segundo plano
    ejecutar_device()

    # Programar el cierre de la ventana después de 5 segundos (5000 milisegundos)
    ventana_precarga.after(5000, cerrar_ventana)

    # No es necesario llamar a sys.exit() aquí, ya que la ventana se cerrará automáticamente después de 5 segundos

    ventana_precarga.mainloop()


