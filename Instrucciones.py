#ALGORITMO

# Digitalizar término statenvertaling[1]
    # Relaciones semánticas del lexema[1]
    # Definición[1]
    # Meterlos en formato json[1]
# (2a versión) Digitalizar 5 términos[0]
    # Hacer tesauro manual[0]
    # Agregar definición[0]
    # Meterlos en formato json[0]

#JSON en Python[0]
    # Instalar pandas[0] 
        # No sirve porque pandas pide el mismo número de filas en archivos json. Lo dejo por si luego se resuelve
    # Importar pandas, json[1] 
        # Sólo JSON
    # Meterlo a python como diccionario [1]
    # Pasarlos por pandas[1] No sirve.

import json
statenFile = open('D:\OneDrive\Proyectos\DRP\Statenvertaling.json', 'r', encoding='utf-8')
staten = json.load(statenFile)
statenFile.close()
type(staten)

# Pasarlos por spacy.nlp[0]
    # Instalar spaCy
    # Convertir a lemmas[0]
    # Eliminar palabras innecesarias[0]

# Hacer input de pregunta natural[0]
    # pasar pregunta por spacy.nlp[0]
    # Eliminar palabras innecesarias[0]
    # Convertir a lemmas[0]

# Contar coincidencias pregunta a términos[0]
    # Ciclo for para contar[0]
    # Ordenar por orden descendente de conincidencias[0]

# Mostrar al usuario el término con mayores coincidencias[0]
