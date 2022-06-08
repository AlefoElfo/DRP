# [0] Buscar coincidencias en lista de términos con lista de pregunta
    # [0] Usar set para evita coincidencias repetidas
    # [0] Crear lista de coincidencias
    # [0] Contar número de coincidencias

coincidencias = []
for eS in statenLista:
    for eP in preguntaLista:
        if set(eS) == set(eP):
            coincidencias.append(eS)
            coincidenciasSet = set(coincidencias)
print('Hemos encontrado', len(coincidenciasSet), 'coincidencias:')
print(coincidenciasSet)


# [0] Mostrar al usuario el término con mayores coincidencias