import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from translate import Translator

def analisis_sentimientos():
    def traducir_texto(texto, de='es', a='en'):
        # Crear un objeto Translator
        translator = Translator(from_lang=de, to_lang=a)
        # Traducir el texto
        traduccion = translator.translate(texto)
        return traduccion

    def analizar_sentimiento_vader(texto):
        # Crear un objeto SentimentIntensityAnalyzer
        sia = SentimentIntensityAnalyzer()
        
        # Analizar el sentimiento
        sentimiento = sia.polarity_scores(texto)
        
        # Obtener las puntuaciones
        compound = sentimiento['compound']
        pos = sentimiento['pos']
        neu = sentimiento['neu']
        neg = sentimiento['neg']
        
        # Determinar el tipo de sentimiento
        if compound > 0.05:
            resultado = 'Positivo'
        elif compound < -0.05:
            resultado = 'Negativo'
        else:
            resultado = 'Neutral'
        
        return resultado, compound, pos, neu, neg

    texto = input("Introduce una frase en español para analizar su sentimiento: ")
    texto_traducido = traducir_texto(texto)
    resultado, compound, pos, neu, neg = analizar_sentimiento_vader(texto_traducido)
    print(f"Texto traducido: {texto_traducido}")
    print(f"Resultado: {resultado}")
    print(f"Compound: {compound}")
    print(f"Positivo: {pos}")
    print(f"Neutral: {neu}")
    print(f"Negativo: {neg}")
