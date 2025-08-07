
import requests

from VariableGlobal import URI_BASE_OBJECTS


def test_filter_objects_by_id_range_local():
    url = URI_BASE_OBJECTS + "/objects"
    ini = 3
    limit = 7

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()

    filtered = []
    for obj in data:
        obj_id = int(obj["id"])
        if ini <= obj_id <= limit:
            filtered.append(obj)

    # Validar que los IDs están dentro del rango esperado
    for obj in filtered:
        assert ini <= int(obj["id"]) <= limit

    print(f"Objetos encontrados en rango {ini}-{limit}: {len(filtered)}")
