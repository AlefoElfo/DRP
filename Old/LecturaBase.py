import pandas as pd
import json

path = 'D:\OneDrive\Proyectos\DRP\BaseDatos\Definiciones.xlsx'
df = pd.read_excel(path, sheet_name='Definiciones')
print(df)



## Json
with open('Statenvertaling.json', 'r', encoding='utf-8') as statenFile:
    staten = json.load(statenFile)
    print('''--------------
Archivo JSON ingresado como DICT''')
    print('Con', len(staten), 'atributos:')
    print('--------------')
for key,value in staten.items():
    print(key)
    statenValue = (str(value))

print(statenValue)

df = pd.DataFrame(list)
