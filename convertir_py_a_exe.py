#def convertir_py_a_exe():

import os
import subprocess
import sys

def convertir_py_a_exe():
        def convert_to_executable(script_path):
            # Verifica que el archivo existe
            if not os.path.isfile(script_path):
                print(f"El archivo {script_path} no existe.")
                return

            # Instala PyInstaller si no está instalado
            try:
                import PyInstaller
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

            # Ejecuta PyInstaller
            try:
                subprocess.check_call([sys.executable, "-m", "PyInstaller", "--onefile", script_path])
                print(f"El archivo ejecutable ha sido creado en el directorio 'dist'.")
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar PyInstaller: {e}")

        script_path = input("Introduce la ruta del script Python que quieres convertir a ejecutable: ")
        convert_to_executable(script_path)


   # pass