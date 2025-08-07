import jsonschema
import pytest
import requests
import json

from VariableGlobal import URI_BASE_OBJECTS,ID_PLAYLIST2


@pytest.mark.smoke
@pytest.mark.regression
def test_001_add_objects():
    # Descripción: El usuario desea modificatos atributos de los objetos

    url = URI_BASE_OBJECTS
    # Paso 1: Seleccionar PUT
    list_url = url +"/objects/"+ID_PLAYLIST2

    # Body de entrada
    payload = json.dumps({
        "name": "Daniela Mac16",
        "data": {
            "year": 2025,
            "price": 2013,
            "CPU model": "Intel",
            "Hard disk size": "1TB",
            "color": "silver"
        }
    })

    # Headers
    headers = {"Content-Type": "application/json"}
    response = requests.put(list_url,headers=headers,data=payload)
    assert response.status_code == 200

#Prioridad : Media
