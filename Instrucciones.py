# [1] Digitalizar término statenvertaling
    # [1]Relaciones semánticas del lexema
    # [1]Definición
    # [1]Meterlos en formato json
# [0] (2a versión) Digitalizar 5 términos
    # [0]Hacer tesauro manual
    # [0]Agregar definición
    # [0]Meterlos en formato json

# [0] JSON en Python
    # [0] Instalar pandas
        # (No sirve porque pandas pide el mismo número de filas en archivos json. Lo dejo por si luego se resuelve)
    # [1] Importar pandas, json
        # (Sólo JSON)
    # [1] Meterlo a python como diccionario 
    # [1] Pasarlos por pandas (No sirve)

import json
with open('D:\OneDrive\Proyectos\DRP\Statenvertaling.json', 'r', encoding='utf-8') as statenFile:
    staten = json.load(statenFile)
    # Decoded JSON Data From File
    for key, value in staten.items():
        print(key, ":", value)
    # Done reading json file


# [0] Importar spacy
    # [1] Instalar spaCy
        # [1] En anaconda prompt (base)
        # [1] Instalar modelo de español profundo
        # [1] Ver que el intérprete sea el mismo (python 3.9.7 base:conda)
    # [1] Importar spacy


import spacy
spacy.load('es_dep_news_trf')

# [0] Pasarlos por spacy.nlp
    # [0] Convertir a lemmas
    # [0] Eliminar palabras innecesarias


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
