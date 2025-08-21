import jsonschema
import requests
import logging
import pytest

from pytest import mark
from VariableGlobal import URI_BASE_SPOTIFY, ID_PLAYLIST, ID_PLAYLIST_INVALID, TOKEN_SPOTIFY, TOKEN_SPOTIFY_INVALID

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


""" TC001: Verificar que la solicitud de obtener playlist con “playlist_id” válido retorne 
la información y código 200"""

@mark.playlist
@mark.smoke
@mark.functional_positive
def test_001_get_playlist_by_id_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    list_response = response.json()
    assert "id" in list_response
    assert response.status_code == 200

"""TC002: Verificar que se rechace la solicitud de obtener playlist con  “playlist_id”   
no existente y retorne codigo 400 """

@mark.playlist
@mark.functional_negative
def test_002_get_playlist_by_id_not_found():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST_INVALID}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer{TOKEN_SPOTIFY}"
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400


"""TC003: Verificar  respuesta exitosa al obtener el playlist por su “playlist_id” ingresando 
un token  valido retorne codigo 200"""

@mark.playlist
@mark.functional_positive
@mark.smoke

def test_003_get_playlist_by_id_with_token_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200

"""TC004: Verificar que se rechace la solicitud de obtener playlist por su “playlist_id” al 
ingresar un token invalido o expirado retornar codigo de 401"""
@mark.playlist
@mark.functional_negative

def test_004_get_playlist_by_id_with_token_invalid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY_INVALID}"
    }
    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 401


""" TC005: Verificar que se rechace la solicitud de obtener playlist por su “playlist_id” al 
ingresar un token vacío retornar codigo de 401 """
def test_005_get_playlist_by_id_with_token_empty():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {}
    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 401

"""TC006: Verificar que el payload de salida contenga los campos requeridos según el schema de salida"""
@mark.playlist
@mark.functional
@mark.smoke

def test_006_validate_output_payload():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN_SPOTIFY}"
        }

    schema_playlist = {
    "title": "Generated schema for Root",
    "type": "object",
    "properties": {
        "collaborative": {
            "type": "boolean"
        },
        "description": {
            "type": "string"
        },
        "external_urls": {
            "type": "object",
            "properties": {
                "spotify": {
                    "type": "string"
                }
            },
            "required": [
                "spotify"
            ]
        },
        "followers": {
            "type": "object",
            "properties": {
                "href": {},
                "total": {
                    "type": "number"
                }
            },
            "required": [
                "href",
                "total"
            ]
        },
        "href": {
            "type": "string"
        },
        "id": {
            "type": "string"
        },
        "images": {},
        "name": {
            "type": "string"
        },
        "owner": {
            "type": "object",
            "properties": {
                "display_name": {
                    "type": "string"
                },
                "external_urls": {
                    "type": "object",
                    "properties": {
                        "spotify": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "spotify"
                    ]
                },
                "href": {
                    "type": "string"
                },
                "id": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "uri": {
                    "type": "string"
                }
            },
            "required": [
                "display_name",
                "external_urls",
                "href",
                "id",
                "type",
                "uri"
            ]
        },
        "primary_color": {},
        "public": {
            "type": "boolean"
        },
        "snapshot_id": {
            "type": "string"
        },
        "tracks": {
            "type": "object",
            "properties": {
                "href": {
                    "type": "string"
                },
                "items": {
                    "type": "array",
                    "items": {}
                },
                "limit": {
                    "type": "number"
                },
                "next": {},
                "offset": {
                    "type": "number"
                },
                "previous": {},
                "total": {
                    "type": "number"
                }
            },
            "required": [
                "href",
                "items",
                "limit",
                "next",
                "offset",
                "previous",
                "total"
            ]
        },
        "type": {
            "type": "string"
        },
        "uri": {
            "type": "string"
        }
    },
    "required": [
        "collaborative",
        "description",
        "external_urls",
        "followers",
        "href",
        "id",
        "images",
        "name",
        "owner",
        "primary_color",
        "public",
        "snapshot_id",
        "tracks",
        "type",
        "uri"
    ]
}
    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)
    payload_salida = response.json()
    try:
        jsonschema.validate(instance=payload_salida, schema=schema_playlist)
    except ValueError as e:
        assert False , f"El payload no cumple el esquema {e.message}"

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

"""TC007:Verificar que el parámetro “fields” devuelve únicamente los campos solicitados en la 
respuesta de la playlist"""
@mark.playlist
@mark.functional_positive
def test_007_get_playlist_by_fields_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers={
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json",
    }
    params={
        "fields": "name"
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)
    logger.debug("params: %s", params)

    response = requests.get(list_url, headers=headers, params=params)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200

"""TC008: Verificar que al  ingresar un campo inexistente en “fields” muestre lista vacia y un codigo de 200 """

@mark.playlist
@mark.functional_negative
def test_008_get_playlist_by_fields_invalid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers={
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json",
    }
    params={
        "fields": "loquesea"
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)
    logger.debug("params: %s", params)

    response = requests.get(list_url, headers=headers, params=params)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200
    assert response.json() == {}

"""TC009:TC009:Verificar que la solicitud de obtener playlist por “playlist_id”
 responda en menos de 1 segundo"""

@mark.playlist
@mark.performance
def test_009_get_playlist_response_time():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json"
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    # Validar status code
    assert response.status_code == 200

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    # Validar tiempo de respuesta (en segundos)
    max_response_time = 1.0  # 1 segundo
    elapsed = response.elapsed.total_seconds()

    logger.info("time response: %s", elapsed)

    assert elapsed <= max_response_time, f"Tiempo de respuesta muy alto: {elapsed} segundos"

"""TC010: Verificar que el query params 'market' se envie con un valor válido y que la respuesta sea 200 """
@mark.playlist
@mark.functional_positive
@mark.smoke
def test_010_verify_market_value_valid():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json"
    }
    params={
        "market": "US" #market con valor valido
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers, params=params)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200

"""TC011: Verificar que el query params 'market' se envie con un valor inválido y que la respuesta sea 400"""
@pytest.mark.xfail(reason="La app permite filtrar playlist con un parametro market no existente BUG001",run=True)
@mark.playlist
@mark.functional_negative
def test_011_verify_market_value_not_found():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json"
    }
    params={
        "market": "PWD" #market con valor invalido
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers, params=params)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400

"""TC012: Verificar que el query params 'market' se envie con un valor numérico y que la respuesta sea 400"""
@pytest.mark.xfail(reason="La app permite filtrar playlist con un parametro market con valor numerico BUG002",run=True)
@mark.playlist
@mark.functional_negative
def test_012_verify_market_value_numeric():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json"
    }
    params={
        "market": "12345" #market con valor invalido
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers, params=params)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400

"""TC013:  Verificar que el query params 'market' se envie con caracteres especiales y que la respuesta sea 400"""
@pytest.mark.xfail(reason="La app permite filtrar playlist con un parametro market con valores de caracteres especiales BUG002",run=True)
@mark.playlist
@mark.functional_negative
def test_013_verify_market_value_special_characteres():
    list_url = f"{URI_BASE_SPOTIFY}/v1/playlists/{ID_PLAYLIST}"
    headers = {
        "Authorization": f"Bearer {TOKEN_SPOTIFY}",
        "Content-Type": "application/json"
    }
    params={
        "market": "$%#$" #market con caracteres especiales
    }

    logger.info("domain %s", list_url)
    logger.debug("request+headers:GET  %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers, params=params)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 400












