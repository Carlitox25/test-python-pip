import requests

def getCategories ():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()

    for aux in categories:
        print(aux['name'])