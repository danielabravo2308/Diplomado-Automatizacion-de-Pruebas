import requests

""" Filtra correctamente el objeto por su Id"""

from VariableGlobal import URI_BASE_OBJECTS

def test_get_with_one_params():
    list_url = URI_BASE_OBJECTS+"/objects"
    params = {"id":"1"}
    response = requests.get(list_url, params=params)

    data = response.json()
    if isinstance(data,list):
        for objecto in data:
            assert objecto["name"] == "Google Pixel 6 Pro"
#-----------------------------------------------------------------------

""" Filtrar un objeto por su id y nombre"""
def test_get_object_by_id_and_name():
    list_url = URI_BASE_OBJECTS + "/objects"

    params = {
        "id": "3",
        "name": "Apple iPhone 12 Pro Max"
    }

    response = requests.get(list_url, params=params)
    data = response.json()

    # Si devuelve una lista, iteramos y verificamos los filtros
    if isinstance(data, list):
        for objecto in data:
            assert objecto["id"] == "3"
            assert objecto["name"] == "Apple iPhone 12 Pro Max"

#-------------------------------------------------------------------------------
""" Filtrar 2 objetos por sus Ids"""


def test_get_with_two_ids():
    list_url = URI_BASE_OBJECTS + "/objects"

    # Múltiples valores para el mismo parámetro -> usar lista
    #params = [("id", "1"), ("id", "2")]  ====> primera forma
    params = {"id": "1,2"}   # =======> segunda forma

    response = requests.get(list_url, params=params)
    data = response.json()

    # Validar que los objetos tengan ID 1 o 2
    expected_ids = ["1", "2"]
    if isinstance(data, list):
        for obj in data:
            assert obj["id"] in expected_ids
