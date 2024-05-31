def chunking_pos():
        
    import nltk
    from nltk.chunk import RegexpParser
    from nltk.tokenize import word_tokenize
    from nltk import pos_tag, ne_chunk

    # Descargar los recursos necesarios de NLTK
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')

    # Solicitar al usuario que ingrese el texto a analizar
    text = input("Ingrese el texto a analizar: ")

    # Tokenizar el texto en palabras
    words = word_tokenize(text)

    # Etiquetar las palabras con sus POS tags
    tagged = pos_tag(words)

    # Definir la gramática para identificar frases nominales (NP), verbales (VP), etc.
    grammar = r"""
        NP: {<DT>?<JJ.*>*<NN.*>}
        P: {<IN>}
        V: {<V.*>}
        PP: {<P> <NP>}
        VP: {<V> <NP|PP>*}
    """

    # Crear el analizador de gramática
    parser = RegexpParser(grammar)

    # Aplicar el analizador al texto etiquetado
    result = parser.parse(tagged)

    # Imprimir el resultado del chunking
    print("Chunking Result:")
    print(result)

    # Función para mostrar los chunks de una forma más legible
    def print_chunks(tree):
        for subtree in tree:
            if isinstance(subtree, nltk.Tree):
                print(f"{subtree.label()}: {' '.join([word for word, tag in subtree.leaves()])}")

    print("Readable Chunks:")
    print_chunks(result)

    # Identificar entidades nombradas (NER)
    ner_chunks = ne_chunk(tagged)

    # Imprimir el resultado de NER
    print("Named Entity Recognition Result:")
    print(ner_chunks)

    # Visualizar el árbol de chunking (opcional)
    result.draw()
    
    pass