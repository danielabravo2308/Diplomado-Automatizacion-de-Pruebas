import json

import jsonschema
import pytest
import requests
import logging

from pytest import mark
from VariableGlobal import URI_BASE_SPOTIFY, TOKEN_SPOTIFY, TOKEN_SPOTIFY_INVALID, ID_USER, ID_USER_INVALID
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)



""" TC001: Validar que el endpoint POST/ playlists crea exitosamente una playlist con un payload de entrada valida"""
@mark.playlist
@mark.functional_positive
def test_001_payload_input_valid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url +f"/{ID_USER}"+"/playlists"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_entrada = {
        "name": "Playlist TEST Daniela",
        "description": "Playlist creada con la API",
         "public": False
    }

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)


    response = requests.post(list_url, headers=headers,json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 201

#------------------------------------------------------------------------------------
""" TC002: Validar que el endpoint POST/playlists rechaza la creacion de un playlist con un payload invalido"""

@mark.playlist
@mark.functional_negative
def test_002_payload_input_invalid():
  url = URI_BASE_SPOTIFY+"/v1/users"
  list_url = url + f"/{ID_USER}" + "/playlists"

  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer{TOKEN_SPOTIFY}"
    }

  payload_entrada = {
    "name": "Playlist TEST Daniela",
    "description": "Playlist creada con la API",
    "public" : False
  }

  logger.info("domain%s", list_url)
  logger.debug("request+headers:PUT  %s %s", list_url, headers)
  logger.debug("payload: %s", payload_entrada)

  response = requests.post(list_url, headers=headers, json=payload_entrada)

  logger.info("status code: %s", response.status_code)
  logger.debug("response: %s", response.json())

  assert response.status_code == 400

#------------------------------------------------------------------------

""" TC003:  Verificar  que se rechace la solicitud de crear Playlist si el token de Authorization es invalido o esta expirado"""
@mark.playlist
@mark.functional_negative
def test_003_token_invalid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}" + "/playlists"
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {TOKEN_SPOTIFY_INVALID}"
    }

    payload_entrada = {
      "name": "Playlist TEST Daniela",
      "description": "Playlist creada con la API",
      "public": False
    }

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 401

#------------------------------------------------------------------------------------
""" TC004:  Verificar  que  la solicitud de crear Playlist se realice correctamente con token de Authorization es invalido """
@mark.playlist
@mark.functional_positive
def test_004_token_valid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}" + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_entrada = {
        "name": "Playlist TEST Daniela",
        "description": "Playlist creada con la API",
        "public": False
    }
    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 201

#----------------------------------------------------------------------------------

""" TC005: Verificar la creación de una playlist utilizando “user_id” del usuario autenticado correctamente """
@mark.playlist
@mark.functional_positive
def test_005_create_playlist_user_valido():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}"+"/playlists"
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_entrada = {
        "name": "Playlist TEST ",
        "description": "Playlist creada con la API",
        "public": False
    }
    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers,json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 201

#--------------------------------------------------------------------------------
""" TC006: Verificar que se rechace la creación de una playlist usando un “user_id” no autorizado """
@mark.playlist
@mark.functional_negative
def test_006_create_playlist_user_invalid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER_INVALID}"+"/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_entrada = {
        "name": "Playlist TEST ",
        "description": "Playlist creada con la API",
        "public": False
    }

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 403

#----------------------------------------------------------------------------
"""TC007 : Verificar que se pueda crear un playlist con solo campos obligatorios """
@mark.playlist
@mark.functional_positive
def test_007_create_playlist_campos_required():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}" + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_entrada = {
        "name": "Playlist TEST ",
        "description": "Playlist creada con la API",
        "public": False
    }
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
              ]
            }
    try:
        jsonschema.validate(instance=payload_entrada, schema=schema)
    except ValueError as e:
        assert False , f"El payload no cumple el esquema"

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("Schema de respuesta recibido: %s", json.dumps(schema, indent=2))
    logger.debug("response: %s", response.json())

    assert response.status_code == 201, f"Se esperaba 201, pero se recibió {response.status_code}"


#-------------------------------------------------------------------------------
"""TC008 : Verificar que se rechace crear un playlist al no ingresar los  campos obligatorios"""
@mark.playlist
@mark.functional_negative
def test_008_create_playlist_campos_not_required():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}" + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    payload_entrada = {
        # "name": "Playlist TEST ",
        "description": "Playlist creada con la API",
        "public": False
    }
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
            #   "required": [
            #   "name",
            # ]

            }
    try:
        jsonschema.validate(instance=payload_entrada, schema=schema)
    except ValueError as e:
        assert False , f"El payload no cumple el esquema {e.message}"

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("Schema de respuesta recibido: %s", json.dumps(schema, indent=2))
    logger.debug("response: %s", response.json())

    assert response.status_code == 400, f"Se esperaba 201, pero se recibió {response.status_code}"




# -------------------------------PRUEBAS EXTRAS DE VALIDACION DE ENTRADA-------------------------------
#     """ Se tiene el siguiente esquema del payload de entrada
#
#             schema = {
#                 "$schema": "http://json-schema.org/draft-07/schema#",
#                 "title": "Generated schema for Root",
#                 "type": "object",
#                 "properties": {
#                 "name": {
#                 "type": "string"
#             },
#                 "description": {
#                  "type": "string"
#             },
#                 "public": {
#                 "type": "boolean"
#             }
#             },
#              "required": [
#              "name",
#             "description",
#             "public"
#         ]
#         }
#
# """


# LO VALIDA BIEN EL NAME solo permite cadenas
#""" TC0010:  Verificar  si valida las entradas del payload de entrada en el campo name que es cadena y se ingresa numeros"""
@mark.playlist
@mark.functional_negative
def test_0010_input_name_invalid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}" + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_entrada = {
        "name": 1234,
        "description": "Playlist creada con la API",
        "public": "False"
    }

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("schema : %s , schema.json() ")
    logger.debug("response: %s", response.json())

    assert response.status_code == 400

#-------------------------------------------------------------------------

@pytest.mark.xfail(reason="La app permite numeros en el atributo description BUG001",run=True)
#""" TC0011:  Verificar  si valida las entradas del payload de entrada en el campo description que es cadena y se ingresa numeros"""
@mark.playlist
@mark.functional_negative
def test_0011_input_description_invalid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}"+ "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_entrada = {
        "name": "lo que sea",
        "description": 56566,
        "public": "False"
    }

    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("schema : %s , schema.json() ")
    logger.debug("response: %s", response.json())

    print(response.status_code)
    assert response.status_code == 400

#----------------------------------------------------------------------------
@mark.playlist
@mark.functional_negative
@pytest.mark.xfail(reason="La app permite letras en el public BUG002",run=True)
#""" TC009:  Verificar  si valida las entradas del payload de entrada en el campo public que es un boolean y se ingresa cadena"""
def test_009_input_public_invalid():
    url = URI_BASE_SPOTIFY+"/v1/users"
    list_url = url + f"/{ID_USER}" + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    payload_entrada = {
        "name": "Playlist TEST Daniela",
        "description": "Playlist creada con la API",
        "public": "False"
    }
    logger.info("domain%s", list_url)
    logger.debug("request+headers:PUT  %s %s", list_url, headers)
    logger.debug("payload: %s", payload_entrada)

    response = requests.post(list_url, headers=headers, json=payload_entrada)

    logger.info("status code: %s", response.status_code)
    logger.debug("schema : %s , schema.json() ")
    logger.debug("response: %s", response.json())
    assert response.status_code == 400

#-----------------------------------------------------------------------








