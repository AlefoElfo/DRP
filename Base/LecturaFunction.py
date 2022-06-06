import json
import spacy
# DEF


def read_file(file):




# [1] JSON EN PYTHON
    # [0] Instalar pandas
        # (No sirve porque pandas pide el mismo número de filas en archivos json. Lo dejo por si luego se resuelve)
    # [0] Importar pandas
    # [1] Importar archivo json
    # [1] Meterlo a python como diccionario 
        # (Con utf-8, por los acentos y todo)
    # [1] Pasarlos por pandas (No sirve)
# [1] Preparar texto
    # [1] Quitar los nombres y sólo dejar los valores (nombre:valor)
    # [1] Convertir a string


    with open(file, encoding='utf-8') as statenFile:
        staten = json.load(statenFile)
        print('''--------------
    Archivo JSON ingresado como DICT''')
        print('Con', len(staten), 'atributos:')
        print('--------------')
    for key,value in staten.items():
        print(key)
        statenValue = str(value)




# [1] LIMPIAR STRING
    # [1] Eliminar residuos de json
    # [1] Hacer minúsculas todas las palabras
# [0] Investigar si limpiar antes de NLP es más eficiente que con NLP de spacy


    residuosJSON = '''[]{}""':,'''
    replace = ''
    for value in statenValue:
        if value in residuosJSON:
            statenValue = statenValue.replace(value, '')
    statenLower = statenValue.lower()
    print('''--------------
    Archivo DICT se ha limpiado
    --------------''')




# [1] SPACY
    # [1] Instalar spaCy
        # [1] En anaconda prompt (base)
        # [1] Instalar modelo de español profundo
            # (pip install -U spacy[cuda110]) sin las comillas para GPU
            # Instalar CUDA para la GPU
        # [1] Ver que el intérprete sea el mismo (python 3.9.7 base:conda)
    # [1] Importar spacy
    # [0] Pasarlos por spacy.nlp
        # [0] Eliminar palabras repetidas
        # [0] Saltar stop words (me,te,el,las,los)
        # [0] Crear lista con lemmas


    nlp = spacy.load('es_dep_news_trf')
    statenNLP = (set(nlp(statenLower)))
    statenLista = []
    for token in statenNLP:
        if not token.is_stop:
            if not token.is_punct: #¿Qué es más eficiente para el procesador?
                statenLista.append(token.lemma_)
    print('''--------------
    Archivo DICT analizado por PLN
    ''')
    print(type(statenLista))
    print('--------------')
    print(statenLista[:5])
    print('...')

    return statenLista

def preguntame():
    nlp = spacy.load('es_dep_news_trf')
    pregunta = (input('Escribe lo que recuerdes: '))
    preguntaLower = nlp(pregunta.lower())
    preguntaLista = []
    for token in preguntaLower:
        if not token.is_stop:
            if not token.is_punct:
                preguntaLista.append(token.lemma_)


# -----------------------------


