import requests
from bs4 import BeautifulSoup


def get_prices_from_armella():
    data = {
        'customer': 'crmturizm',
        'downPayment': '0',
        'hotel_id': '124',
        'widget_id': '160',
        'access_token': 'TzdlZWh2N2ZqM05vZEJhd2pMQ0FrTVZBNWRYcnpJWU5yeDlHL3lyUWY0NXptOXFHaTJ0bGZQaUFNRHptWEpEVi9tTFNqNzJ5M0tvTFVvc2h3T0FsSTVGdWEvV1hMYVR5M1ZCU2l0NDY2OXh0VS8xaXRlSWQ5THFKYmQxZEgxVDl5SGZOZ2hZby96bmFReVlzbFE0bC9XTlF1aVNaRk9pTXovaE1sb21FcU1VR1EyTU8xNjNEYlpGVHZ3dVFUR01h',
        'checkin': '20.07.2021',
        'checkout': '25.07.2021',
        'adult': '2',
        'child': '',
        'child1': '',
        'child2': '',
        'child3': '',
        'child4': ''
    }

    response = requests.post('https://www.armellahotels.com/rezervasyon', data=data).content

    soup = BeautifulSoup(response, features="lxml")

    rooms = soup.body.find_all('div', attrs={'class': 'room_price'})

    prices = [room.findChildren("span", recursive=False)[0].text for room in rooms]

    return prices

def get_prices_from_glamour():
    data = {
    'config[customer]': 'webres',
    'config[hotel_id]': '1',
    'config[widget_id]': '1',
    'config[access_token]': 'c1UxeDhoV2ZNNHpBbTFwZDBYVmFZaHF1YkFOSTdNVkhBaFJydHlJUlA2R20yZFczVXNkMlRsL1B2YVNuNWd1aGszREhud2pHSlZnamFDTjM0NDhsRjk4dFlkL09nQnRVVFh2VGkyWkZ0NmVtMHdCZ0dnRW1lQ1Zwcm1LTkYzQmMwK0tHM0dJdGhOWGpncWoxc3ZsdzFVS3M4VEQwdllKcEdTekNnUEhTZEFrWmlNNHI0TjVSVDRYcTlmWUhWVytU',
    'config[booking_step]': '1',
    'config[kaporaKontrol]': '',
    'checkin': '20/07/2021',
    'checkout': '25/07/2021',
    'adult': '2',
    'child': '0',
    'child1': '',
    'child2': '',
    'child3': '',
    'child4': ''
    }

    response = requests.post('http://app2.travelus.pro/booking/v2/', data=data, verify=False).content

    soup = BeautifulSoup(response, features="lxml")

    rooms = soup.body.find_all('div', attrs={'class': 'room_price'})

    prices = [room.findChildren("span", recursive=False)[0].text for room in rooms]

    return prices
