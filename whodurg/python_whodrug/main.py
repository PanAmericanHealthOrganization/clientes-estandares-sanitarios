import json
import requests
import datetime

# Credenciales whodrug
umc_client_key = 'umc_client_key'
umc_license_key = 'umc_license_key'

# request
'''
    IncludeAtc: true | false
    MedProdLevel: 1 | 2 | 3
    IngredientTranslations = es-ES | en-US
'''
parametros = ""
api_url = "https://api.who-umc.org/whodrug/download/v2/regional-drugs?MedProdLevel=2&IncludeAtc=true&IngredientTranslations=es-ES"


def save_json_to_file(json_data, filename):
    '''
    Genera una archivo a partir del json_data
    @param json_data: json, dict contenido del archivo
    @param filename: str. nombre del archivo, ej. 'regional_drugs.json'
    '''
    with open(filename, 'w') as file:
        json.dump(json_data, file)


def fetch_json_from_api(url):
    '''
    Realiza una peticion a la API de WHO-UMC y retorna el contenido en formato JSON
    @param url: str. URL de la API
    '''
    try:
        headers = {
            'umc-client-key': umc_client_key,
            'umc-license-key': umc_license_key
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":

    json_data = fetch_json_from_api(api_url)

    if json_data:
        today = datetime.datetime.now().strftime("%Y_%m_%d")
        save_json_to_file(json_data, f"{today}_whodrug.json")
