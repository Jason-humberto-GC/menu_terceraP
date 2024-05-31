import tkinter as tk
from tkinter import messagebox
import convertir_py_a_exe
import audio_texto
import texto_a_audio
import Audio_Texto_Audio
import txt_a_audio
import gpt
import Análisis_de_Sentimientos_Analyzer
import Chunking_regex
import Chunking_etiquetas_pos

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
        messagebox.showinfo("Información", "Funcionalidad aún no implementada.")
    elif opcion == "11":
        root.destroy()
    else:
        messagebox.showwarning("Advertencia", "Opción no válida. Por favor, seleccione una opción del 1 al 11.")

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
        "Análisis sobre PLN en una página web",
        "Salir"
    ]

    tk.Label(root, text="Menú de Programas Tercera parcial", font=("Helvetica", 16, "bold")).pack(pady=10)

    for idx, opcion in enumerate(opciones, start=1):
        btn = tk.Button(root, text=opcion, width=50, command=lambda idx=idx: ejecutar_programa(str(idx), root))
        btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    crear_menu()
