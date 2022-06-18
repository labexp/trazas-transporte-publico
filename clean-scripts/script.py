import os
import pandas as pd
import sys
'''
Funcion que lista las rutas de los archivos de tipo csv encontrados en la ruta 
entrante, se excluye el directorio 'asistentes'.
Parametros:
    - root: ruta d
Salida:
    - paths: lista de rutas de los csv encontrados
'''
def find_csv(root, pattern):
    paths = []
    for path, subdirs, files in os.walk(root):
        if 'asistentes' in subdirs:
            subdirs.remove('asistentes')
        for name in files:
            p = name.split('.')[-1]
            if p == pattern:
                paths.append(os.path.join(path, name))
    return paths


args = sys.argv[1]
ruta = args
pattern = "csv"   
paths = find_csv(ruta, pattern)
result = pd.concat([pd.read_csv(i) for i in paths ] )
result.to_csv("result.csv", index=False)

