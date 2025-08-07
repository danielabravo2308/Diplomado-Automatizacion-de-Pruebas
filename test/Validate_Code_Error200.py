

""" STATUS CODE """

import pytest
import requests

from VariableGlobal import URI_BASE_AIRPORT


#Titulo : obtener lista de aeropuertos
@pytest.mark.smoke
def test_001_Obtener_la_lista_de_aeropuertos():
# El usuario debe obtener los datos de estado de cada aeropuerto como los atributos

# Ambiente : Se pone sola la URL
  url = URI_BASE_AIRPORT

#Pasos
#1.Selecionar GET

#2.Llamar el recurso aeropuertos
#Se concatena la URL con los rescursos
  list_url = url + "/airports"

#3.Click en el boton Send

  response = requests.get(list_url)
#4.Verificar que el estado correcto sea 200
  assert response.status_code == 200

#Resultado Esperado
#Verificar la respuesta sea un arreglode objetos

#Prioridad : Media
