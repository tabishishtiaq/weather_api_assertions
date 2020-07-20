import requests


Api_Key = "c73e48a7ec5a89f57f52c48a792e7064"
zip = 10001
country_code = "US"


response = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units=metric".format(zip,country_code,Api_Key))

print("response.status_code:")
print("\t" + str(response.status_code))
expected_status_code = 200
assert expected_status_code == response.status_code
assert "200" in str(response.status_code)


print("response.request:")
print("\t" + str(response.request))
expected_request = "<PreparedRequest [GET]>"
assert expected_request == str(response.request)
assert "[GET]" in str(response.request)

print("response.text:")
print("\t" + str(response.text))
expected_text = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":289.21,"feels_like":285.21,"temp_min":288.15,"temp_max":290.93,"pressure":1023,"humidity":42},"visibility":10000,"wind":{"speed":3.6,"deg":300},"clouds":{"all":0},"dt":1594072361,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1594007503,"sunset":1594066713},"timezone":3600,"id":2643743,"name":"London","cod":200}
assert 'coord' in str(response.text)
assert 'lon' in str(response.text)
assert 'lat' in str(response.text)
assert 'weather' in str(response.text)
assert 'id' in str(response.text)
assert 'main' in str(response.text)
assert 'description' in str(response.text)
assert 'icon' in str(response.text)
assert 'base' in str(response.text)
assert 'main' in str(response.text)
assert 'temp' in str(response.text)
assert 'feels_like' in str(response.text)
assert 'temp_min' in str(response.text)
assert 'temp_max' in str(response.text)
assert 'pressure' in str(response.text)
assert 'humidity' in str(response.text)
assert 'visibility' in str(response.text)
assert 'wind' in str(response.text)
assert 'speed' in str(response.text)
assert 'deg' in str(response.text)
assert 'clouds' in str(response.text)
assert 'all' in str(response.text)
assert 'dt' in str(response.text)
assert 'sys' in str(response.text)
assert 'type' in str(response.text)
assert 'id' in str(response.text)
assert 'country' in str(response.text)
assert 'sunrise' in str(response.text)
assert 'sunset' in str(response.text)
assert 'timezone' in str(response.text)
assert 'id' in str(response.text)
assert 'name' in str(response.text)
assert 'cod' in str(response.text)

print("response.headers:")
print("\t" + str(response.headers))
expected_headers = {'Server': 'openresty', 'Date': 'Mon, 06 Jul 2020 21:59:22 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '462', 'Connection': 'keep-alive', 'X-Cache-Key': '/data/2.5/weather?q=london', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Methods': 'GET, POST'}
assert 'Server' in response.headers
assert 'Date' in response.headers
assert 'Content-Type' in response.headers
assert 'Content-Length' in response.headers
assert 'Connection'   in response.headers
assert 'X-Cache-Key'  in response.headers
assert 'Access-Control-Allow-Origin' in response.headers
assert 'Access-Control-Allow-Credentials' in response.headers
assert 'Access-Control-Allow-Methods' in response.headers

print("response.content:")
print("\t" + str(response.content))
expected_content = b'{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":290.6,"feels_like":287.43,"temp_min":289.26,"temp_max":292.04,"pressure":1021,"humidity":51},"visibility":10000,"wind":{"speed":3.6,"deg":250},"clouds":{"all":2},"dt":1594109707,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1594093958,"sunset":1594153077},"timezone":3600,"id":2643743,"name":"London","cod":200}'

assert 'coord' in str(response.content)
assert 'lon' in str(response.content)
assert 'lat' in str(response.content)
assert 'weather' in str(response.content)
assert 'id' in str(response.content)
assert 'main' in str(response.content)
assert 'description' in str(response.content)
assert 'icon' in str(response.content)
assert 'base' in str(response.content)
assert 'main' in str(response.content)
assert 'temp' in str(response.content)
assert 'feels_like' in str(response.content)
assert 'temp_min' in str(response.content)
assert 'temp_max' in str(response.content)
assert 'pressure' in str(response.content)
assert 'humidity' in str(response.content)
assert 'visibility' in str(response.content)
assert 'wind' in str(response.content)
assert 'speed' in str(response.content)
assert 'deg' in str(response.content)
assert 'clouds' in str(response.content)
assert 'all' in str(response.content)
assert 'dt' in str(response.content)
assert 'sys' in str(response.content)
assert 'type' in str(response.content)
assert 'id' in str(response.content)
assert 'country' in str(response.content)
assert 'sunrise' in str(response.content)
assert 'sunset' in str(response.content)
assert 'timezone' in str(response.content)
assert 'id' in str(response.content)
assert 'name' in str(response.content)
assert 'cod' in str(response.content)


