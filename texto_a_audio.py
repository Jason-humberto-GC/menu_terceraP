def texto_a_audio():
        
    from gtts import gTTS

    # Pedir al usuario que ingrese el texto
    texto = input("Ingrese el texto que desea convertir a audio: ")

    # Crear un objeto de gTTS con el texto ingresado y especificar la voz masculina
    tts = gTTS(text=texto, lang='es')


    # Guardar el archivo de audio
    tts.save("output.mp3")

    # Reproducir el archivo de audio
    import pygame
    pygame.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    
    pass