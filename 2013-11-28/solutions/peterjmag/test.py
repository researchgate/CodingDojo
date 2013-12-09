import requests
from random import *


def random_data(length):
    data = ''
    while len(data) < length:
        data += str(randint(0, 1))

    return data


url = 'http://192.168.178.134:8080'
# url = 'http://localhost:8080'
delay = 50
data = []

for x in range(1, 10):
    data.append(str(delay) + '-' + random_data(16))

data = '\n'.join(data)
print data

r = requests.post(url, data)
print r.status_code, r.text
