import json


def findPizzaByName(name: str):
    with open('zania/mock_data.json', 'r') as file:
        json_data = json.load(file)
        for pizza in json_data:
            if pizza['name'].lower() == name.lower():
                file.close()
                return pizza

        file.close()
        return {}

def getIdAndPrice():
    res = dict()
    with open('zania/mock_data.json', 'r') as file:
        json_data = json.load(file)
        for pizza in json_data:
            res[pizza['id']] = pizza['price']

    file.close()
    return res