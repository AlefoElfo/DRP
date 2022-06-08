# [1] Hacer input de pregunta natural
# [1] Pedir pregunta al usuario
# [1] Convenrtir a string
# [1] Volver minúsculas
# [1] pasar pregunta por spacy.nlp
# [1] Limpiar puntuación
# [1] Eliminar palabras innecesarias
# [1] Convertir a lemmas

import spacy
nlp = spacy.load('es_dep_news_trf')
pregunta = (input('Escribe lo que recuerdes: '))
preguntaLower = nlp(pregunta.lower())
preguntaLista = []
for token in preguntaLower:
    if not token.is_stop:
        if not token.is_punct:
            preguntaLista.append(token.lemma_)
