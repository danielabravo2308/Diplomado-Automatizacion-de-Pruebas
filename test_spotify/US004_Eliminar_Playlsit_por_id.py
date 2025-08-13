import jsonschema
import pytest
import requests
import logging

from pytest import mark
from VariableGlobal import URI_BASE_SPOTIFY, ID_PLAYLIST, ID_PLAYLIST_INVALID, TOKEN_SPOTIFY, TOKEN_SPOTIFY_INVALID , TOKEN_SPOTIFY_EMPTY, ID_PLAYLIST_EMPTY


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

"""TC001: Verificar eliminación de un “track” mediante el  “playlist_id” 
válido y URI correcto, retornando código 200
"""
@mark.playlist
@mark.functional_positive
def test_001_delete_playlist_by_id_and_body_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",

            }
        ]
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200



""" TC002: Verificar que eliminar “track” mediante un “playlist_id”
 incorrecto body de entrada válido retorne código 400"""
@mark.playlist
@mark.functional_negative
def test_002_delete_playlist_by_id_invalid_and_body_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST_INVALID}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",

            }
        ]
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400

"""TC003: Verificar que eliminar “track” mediante un  “playlist_id” valido
 y  el body entrada invalido retorne codigo 400"""

@mark.playlist
@mark.functional_negative
def test_003_delete_playlist_by_id_valid_and_body_invalid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
         "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST_INVALID}",

            }
        ]
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400


"""TC004: Verificar que eliminar “track” mediante un  “´playlist_id” valido 
y el body de entrada vacia retorne codigo 400"""
@mark.playlist
@mark.functional_negative
def test_004_delete_playlist_by_id_valid_and_body_empty():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
         "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST_EMPTY}",

            }
        ]
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400



""" TC005: Verificar que eliminar “track” mediante su “playlist_id”, con token valido retorne codigo  200"""
@mark.playlist
@mark.functional_positive
def test_005_delete_playlist_by_id_with_token_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
            }

        ]
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200


"""TC006: Verificar que eliminar “track” mediante  “playlist_id”  con token inválido o expirado retorne 
código 401 Unauthorized """
@mark.playlist
@mark.functional_negative
def test_006_delete_playlist_by_id_with_token_invalid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY_INVALID}"
    }
    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
            }

        ]
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 401

"""TC007: Verificar que eliminar “track”  mediante “playlist_id” con token vacío retorne 
código 401 Unauthorized """
@mark.playlist
@mark.functional_negative
def test_007_delete_playlist_by_id_with_token_empty():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY_EMPTY}"
    }
    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
            }

        ]
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400

"""TC008: Validar que la respuesta incluya header “Content-Type” con valor “application/json” """
@mark.playlist
@mark.functional_negative
def test_008_validate_header_JSON():
   list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
   headers = {
       "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
   }
   payload_input = {
       "tracks": [
           {
               "uri": f"spotify:track:{ID_PLAYLIST}",
           }

       ]
   }

   logger.info("domain %s", list_url)
   logger.debug("request+headers:DELETE  %s %s", list_url, headers)
   logger.debug("payload input %s", payload_input)

   response=requests.delete(list_url, headers=headers, json=payload_input)

   logger.info("status code: %s", response.status_code)
   logger.debug("response: %s", response.json())

   get_content_type = response.headers.get('Content-Type')

   logger.debug("get_content_type: %s", get_content_type)

   assert get_content_type.startswith('application/json')

   assert response.status_code == 200

"""TC009: Validar que el atributo snapshot_id en la respuesta sea de tipo string """
def test_009_validate_snapshot_id():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
            }

        ]
    }

    schema_output = {
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
        "snapshot_id": {
            "type": "string"
        }
            },
        "required": [
                    "snapshot_id"
        ]
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)
    try:
        jsonschema.validate(instance=response.json(), schema=schema_output)
    except ValueError as e:
        assert False, f"El payload no cumple el esquema {e.message}"

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200

"""TC0010: Verificar eliminación exitosa de “tracks” mediante su “playlist_id” y posiciones válidas 
positivas, retorna código 200"""
@mark.playlist
@mark.functional_positive

def test_0010_delete_by_playlist_id_with_position_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
                "position": [1,2]
            }

        ]
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    # logger.debug("response: %s", response.json())

    assert response.status_code == 200

"""TC0011: Verificar que eliminar “tracks” mediante su “playlist_id” y body de entrada valida
 y  con posiciones negativas retorne error """
@pytest.mark.xfail(reason="La app permite eliminar track al ingresar posicion con valor negativo BUG004",run=True)

@mark.playlist
@mark.functional_negative
def test_0011_delete_by_playlist_id_with_position_invalid_negative():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
                "positions": [-40]
            }

        ]
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    # logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    # logger.debug("response: %s", response.json())

    assert response.status_code == 400


"""TC0012: Verificar que eliminar “tracks” mediante su “playlist_id” y body de entrada valida 
y con posiciones fuera de rango retorne error """
@pytest.mark.xfail(reason="La app permite eliminar track al ingresar posicion que sobrepasa el limite BUG005",run=True)

@mark.playlist
@mark.functional_negative
def test_0012_delete_by_playlist_id_with_position_limit():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}/tracks"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_input = {
        "tracks": [
            {
                "uri": f"spotify:track:{ID_PLAYLIST}",
                "positions": [999999999999999999999]
            }

        ]
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:DELETE  %s %s", list_url, headers)
    # logger.debug("payload input %s", payload_input)

    response = requests.delete(list_url, headers=headers, json=payload_input)

    logger.info("status code: %s", response.status_code)
    # logger.debug("response: %s", response.json())

    assert response.status_code == 400