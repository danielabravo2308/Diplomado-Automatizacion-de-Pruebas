import pytest
import requests

from VariableGlobal import URI_BASE_AIRPORT

# Categoria
@pytest.mark.functional_negative
def test_002_Obtener_airport_by_Id_NotExists_code_404():
    # Titulo
    # El usuario debe obtener un error 404 al no ingresar un Id de un aeropuerto no existente

    # Ambiente
    url = URI_BASE_AIRPORT

    # Pasos
    # 1.Selecionar GET
    # 2.Llamar el recurso aeropuertos con Id del aeropuerto no existente
    list_url = url + "/airports/MLQ1"
    # 3.Click en el boton Send

    response = requests.get(list_url)

    # 4.Verificar que el estado sea incorrecto sea 404
    assert response.status_code == 404

""" 
  Resultado Esperado

{
    "errors": [
        {
            "status": "404",
            "title": "Not Found",
            "detail": "The page you requested could not be found"
        }
    ]
}
"""

# Prioridad : Media
