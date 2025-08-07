#Solicitud mal formada o con datos invalidos

import pytest
#Titulo : Verificar que el sistema no permite añadir un aeropuerto cuando
#         el cuerpo de la solicitud está mal formulado
import requests

from VariableGlobal import URI_BASE_AIRPORT

@pytest.mark.smoke
def test_002_Obtener_error_400():

 # Ambiente : Se pone Solo la URL
 url = URI_BASE_AIRPORT

 # Pasos
 # 1.Selecionar POST
 # 2.Llamar el recurso aeropuertos
 # Se concatena la URL con los recursos
 list_url = url + "/favorites"

 # 3.Click en el boton Send


 payload = "\r\n{ \"airport_id\": \"KIX }"
 headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer qPn5WXRKC8cvnWkiZ4vfwghR'
 }
 response = requests.post( list_url, headers=headers, data=payload)

#4.Verificar que el estado correcto sea 200
 assert response.status_code == 400

#Prioridad : Media