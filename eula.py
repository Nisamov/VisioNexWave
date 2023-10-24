import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from PIL import Image, ImageTk  # Necesitas instalar Pillow para usar Image y ImageTk
from precharge import ejecutar_device

class EULAWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Aceptación de EULA")

        # Dimensiones de la ventana EULA
        width = 800  # Ancho de la ventana
        height = 615  # Alto de la ventana

        # Obtener las dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular las coordenadas x e y para centrar la ventana en la pantalla
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.protocol("WM_DELETE_WINDOW", self.close_app)  # Capturar cierre de ventana

        # Cambiar el icono de la ventana del EULA (Asegúrate de tener un archivo .ico válido)
        self.root.iconbitmap("_media/_images/_icon/app_icon.ico")

        # Crear un widget Frame para contener el contenido
        eula_frame = ttk.Frame(self.root)
        eula_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Cargar el texto del EULA desde un archivo usando utf-8
        with open("EULA.txt", "r", encoding="utf-8") as file:
            eula_text = file.read()

        # Crear una etiqueta de título para el EULA
        title_label = ttk.Label(eula_frame, text="Aceptación de EULA", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=10)

        # Crear un widget de texto con scrollbar para mostrar el EULA
        eula_text_widget = tk.Text(eula_frame, wrap=tk.WORD, font=("Helvetica", 12))
        eula_text_widget.insert(tk.END, eula_text)
        eula_text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Agregar un scrollbar al widget de texto
        scrollbar = Scrollbar(eula_frame, command=eula_text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        eula_text_widget.config(yscrollcommand=scrollbar.set)

        # Agregar un botón para continuar justo debajo del texto
        continue_button = ttk.Button(eula_frame, text="Aceptar y Continuar", command=self.continue_app)
        continue_button.pack(pady=20)

    def continue_app(self):
        self.hide_window()  # Oculta la ventana del EULA
        ejecutar_device()  # Ejecuta precharge.py después de ocultar el EULA

    def hide_window(self):
        self.root.withdraw()  # Oculta la ventana del EULA

    def close_app(self):
        self.root.destroy()

# Crear una instancia de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use("clam")  # Puedes cambiar "clam" a otros temas disponibles (aquavit, keramik, etc.)
    app = EULAWindow(root)
    root.mainloop()
