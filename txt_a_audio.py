import pyttsx3
import os

def texto_archivo_a_audio():
    def text_to_audio(file_path):
        # Inicializar el motor TTS (Texto a Voz)
        engine = pyttsx3.init()

        # Configuraciones opcionales
        engine.setProperty('rate', 150)  # Velocidad de reproducción (palabras por minuto)

        # Leer el archivo de texto
        with open(file_path, 'r') as file:
            text = file.read()

        # Convertir texto a audio
        engine.save_to_file(text, 'output.mp3')  # Guardar el audio como 'output.mp3'
        engine.runAndWait()  # Esperar hasta que se complete la conversión y reproducción

        # Reproducir el audio generado
        os.system('start output.mp3')  # Abrir el archivo de audio con el reproductor predeterminado

    file_path = input("Introduce la ruta del archivo de texto (.txt): ")
    text_to_audio(file_path)
