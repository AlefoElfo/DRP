# DRP
## Pasos
* Digitalizar término statenvertaling
  * Relaciones semánticas del lexema
  * Definición
* (2a versión) Digitalizar 5 términos
  * Hacer tesauro manual
  * Agregar definición
* Meterlos en formato json
* Pasarlos por pandas
* Pasarlos por spacy.nlp
  * Eliminar palabras innecesarias
  * Convertir a lemmas
* Hacer input de pregunta natural
* pasar pregunta por spacy.nlp
  * Eliminar palabras innecesarias
  * Convertir a lemmas
* Contar coincidencias pregunta a términos
  * Ciclo for para contar
  * Ordenar por orden descendente de conincidencias
* Mostrar al usuario el término con mayores coincidencias
