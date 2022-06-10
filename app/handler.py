import json

def json_input(file):
    """
    leer datos del json local
    """
    with open(file, 'rb') as file:
        data = json.load(file)
    return data
