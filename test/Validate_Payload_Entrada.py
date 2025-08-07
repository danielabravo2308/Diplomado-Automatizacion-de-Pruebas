
""" VALIDAR PAYLOAD DE ENTRADA solo para metodos POST y PUT
    Para este ejemplo se evaluara con el metodo POST
    Se usa Schema para validar estos payloads"""

import jsonschema
import pytest
import requests
import json

from VariableGlobal import URI_BASE_OBJECTS


@pytest.mark.smoke
@pytest.mark.regression
def test_001_add_objects():
    # Descripción: El usuario debe añadir objetos correctamente

    get_url = URI_BASE_OBJECTS
    # Paso 1: Seleccionar POST
    list_url = get_url + "/objects"

    # Body de entrada
    payload_entrada = json.dumps({
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

    # Envío del request
    response = requests.post(list_url, headers=headers, data=payload_entrada)

    # Verificar que el estado correcto sea 200
    assert response.status_code == 200

    # Definición del esquema esperado
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "number"},
                    "price": {"type": "number"},
                    "CPU model": {"type": "string"},
                    "Hard disk size": {"type": "string"},
                    "color": {"type": "string"}
                },
                "required": [
                    "year", "price", "CPU model",
                    "Hard disk size", "color"
                ]
            }
        },
        "required": ["name", "data"]
    }

    # Validación del esquema de la respuesta
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")



#Prioridad : Media