print("response.url:")
print("\t" + str(response.url))
expected_url = 'https://api.openweathermap.org/data/2.5/weather?zip=10001,US&appid=c73e48a7ec5a89f57f52c48a792e7064&units=metric'
assert "10001" in response.url
assert "US" in response.url
assert "c73e48a7ec5a89f57f52c48a792e7064"
assert "https" in response.url

print("response.cookies:")
print("\t" + str(response.cookies))
expected_cookies = "<RequestsCookieJar[]>"
assert "[]" in str(response.cookies)


print("response.encoding:")
print("\t" + str(response.encoding))
expected_encoding = "utf-8"
assert "utf-8" in response.encoding

print("response.apparent_encoding:")
print("\t" + str(response.apparent_encoding))
expected_apparent_encoding = "ascii"
assert "ascii" in response.apparent_encoding

print("response.elapsed:")
print("\t" + str(response.elapsed))
assert response.elapsed == response.elapsed

print("response.history:")
print("\t" + str(response.history))
expected_history = []
assert expected_history  == response.history
assert "[]" in str(response.history)

print("response.is_permanent_redirect:")
print("\t" + str(response.is_permanent_redirect))
expected_permanent_redirect = False
assert expected_permanent_redirect == response.is_permanent_redirect
assert "False" in str(response.is_permanent_redirect)

print("response.is_redirect:")
print("\t" + str(response.is_redirect))
expected_response_is_redirect = False
assert expected_response_is_redirect == response.is_redirect
assert "False" in str(response.is_redirect)

print("response.reason:")
print("\t" + str(response.reason))
expected_reason = "OK"
assert expected_reason in response.reason
assert "OK" in str(response.reason)

print("response.json:")
print("\t" + str(response.json()))
Expected_Response = {'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 292.41, 'feels_like': 287.93, 'temp_min': 290.93, 'temp_max': 293.71, 'pressure': 1021, 'humidity': 42}, 'visibility': 10000, 'wind': {'speed': 5.1, 'deg': 290}, 'clouds': {'all': 0}, 'dt': 1594063030, 'sys': {'type': 1, 'id': 1414, 'country': 'GB', 'sunrise': 1594007503, 'sunset': 1594066713}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
assert 'coord' in response.json()
assert 'lon' in response.json()['coord']
assert 'lat' in response.json()['coord']
assert 'weather' in response.json()
assert 'id' in response.json()['weather'][0]
assert 'main' in response.json()['weather'][0]
assert 'description' in response.json()['weather'][0]
assert 'icon' in response.json()['weather'][0]
assert 'base' in response.json()
assert 'main' in response.json()
assert 'temp' in response.json()['main']
assert 'feels_like' in response.json()['main']
assert 'temp_min' in response.json()['main']
assert 'temp_max' in response.json()['main']
assert 'pressure' in response.json()['main']
assert 'humidity' in response.json()['main']
assert 'visibility' in response.json()
assert 'wind' in response.json()
assert 'speed' in response.json()['wind']
assert 'deg' in response.json()['wind']
assert 'clouds' in response.json()
assert 'all' in response.json()['clouds']
assert 'dt' in response.json()
assert 'sys' in response.json()
assert 'type' in response.json()['sys']
assert 'id' in response.json()['sys']
assert 'country' in response.json()['sys']
assert 'sunrise' in response.json()['sys']
assert 'sunset' in response.json()['sys']
assert 'timezone' in response.json()
assert 'id' in response.json()
assert 'name' in response.json()
assert 'cod' in response.json()

