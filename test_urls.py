import requests
import configuration
# Prueba endpoints alternativos
test_urls = [
    "/api/v1/users/",
    "/api/db/users/",
    "/api/users/",
    "/api/v1/users/table/",
    "/api/db/table/"
]

for url in test_urls:
    response = requests.get(configuration.URL_SERVICE + url)
    print(f"URL: {url} - Código: {response.status_code}")