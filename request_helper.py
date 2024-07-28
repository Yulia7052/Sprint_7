import requests

site_url = "https://qa-scooter.praktikum-services.ru/api/v1/"

def make_request(api, payload, query = ""):
    return requests.post(f'{site_url}{api}{query}', data = payload)

def make_request_login(payload):
    return make_request(f'courier/login', payload)

def make_request_courier(payload):
    return make_request(f'courier', payload)

def make_request_orders(payload, query = ""):
    return make_request(f'orders', payload, query)

def get_orders(query = ""):
    return requests.get(f'{site_url}orders{query}')

def get_metro_station_number(station):
    return requests.get(f'{site_url}stations/search?s={station}').json()["number"]