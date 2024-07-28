import random

logins = [
    "master",
    "minikuper",
    "fate",
    "bob"
]
firstNames = [
    "Oleg",
    "Dima",
    "Misha",
    "Vadim"
]

def generate_courier():
    return {
        "login": logins[random.randint(0, len(logins) - 1)] + str(random.randint(0, 9999999)),
        "firstName": firstNames[random.randint(0, len(firstNames) - 1)],
        "password": random.randint(1000, 9999),
    }

def generate_order(colors):
    name = firstNames[random.randint(0, len(firstNames) - 1)]
    return {
        "firstName": name,
        "lastName": name,
        "address": "city city, street street, building, 123",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "No comments",
        "color": colors
    }
