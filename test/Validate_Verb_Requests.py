
"""  Validando Verb Request y Status Code: asegurarse que el endpoint acepte y responda correctamente
                         a un metodo especifico """

import requests

from VariableGlobal import URI_BASE_OBJECTS

def test_post_metodo_exitoso_crea_el_objeto():
    list_url = URI_BASE_OBJECTS + "/objects"
    response = requests.post(list_url,json={"name":"Apple Mac16" ,
                                                    "data":{"year":2025,
                                                            "price": 2013,
                                                            "CPU model":"Intel",
                                                            "Hard disk size":"1TB",
                                                            "color":"silver"
                                                            }})
    assert response.status_code == 200 # Resultado Actual 200


"""
    Es muy comun y correcto que un endpoint como https://api.restful-api.dev/objects
    maneje diferentes verbos en este caso retorna un codigo 200 usando el metodo GET y POST
    Y no se consideraria un BUG segun su documentacion se observo que tiene 2 funcionalidades
    sino dice en la documentacion es BUG  
"""
def test_get_metodo_exitoso_obtiene_lista_de_objetos():
    list_url = URI_BASE_OBJECTS + "/objects"
    response = requests.get(list_url)
    assert response.status_code == 200    # Resultado Actual code 200



def test_put_metodo_no_permitido():
    list_url = URI_BASE_OBJECTS + "/objects"
    response = requests.put(list_url,json={"name":"Apple Mac17" ,})
    assert response.status_code == 405  # Resultado Actual 405


def test_delete_metodo_no_permitido():
    list_url = URI_BASE_OBJECTS + "/objects"
    response = requests.delete(list_url)
    assert response.status_code == 405   #Resultado Actual 405