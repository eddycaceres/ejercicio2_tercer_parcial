import json

def modificar_json():
    with open('datos.json', 'r') as file:
        data = json.load(file)

    data['name'] = 'Andres Iniesta Perez'

    ultimo_club = {
        "name": "Kobe Vissel",
        "period": "2018-present"
    }
    data['clubs'].append(ultimo_club)

    with open('datos_modificado.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    modificar_json()
