
import pytest
import requests
import logging
from pytest import mark

from VariableGlobal import URI_BASE_SPOTIFY, TOKEN_SPOTIFY, TOKEN_SPOTIFY_INVALID
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

""" TC001:  Verificar que el usuario autenticado pueda obtener su lista de "PlayList" exitosamente """

@mark.playlist
@mark.smoke
@mark.functional
def test_001_Obtener_la_lista_de_playlists():
    url = URI_BASE_SPOTIFY

    # Paso 1: Ingresar Token de Cuenta Personal
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    # Paso 2: Llamar el recurso playlist
    list_url = url + "/playlists"

    logger.info("domain%s", url)
    logger.debug("request+headers:PUT  %s %s", url, headers)

    # Paso 3: Seleccionar método GET y enviar request
    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    # Paso 4: Verificar que el estado sea 200
    assert response.status_code == 200


""" TIPO DE VALIDACION : 
    1.Status Code
    2.Verb Requests"""

#-----------------------------------------------------------------------------
""" TC002:  Validar que se rechace la solicitud si el token de Authorization es invalido o esta expirados """

@mark.playlist
@mark.functional_negative
def test_002_token_invalid():

    url = URI_BASE_SPOTIFY
    list_url = url+"/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY_INVALID}"

    }
    logger.info("Domain: %s", list_url)
    logger.debug("Request + Headers: GET %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 401

#-------------------------------------------------------------------------------------------
"""TC003: Validar  la solicitud si el token de Authorization es valido """

@mark.playlist
@mark.functional_positive
def test_003_token_valid():
    url = URI_BASE_SPOTIFY
    list_url = url + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"

    }

    logger.info("Domain: %s", list_url)
    logger.debug("Request + Headers: GET %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())

    assert response.status_code == 200


#-------------------------------------------------------------------------------------------
""" TC004:  Verificar que el usuario autenticado reciba correctamente las playlist al aplicar filtros por query parameter por id"""
@mark.playlist
@mark.smoke
@mark.functional
def test_004_filter_by_Ids():
  url = URI_BASE_SPOTIFY
  list_url = url + "/playlists"

  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

  params = {"id": "1,2"}

  logger.info("Domain: %s", list_url)
  logger.debug("Request + Headers: GET %s %s", list_url, headers)

  response = requests.get(list_url, headers=headers, params=params)
  data = response.json()

  # Validar que los objetos tengan ID 1 o 2
  ids_esperado = ["1", "2"]
  if isinstance(data, list):
      for obj in data:
        assert obj["id"] in ids_esperado
  logger.info("status code: %s", response.status_code)
  logger.debug("response: %s", data)

#------------------------------------------------------------------------------
"""TC005: Verificar que el usuario autenticado reciba correctamente las playlist al aplicar filtros por query parameters por limit"""
#limit :  limita la cantidad de resultados  que devuelve la API en una sola respuesta
@mark.playlist
@mark.smoke
@mark.functional
def test_005_filter_by_query_params_limit():
    url = URI_BASE_SPOTIFY
    list_url = url + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    params = {"limit": 35}

    logger.info("Domain: %s", list_url)
    logger.debug("Request + Headers: GET %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers, params=params)
    list_data = response.json()
    if "items" in list_data:
        cantidad_playlist = len(list_data["items"])
        assert cantidad_playlist == 35

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())
#------------------------------------------------------------------------------
""" TC006: Verifique que la API responda en formato JSON con los campos esperados"""
@mark.playlist
@mark.functional
def test_006_validate_response_JSON():
    url = URI_BASE_SPOTIFY
    list_url = url + "/playlists"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }

    logger.info("Domain: %s", list_url)
    logger.debug("Request + Headers: GET %s %s", list_url, headers)

    response = requests.get(list_url, headers=headers)
    header_Actual = response.headers.get("Content-Type","")
    assert "application/json" in header_Actual

    logger.info("status code: %s", response.status_code)
    logger.debug("response: %s", response.json())
    #assert isinstance(response.json(), dict)
#-------------------------------------------------------------------------------------
"""TC007: Verificar que el header “Authorization “ tenga el prefijo “Bearer”"""
@pytest.mark.functional
@pytest.mark.smoke
def test_007_validate_response_headers():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN_SPOTIFY}"
    }
    assert headers["Authorization"].startswith("Bearer")

#-------------------------------------------------------------------------------------











