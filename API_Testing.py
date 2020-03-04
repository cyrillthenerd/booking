 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol': 'ICX'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'fb8af417-854e-4872-8977-4efccf57a135',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
  resp_dict = json.loads(resp_str)

  f = open("ICX_Price.txt", "a+", encoding="utf8")
  f.writelines(str(data))
  f.close()
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


