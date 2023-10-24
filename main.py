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
from tkinter import ttk
import webbrowser
import html2text

class InfoWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Información del Programa")

        # Dimensiones de la ventana informativa
        width = 800
        height = 600

        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas x e y para centrar la ventana en la pantalla
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Crear un widget Frame para contener el contenido informativo
        info_frame = ttk.Frame(self.root)
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Agregar información sobre el programa
        info_label = ttk.Label(info_frame, text="Información sobre el programa", font=("Helvetica", 18, "bold"))
        info_label.pack(pady=10)

        # Agregar texto informativo enriquecido (con etiquetas HTML)
        info_text = """
        <html>
        <body>
            <p>Este programa es una aplicación increíble que hace muchas cosas geniales.</p>
            <p>Para obtener más información, visita nuestro sitio web:</p>
            <a href="https://www.ejemplo.com">Sitio Web del Programa</a>
            <p>Este programa utiliza las siguientes licencias:</p>
            <ul>
                <li><a href="https://www.ejemplo.com/licencia_a">Licencia A</a></li>
                <li><a href="https://www.ejemplo.com/licencia_b">Licencia B</a></li>
            </ul>
            <p>Al hacer clic en 'Aceptar', aceptas los términos y condiciones del programa.</p>
        </body>
        </html>
        """

        # Eliminar las etiquetas HTML usando html2text
        clean_text = html2text.html2text(info_text)

        # Configurar el widget Text en modo solo lectura
        info_text_widget = tk.Text(info_frame, wrap=tk.WORD, font=("Helvetica", 12), height=10)
        info_text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        info_text_widget.insert(tk.END, clean_text)
        info_text_widget.config(state=tk.DISABLED)  # Configurar el estado como deshabilitado

        # Configurar estilos para los hipervínculos
        info_text_widget.tag_configure("hyperlink", foreground="blue", underline=True)

        # Función para abrir enlaces
        def open_link(event):
            index = info_text_widget.index(tk.CURRENT)
            line, col = index.split(".")
            char_index = int(col) - 1
            line_start = f"{line}.0"
            line_end = f"{line}.end"
            link_text = info_text_widget.get(line_start, line_end)
            link_start = char_index - link_text.find("http")
            link_end = link_start + link_text[link_start:].find(" ")
            link = link_text[link_start:link_end]
            webbrowser.open(link)

        # Encontrar y resaltar hipervínculos
        search_start = "1.0"
        while True:
            link_start = info_text_widget.search("http", search_start, tk.END)
            if not link_start:
                break
            link_end = info_text_widget.search(" ", link_start, tk.END)
            if not link_end:
                break
            info_text_widget.tag_add("hyperlink", link_start, link_end)
            info_text_widget.tag_bind("hyperlink", "<Button-1>", open_link)
            search_start = link_end

        # Agregar una marca de agua de la empresa en la parte inferior izquierda
        watermark_label = ttk.Label(root, text="Theritex", font=("Helvetica", 10), foreground="gray")
        watermark_label.place(relx=0.05, rely=0.92, anchor="sw")

        # Agregar texto de derechos de autor debajo de la marca de agua
        copyright_label = ttk.Label(root, text="© Todos los derechos reservados por Theritex", font=("Helvetica", 8), foreground="gray")
        copyright_label.place(relx=0.05, rely=0.96, anchor="sw")

        # Agregar un botón para aceptar
        accept_button = ttk.Button(info_frame, text="Aceptar", command=self.accept_info)
        accept_button.pack(pady=20)

    def accept_info(self):
        self.hide_window()
        eula_root = tk.Tk()
        eula_window = EULAWindow(eula_root)
        eula_root.mainloop()

    def hide_window(self):
        self.root.withdraw()

class EULAWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Acuerdo de Licencia de Usuario Final (EULA)")

        # Dimensiones de la ventana EULA
        width = 600
        height = 400

        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas x e y para centrar la ventana en la pantalla
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Crear un widget Frame para contener el texto del EULA
        eula_frame = ttk.Frame(self.root)
        eula_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Leer el texto del EULA desde un archivo (eula.txt)
        with open("eula.txt", "r", encoding="utf-8") as file:
            eula_text = file.read()

        # Agregar el texto del EULA en un widget Text
        eula_text_widget = tk.Text(eula_frame, wrap=tk.WORD, font=("Helvetica", 12), height=10)
        eula_text_widget.insert(tk.END, eula_text)
        eula_text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Agregar un botón para aceptar el EULA
        accept_button = ttk.Button(eula_frame, text="Aceptar", command=self.accept_eula)
        accept_button.pack(pady=20)

    def accept_eula(self):
        self.root.destroy()

if __name__ == "__main__":
    has_accepted_info_and_eula = False  # Cambia esto a True si el usuario ya ha aceptado
    
    if has_accepted_info_and_eula:
        eula_root = tk.Tk()
        eula_window = EULAWindow(eula_root)
        eula_root.mainloop()
    else:
        root = tk.Tk()
        style = ttk.Style(root)
        style.theme_use("clam")
        info_window = InfoWindow(root)
        root.mainloop()
