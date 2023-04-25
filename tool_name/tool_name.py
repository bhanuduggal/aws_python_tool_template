import requests

def sample(event, context):
    url = 'https://data.nationalgrideso.com/backend/datastore/dump/6fd8e042-be27-4c67-ad59-5acdd2a7b0fd'
    response = requests.get(url)
    print('Response returned by API: ', response.status_code)

if __name__ == "__main__":
    sample(None, None)