from requests import get, post, delete, put

way = 'http://127.0.0.1:5000'


bites = get(f'{way}/api/v2/db').json()
with open('db/mars_explorer.sqlite2', 'wb') as file:
    file.write(bytes(bites['db']))

