import json
def fnObtenerDato(sArchivo):
 with open(sArchivo) as f:
     data = json.load(f)
     return data