import requests

from VariableGlobal import URI_BASE_OBJECTS

def test_method_get_Key_headers():
   list_url = URI_BASE_OBJECTS + "/objects"
   response = requests.get(list_url)
   my_headers = response.headers

   assert "Content-Type" in my_headers


def test_metod_get_Value_headers():
   list_url = URI_BASE_OBJECTS + "/objects"
   response = requests.get(list_url)
   key_headers = response.headers
   value_headers = key_headers["content-type"]
   assert value_headers == "application/json"


def test_method_post_Key_headers():
   list_url = URI_BASE_OBJECTS + "/objects"
   response = requests.post(list_url, json={"id": "4"})
   my_headers = response.headers

   assert "Content-Type" in my_headers


def test_method_post_Value_headers():
   list_url = URI_BASE_OBJECTS + "/objects"
   response = requests.post(list_url, json={"id": "4"})
   key_headers = response.headers
   value_headers = key_headers["Content-Type"]
   assert value_headers == "application/json"



def test_method_put_Key_headers():
   list_url = URI_BASE_OBJECTS + "/objects"
   response = requests.put(list_url, json={"id": "2"})
   my_headers = response.headers
   assert "Content-Type" in my_headers


def test_method_put_Value_headers():
 list_url = URI_BASE_OBJECTS + "/objects"
 response = requests.post(list_url, json={"id": "1"})
 key_headers = response.headers
 value_headers = key_headers["Content-Type"]
 assert value_headers == "application/json"


def test_method_delete_Key_headers():
 list_url = URI_BASE_OBJECTS + "/objects-4554"
 response = requests.delete(list_url)
 my_headers = response.headers
 assert "Content-Type" in my_headers

def test_method_delete_Value_headers():
  list_url = URI_BASE_OBJECTS + "/objects"
  response = requests.delete(list_url)
  key_headers = response.headers
  value_headers = key_headers["Content-Type"]
  assert value_headers == "application/json"


