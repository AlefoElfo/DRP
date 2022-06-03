# [0] Hacer input de pregunta natural
    # [0] Pedir pregunta al usuario
    # [0] Convenrtir a string
    # [0] Limpiar puntuación
    # [0] Volver minúsculas
    # [0] pasar pregunta por spacy.nlp
    # [0] Eliminar palabras innecesarias
    # [0] Convertir a lemmas


print('''¡Hola! ¿No recuerdas el término?
¿Lo tienes en la punta de la lengua?
Escribe lo que recuerdes y buscaré la mejor opción:
''')
pregunta = str(input())

#LIMPIAR PREGUNTA
   
   
preguntaPunct = '[!¡"\#¿?()=,.-_:;]'
replace = ''
for str in pregunta:
    if str in preguntaPunct:
        pregunta = pregunta.replace(str, '')
preguntaLower = pregunta.lower()


print(preguntaLower)


# [0] Crear función para leer los json
    # [0] For lectura in jsonFIle:
    # [0] buscar en nombre, hiperónimos, cohipónimos, hipónimos, polisemia, antonimia, meronimia, definición
    # [0] Contar coincidencias de acuerdo con la pregunta
    # [0] Arrojar resultado de coincidencias

# [0] Contar coincidencias pregunta a términos
    # [0] Ciclo for para contar
    # [0] Ordenar por orden descendente de conincidencias

# [0] Mostrar al usuario el término con mayores coincidencias