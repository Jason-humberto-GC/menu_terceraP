def chat_gpt():
        
    import openai

    # Configurar tu clave de API de OpenAI
    openai.api_key = "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"
    # Función para registrar consultas y respuestas
    def registrar(consulta, respuesta):
        with open("log.txt", "a") as archivo:
            archivo.write(f"Consulta: {consulta}\nRespuesta: {respuesta}\n\n")

    # Función para enviar una solicitud de chat a ChatGPT
    def enviar_solicitud_chat(mensaje):
        try:
            respuesta = openai.Completion.create(
                engine='text-gpt-2.5-turbo',
                prompt=mensaje,
                max_tokens=50,
                temperature=0.7
            )
            respuesta_texto = respuesta.choices[0].text.strip()
            registrar(mensaje, respuesta_texto)
            return respuesta_texto
        except Exception as e:
            error = f"Ocurrió un error al enviar la solicitud de chat: {str(e)}"
            registrar(mensaje, error)
            return error

    # Función para interactuar con el usuario
    def interactuar():
        print("¡Bienvenido al ChatGPT!")
        print("Puedes comenzar a escribir tus mensajes. Escribe 'salir' para terminar la conversación.")
        print("-----------------------------------------")

        # Loop de interacción
        while True:
            mensaje = input("Usuario: ")

            if mensaje.lower() == 'salir':
                break

            respuesta = enviar_solicitud_chat(mensaje)
            print("ChatGPT:", respuesta)
            print("-----------------------------------------")

    # Ejecutar la función de interacción
    interactuar()
    
    pass