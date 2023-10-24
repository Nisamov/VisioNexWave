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

import sys
import os
import json
import win32api  # Necesitas instalar pywin32 para esto
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QMenu, QAction, QInputDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class TextFile(QLabel):
    def __init__(self, file_name, base_location, parent=None):
        super().__init__(parent)
        self.setText(file_name)
        self.base_location = base_location  # Almacena la ubicación base
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('background-color: #FFFFFF')
        self.setFixedSize(QSize(100, 100))
        self.mousePressEvent = self.run_file

        # Almacena la ubicación del archivo en una propiedad
        self.file_path = os.path.join(self.base_location, file_name + ".txt")

    def run_file(self, event):
        with open(self.file_path, "r") as file:
            file_contents = file.read()
        # Puedes hacer algo con el contenido del archivo, como mostrarlo en una ventana
        print(f"Contenido de {self.file_path}:\n{file_contents}")

class DesktopApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definir la ubicación base para guardar archivos y carpetas
        self.base_location = "_section_module/files_and_folders"

        self.initUI()
        self.load_desktop_state()  # Cargar el estado del escritorio al inicio

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)  # Define las dimensiones de la ventana principal
        self.setWindowTitle('Mi Escritorio')

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)  # Establece las dimensiones de la etiqueta de fondo
        self.background_label.setPixmap(QPixmap("_media/_images/background.png"))  # Establece la imagen de fondo

        self.current_x = 50  # Coordenada X inicial para la creación de carpetas

        # Una lista de carpetas y archivos de texto creados
        self.folders_and_text_files = []

        # Agregar el menú contextual (clic derecho)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.base_location, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Obtener el ícono de una carpeta de Windows
        folder_icon_path = win32api.GetFileAttributes(folder_path)

        folder_label = QLabel(self)
        folder_label.setText(folder_name)
        folder_label.setAlignment(Qt.AlignCenter)
        folder_label.setGeometry(self.current_x, 200, 100, 100)
        folder_label.setStyleSheet('background-color: #FFFFFF')
        folder_label.setFixedSize(QSize(100, 100))
        folder_label.mousePressEvent = self.run_application  # Asocia la acción de hacer clic en la carpeta a la ejecución de una aplicación
        folder_label.setProperty("path", folder_path)  # Almacena la ubicación de la carpeta en una propiedad

        # Establecer el ícono de la carpeta
        folder_icon = QIcon(folder_icon_path)
        folder_label.setPixmap(folder_icon.pixmap(QSize(64, 64)))  # Tamaño del ícono

        self.current_x += 120  # Incrementa la coordenada X para la próxima carpeta
        self.folders_and_text_files.append(folder_label)
        self.save_desktop_state()  # Guardar el estado del escritorio después de crear una carpeta

    def show_create_folder_dialog(self):
        folder_name, ok = QInputDialog.getText(self, 'Crear Carpeta', 'Nombre de la Carpeta:')
        if ok:
            self.create_folder(folder_name)

    def show_create_file_dialog(self):
        file_name, ok = QInputDialog.getText(self, 'Crear Archivo', 'Nombre del Archivo:')
        if ok:
            text_file = TextFile(file_name, self.base_location, self)
            self.folders_and_text_files.append(text_file)
            self.save_desktop_state()  # Guardar el estado del escritorio después de crear un archivo de texto

    def run_application(self, event):
        folder_label = self.sender()
        app_name, ok = QInputDialog.getText(self, 'Ejecutar Aplicación', 'Nombre de la Aplicación:')
        if ok:
            # Simula la ejecución de la aplicación
            folder_label.setText(f"Ejecutando: {app_name}")
            folder_label.setStyleSheet('background-color: #FFFF00')
            folder_label.setWordWrap(True)
            folder_label.setAlignment(Qt.AlignTop)
            self.save_desktop_state()  # Guardar el estado del escritorio después de ejecutar una aplicación

    def save_desktop_state(self):
        # Guardar el estado de las carpetas y archivos de texto en un archivo JSON
        state = {"items": [label.text() for label in self.folders_and_text_files]}
        with open("_section_module/desktop_state.json", "w") as file:
            json.dump(state, file)

    def load_desktop_state(self):
        # Cargar el estado de las carpetas y archivos de texto desde un archivo JSON
        if os.path.exists("_section_module/desktop_state.json"):
            with open("_section_module/desktop_state.json", "r") as file:
                state = json.load(file)
                for item_name in state.get("items", []):
                    if item_name.endswith(".txt"):
                        # Crear un archivo de texto si el nombre termina con ".txt"
                        text_file = TextFile(item_name[:-4], self.base_location, self)
                        self.folders_and_text_files.append(text_file)
                    else:
                        # Crear una carpeta en caso contrario
                        self.create_folder(item_name)

    def show_context_menu(self, event):
        context_menu = QMenu(self)

        create_folder_action = QAction("Crear Carpeta", self)
        create_folder_action.triggered.connect(self.show_create_folder_dialog)

        create_file_action = QAction("Crear Archivo de Texto", self)
        create_file_action.triggered.connect(self.show_create_file_dialog)

        settings_action = QAction("Ajustes de Pantalla", self)
        settings_action.triggered.connect(self.show_settings_dialog)

        context_menu.addAction(create_folder_action)
        context_menu.addAction(create_file_action)
        context_menu.addAction(settings_action)

        context_menu.exec_(self.mapToGlobal(event))

    def show_settings_dialog(self):
        # Puedes agregar la lógica para mostrar la ventana de ajustes aquí
        pass

def main():
    app = QApplication(sys.argv)
    ex = DesktopApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
