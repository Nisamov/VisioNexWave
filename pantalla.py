import tkinter as tk
from tkinter import ttk

class VentanaMovible(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Programa test")
        self.geometry("1200x800")
        self.configure(bg="white")

        self.iconbitmap("C:\\Users\\Nisamov\\Desktop\\ProyectoCreacion\\media\\loader\\random.ico")

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (ancho_pantalla - self.winfo_reqwidth()) // 2
        y = (alto_pantalla - self.winfo_reqheight()) // 2

        # Posicionar la ventana en el centro de la pantalla
        self.geometry("+{}+{}".format(x, y))

        self.bind("<ButtonPress-1>", self.iniciar_arrastre)
        self.bind("<B1-Motion>", self.arrastre_ventana)

        # Cambiar color de fondo de la barra superior
        self.barra_superior = tk.Frame(self, height=30, bg="#EEE8E7")
        self.barra_superior.pack(fill=tk.X)

        # Crear etiqueta de opciones en la barra superior con la fuente Cyberfunk
        self.boton_opciones = tk.Label(self.barra_superior, text="Opciones", bg="#EEE8E7", padx=5,
                                       font=("Cyberfunk", 12))  # Fuente Cyberfunk
        self.boton_opciones.pack(side=tk.LEFT)

        self.boton_opciones.bind("<Enter>", self.mostrar_descripcion)
        self.boton_opciones.bind("<Leave>", self.ocultar_descripcion)

    def iniciar_arrastre(self, event):
        self._x = event.x
        self._y = event.y

    def arrastre_ventana(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        nueva_geo = f"{self.winfo_width()}x{self.winfo_height()}+{self.winfo_x() + deltax}+{self.winfo_y() + deltay}"
        self.geometry(nueva_geo)

    def mostrar_descripcion(self, event):
        descripcion = "Esta es la descripción del texto 'Opciones'"
        self.tooltip = tk.Label(self, text=descripcion, background="#f0f0f0", relief="solid", borderwidth=1)
        self.tooltip.place(x=self.boton_opciones.winfo_x() + self.boton_opciones.winfo_width() + 5,
                           y=self.boton_opciones.winfo_y())

    def ocultar_descripcion(self, event):
        self.tooltip.destroy()

ventana = VentanaMovible()
ventana.mainloop()
