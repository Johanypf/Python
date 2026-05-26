import requests


def get_categories():
    response = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(f"Status Code: {response.status_code}")
    print(f"{response.text}")
    print("-----------------------------")
    categorias = response.json()
    print(categorias)
    for categoria in categorias:
        print(categoria["name"])


    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
