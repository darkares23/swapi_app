import requests

SWAPI_GRAPHQL_ENDPOINT = 'https://swapi-graphql.netlify.app/.netlify/functions/index'

def fetch_all_planets():
    try:
        query = """
        {
        allPlanets {
            planets {
            name
            population
            terrains
            climates
            }
        }
        }
        """
        response = requests.post(SWAPI_GRAPHQL_ENDPOINT, json={'query': query})
        if response.status_code == 200:
            planets_data = response.json()['data']['allPlanets']['planets']
            return planets_data
        else:
            print(f"Request failed with status code: {response.status_code}")
            return []
    except Exception as e:
        print("Error fetching planets:", e)
        return []
