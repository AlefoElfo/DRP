# [1] CREAR TESAURO EN JSON
    # [1]Relaciones semánticas del lexema
    # [1]Definición
    # [1]Meterlos en formato json
# [0] (2a versión) Digitalizar 5 términos
    # [0]Hacer tesauro manual
    # [0]Agregar definición
    # [0]Meterlos en formato json





# [1] JSON EN PYTHON
    # [0] Instalar pandas
        # (No sirve porque pandas pide el mismo número de filas en archivos json. Lo dejo por si luego se resuelve)
    # [0] Importar pandas
    # [1] Importar json
    # [1] Meterlo a python como diccionario 
        # (Con utf-8, por los acentos y todo)
    # [1] Pasarlos por pandas (No sirve)
# [1] Preparar texto
    # [1] Quitar los nombres y sólo dejar los valores
    # [1] Convertir a atring


import json

from sympy import intersection
with open('Statenvertaling.json', 'r', encoding='utf-8') as statenFile:
    staten = json.load(statenFile)
    print('''--------------
Archivo JSON ingresado como DICT''')
    print('Con', len(staten), 'atributos:')
    print('--------------')
for key,value in staten.items():
    print(key)
    statenValue = (str(value))
#PENDIENTES
# 1. ¿Cómo especificar si el atributo tiene una lista, tupla o diccionario?




# [1] LIMPIAR STRING
    # [1] Eliminar residuos de json
    # [1] Hacer minúsculas todas las palabras
# [0] Investigar si limpiar antes de NLP es más eficiente que con NLP de spacy

residuosJSON = '''[]{}""':,'''
replace = ''
for str in statenValue:
    if str in residuosJSON:
        statenValue = statenValue.replace(str, '')
statenLower = statenValue.lower()
print('''--------------
Archivo DICT se ha limpiado
--------------''')






# [1] Importar spacy
    # [1] Instalar spaCy
        # [1] En anaconda prompt (base)
        # [1] Instalar modelo de español profundo
            # (pip install -U spacy[cuda110]) sin las comillas para GPU
            # Instalar CUDA para la GPU
        # [1] Ver que el intérprete sea el mismo (python 3.9.7 base:conda)
    # [1] Importar spacy
        # [1] Añadir 
    # [0] Pasarlos por spacy.nlp
        # [0] Eliminar palabras repetidas
        # [0] Saltar stop words (me,te,el,las,los)
        # [0] Convertir a lemmas

import spacy
nlp = spacy.load('es_dep_news_trf')
statenNLP = (set(nlp(statenLower)))
statenLista = []
for token in statenNLP:
    if not token.is_stop:
        if not token.is_punct:
            statenLista.append(token.lemma_)
print('''--------------
Archivo DICT analizado por PLN
''')
print(type(statenLista))
print('--------------')
print(statenLista)




# -----------------------------

# [1] Hacer input de pregunta natural
    # [1] Pedir pregunta al usuario
    # [1] Convenrtir a string
    # [1] Volver minúsculas
    # [1] pasar pregunta por spacy.nlp
    # [1] Limpiar puntuación
    # [1] Eliminar palabras innecesarias
    # [1] Convertir a lemmas

pregunta = (input('Escribe lo que recuerdes: '))
preguntaLower = nlp(pregunta.lower())
preguntaLista = []
for token in preguntaLower:
    if not token.is_stop:
        if not token.is_punct:
            preguntaLista.append(token.lemma_)
print(preguntaLista)



# [0] Comparar las listas
    # [0] 
    # [0] 
    # [0] 
    # [0] 

coincidencias = []
for eS in statenLista:
    for eP in preguntaLista:
        if set(eS) == set(eP):
            coincidencias.append(eS)
print(len(coincidencias))


# [0] Crear función para leer los json
# [0] For lectura in jsonFIle:
# [0] buscar en nombre, hiperónimos, cohipónimos, hipónimos, polisemia, antonimia, meronimia, definición
# [0] Contar coincidencias de acuerdo con la pregunta
# [0] Arrojar resultado de coincidencias

# [0] Contar coincidencias pregunta a términos
# [0] Ciclo for para contar
# [0] Ordenar por orden descendente de conincidencias

# [0] Mostrar al usuario el término con mayores coincidencias
