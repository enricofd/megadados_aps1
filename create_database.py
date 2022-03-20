import requests


def make_product(name, description, price):
    return {"name": name, "description": description, "price": price}


products = [
    make_product("Batata", "Batata usada para cozinhar", 3.75),
    make_product("Beterraba", "Beterraba utilizada para salada", 2.99),
    make_product("Cenoura", "Cenoura para vitaminas", 1.99),
]


class Requests:
    baseurl = 'http://localhost:8000'

    @staticmethod
    def post(endpoint, data):
        response = requests.post(Requests.baseurl + endpoint, json=data)
        return response


def create_products():
    for product in products:
        print(product)
        Requests.post('/product', product)


if __name__ == "__main__":
    create_products()
