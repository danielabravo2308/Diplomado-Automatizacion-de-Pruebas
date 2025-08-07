""" VALIDAR PAYLOAD DE ENTRADA solo para metodos POST y PUT
    Para este ejemplo se evaluara con el metodo PUT"""

import jsonschema
import pytest
import requests
import json

from VariableGlobal import URI_BASE_OBJECTS,ID_OBJECT



@pytest.mark.smoke
@pytest.mark.regression
def test_001_add_objects():
    # Descripción: El usuario debe añadir objetos correctamente

    get_url = URI_BASE_OBJECTS
    # Paso 1: Seleccionar POST
    list_url = get_url + "/objects/"+ID_OBJECT

    # Body de salida
    payload_salida = json.dumps({
    "id": "ff8081819782e69e01984385ed49265e",
    "name": "Daniela Mac16",
    "updatedAt": "2025-07-31T19:05:18.945+00:00",
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
    response = requests.put(list_url, headers=headers, data=payload_salida)

    # Verificar que el estado correcto sea 200
    assert response.status_code == 200

    # Definición del esquema esperado
    schema = {
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "id": {
                "type": "string"
            },
            "name": {
                "type": "string"
            },
            "updatedAt": {
                "type": "string"
            },
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
                    "year", "price", "CPU model", "Hard disk size", "color"
                ]
            }
        },
        "required": ["id", "name", "updatedAt", "data"]
    }

    # Validación del esquema de la respuesta
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")


#Prioridad : Media
