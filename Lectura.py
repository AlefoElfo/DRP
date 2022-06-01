# [1] Digitalizar término statenvertaling
    # [1]Relaciones semánticas del lexema
    # [1]Definición
    # [1]Meterlos en formato json
# [0] (2a versión) Digitalizar 5 términos
    # [0]Hacer tesauro manual
    # [0]Agregar definición
    # [0]Meterlos en formato json





# [1] JSON en Python
    # [0] Instalar pandas
        # (No sirve porque pandas pide el mismo número de filas en archivos json. Lo dejo por si luego se resuelve)
    # [0] Importar pandas
    # [1] Importar json
    # [1] Meterlo a python como diccionario 
    # [1] Pasarlos por pandas (No sirve)

import json
with open('Statenvertaling.json', 'r', encoding='utf-8') as statenFile:
    staten = json.load(statenFile)
    print('Archivo JSON recibido con', len(staten), 'atributos:')
for key,value in staten.items():
    print(key)
    statenValue = (str(value))
#PENDIENTES
# 1. ¿Cómo especificar si el atributo tiene una lista, tupla o diccionario?




# [1] Importar spacy
    # [1] Instalar spaCy
        # [1] En anaconda prompt (base)
        # [1] Instalar modelo de español profundo
        # [1] Ver que el intérprete sea el mismo (python 3.9.7 base:conda)
    # [1] Importar spacy
    # [1] Añadir 

# ESTE CÓDIGO FUNCIONA, PERO NO PUEDO GENERAR UNA VARIABLE CON EL RESULTADO FINAL
# import spacy
# nlp = spacy.load('es_dep_news_trf')
# statenNLP = nlp(statenValue)
# print('Archivo analizado por IA')
# for token in statenNLP:
#     if token.is_alpha:
#         print(token.text)


import spacy
nlp = spacy.load('es_dep_news_trf')
statenNLP = nlp(statenValue)
print('Archivo analizado por IA')
for token in statenNLP:
    if token.is_alpha:
        print(token.text)

# [0] Pasarlos por spacy.nlp
    # [0] Convertir a lemmas
    # [0] Eliminar palabras innecesarias


# [0] Preparar texto (No es tan necesario porque es texto introducido manualmente)
# [0] Limpiar texto con una función
# [0] Quitar los nombres y sólo dejar los valores

# with staten as statenKey:
#    staten.items
# for key in staten.items():
#    print(key, ":", value)


# [0] Hacer input de pregunta natural
    # [0] pasar pregunta por spacy.nlp
    # [0] Eliminar palabras innecesarias
    # [0] Convertir a lemmas

# [0] Crear función para leer los json
    # [0] For lectura in jsonFIle:
    # [0] buscar en nombre, hiperónimos, cohipónimos, hipónimos, polisemia, antonimia, meronimia, definición
    # [0] Contar coincidencias de acuerdo con la pregunta
    # [0] Arrojar resultado de coincidencias

# [0] Contar coincidencias pregunta a términos
    # [0] Ciclo for para contar
    # [0] Ordenar por orden descendente de conincidencias

# [0] Mostrar al usuario el término con mayores coincidencias
