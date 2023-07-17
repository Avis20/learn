
from urllib.parse import urlunsplit


url = 'https://hello.ru'
# params = {'test': 1}
print(urlunsplit((url, f'test=1')))
