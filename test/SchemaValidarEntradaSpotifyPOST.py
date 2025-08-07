import jsonschema
import pytest
import requests
import json


from VariableGlobal import URI_BASE_SPOTIFY, ID_PLAYLIST


####################################### EXAMPLE SPOTIFY #################################33
@pytest.mark.smoke
@pytest.mark.regression
def test_001_add_airports():
    # Descripción: El usuario debe crear PlayList

    get_url = URI_BASE_SPOTIFY
    # Paso 1: Seleccionar POST
    list_url = get_url+"/"+ID_PLAYLIST +"/playlists"

    # Body de entrada
    payload = json.dumps({
         "name": "Playlist TEST Daniela",
         "description": "Playlist creada con la API",
        "public": "false"
    })

    # Headers
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer BQAjuui-_Nvkpq1tC8LpnrHOhiEXBbb271bKP6t_SMpJVbqvTiYg6XVkVQHlo0ntRO0sKE2W7Q14gXxZqdlwCkZ-IZp2i8SR73cJ2XN1RYUzTxVbTtI3JD6ezY4pKxdY1FXCqldRHK6aunngNeSFsn3CpkqTYDpG2p3evDkcIGOzsaJxZ7KJZIlmYvrO-lMvYCIcFHzCpwOXK5Z1gtJ5B9JT1s_9UHHpEEGpXT2MSYtm6Z9VZlR-kCgxsfF4XChdsF-kNUusjUtmNEfzvKPwIzWps1xLjDZhj9gCktd9iK1l0Ei8OTCRSqgbh3Dwf2H2WSDYu1HpwNDjOM614hfydjZGgz0"
            }

    # Envío del request
    response = requests.post(list_url, headers=headers, data=payload)

    # Verificar que el estado correcto sea 201 Created
    assert response.status_code == 201

    # Definición del esquema esperado
    schema = {
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "public": {
                "type": "boolean"
            }
        },
        "required": [
            "name",
            "description",
            "public"
        ]
    }

    # Validación del esquema de la respuesta
    try:
        jsonschema.validate(instance=response.json(), schema=schema)
    except jsonschema.exceptions.ValidationError as error:
        pytest.fail(f"JSON schema doesn't match: {error}")



#Prioridad : Media
