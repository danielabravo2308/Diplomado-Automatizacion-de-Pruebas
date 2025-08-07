import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

payload = {}
headers = {
  'Cookie': 'incap_ses_1721_1662004=1C0UbT+ykDhlDH3fvjjiF6VagWgAAAAATn7CU3OKcSfLb8vfD3E8DQ==; visid_incap_1662004=f2Pju49zQaOSoDbOmDGPaBsjgGgAAAAAQUIPAAAAAABxnaxSwWziRiybBTg7y94t'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
