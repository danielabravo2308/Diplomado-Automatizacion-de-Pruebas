import jsonschema
import pytest
import requests
import json

from VariableGlobal import URI_BASE_OBJECTS

################  EXAMPLE BUG NOT VALIDATE DATA ########################

@pytest.mark.smoke
@pytest.mark.regression
def test_002_add_objects_with_anio_limit_invalid():
    # Descripción: El usuario debe añadir objetos correctamente

    get_url = URI_BASE_OBJECTS
    # Paso 1: Seleccionar POST
    list_url = get_url + "/objects"

    # Body de entrada
    payload = json.dumps({
        "name": "Daniela Mac16",
        "data": {
            "year": 456465465,    # Se tiene Bug no deberia validar este atributo sobrepasa a un año valido
            "price": 2013,
            "CPU model": "Intel",
            "Hard disk size": "1TB",
            "color": "silver"
        }
    })

    # Headers
    headers = {"Content-Type": "application/json"}

    # Envío del request
    response = requests.post(list_url, headers=headers, data=payload)

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
        #assert_create_object_response_schema(response)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")

#Prioridad : Media
#El TestCase Pasa a pesar que se introdujo un dato invalido en su JSON y se debria considerar Bug
