import tkinter as tk
from tkinter import messagebox
from flask import Flask, request, jsonify, render_template
import convertir_py_a_exe
import audio_texto
import texto_a_audio
import Audio_Texto_Audio
import txt_a_audio
import gpt
import Análisis_de_Sentimientos_Analyzer
import Chunking_regex
import Chunking_etiquetas_pos

# Definición de la aplicación Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    original_text = data.get('text')
    reversed_text = original_text[::-1]
    return jsonify({'reversed_text': reversed_text})

def run_flask_app():
    # Ejecuta el servidor Flask
    app.run(debug=True)

def ejecutar_programa(opcion, root):
    if opcion == "1":
        convertir_py_a_exe.convertir_py_a_exe()
    elif opcion == "2":
        audio_texto.grabar_audio_a_texto()
    elif opcion == "3":
        texto_a_audio.texto_a_audio()
    elif opcion == "4":
        Audio_Texto_Audio.convertidor_audio_texto_audio()
    elif opcion == "5":
        txt_a_audio.texto_archivo_a_audio()
    elif opcion == "6":
        gpt.chat_gpt()
    elif opcion == "7":
        Análisis_de_Sentimientos_Analyzer.analisis_sentimientos()
    elif opcion == "8":
        Chunking_regex.chunking_regex()
    elif opcion == "9":
        Chunking_etiquetas_pos.chunking_pos()
    elif opcion == "10":
        root.destroy()
        run_flask_app()  # Ejecuta la aplicación web Flask
    else:
        messagebox.showwarning("Advertencia", "Opción no válida. Por favor, seleccione una opción del 1 al 10.")

def crear_menu():
    root = tk.Tk()
    root.title("Menú de Programas")

    opciones = [
        "Convertir un archivo .py a ejecutable",
        "Grabar un audio y convertirlo a texto",
        "Convertir un texto a audio y reproducirlo",
        "Convertidor de Audio-Texto-Audio",
        "Convertir el texto de un archivo .txt o de Word a audio y reproducirlo",
        "Programa que realiza la función de chat GPT",
        "Análisis de Sentimientos con SentimentIntensityAnalyzer",
        "Chunking: Regex",
        "Chunking: Etiquetas POS",
        "Salir y ejecutar aplicación web, Análisis sobre PLN en una página web"
    ]

    tk.Label(root, text="Menú de Programas", font=("Helvetica", 16, "bold")).pack(pady=10)

    for idx, opcion in enumerate(opciones, start=1):
        btn = tk.Button(root, text=opcion, width=50, command=lambda idx=idx: ejecutar_programa(str(idx), root))
        btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    crear_menu()
