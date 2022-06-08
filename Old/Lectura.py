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
    # [1] Importar archivo json
    # [1] Meterlo a python como diccionario 
        # (Con utf-8, por los acentos y todo)
    # [1] Pasarlos por pandas (No sirve)
# [1] Preparar texto
    # [1] Quitar los nombres y sólo dejar los valores (nombre:valor)
    # [1] Convertir a string


import json
with open('BaseDatos/Statenvertaling.json', 'r', encoding='utf-8') as statenFile:
    staten = json.load(statenFile)
    print('''--------------
Archivo JSON ingresado como DICT''')
    print('Con', len(staten), 'atributos:')
    print('--------------')
for key,value in staten.items():
    print(key)
    statenValue = (str(value))




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


import spacy
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


# [0] Buscar coincidencias en lista de términos con lista de pregunta
    # [0] Usar set para evita coincidencias repetidas 
    # [0] Crear lista de coincidencias
    # [0] Contar número de coincidencias

coincidencias = []
coincidenciasSet = []
for eS in statenLista:
    for eP in preguntaLista:
        if set(eS) == set(eP):
            coincidencias.append(eS)
            coincidenciasSet = set(coincidencias)
print('Hemos encontrado', len(coincidenciasSet), 'coincidencias:')
print(coincidenciasSet)