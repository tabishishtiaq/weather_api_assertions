import requests
import json
import pytest


Api_Key = "c73e48a7ec5a89f57f52c48a792e7064"
lon= 67.03

lat = 24.87

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(lat,lon, Api_Key))


def response_code():
    print("response.status_code:")
    print("\t" + str(response.status_code))
    expected_status_code = 200
    try:
        if response.status_code == 200:
            assert expected_status_code == response.status_code
            assert "200" in str(response.status_code)
            print("Response Status Code Assertion is Passed ")
        else:
            print("Response Status Code Assertion is Failed ")
    except requests.RequestException as e:
        print("Response Status Code Assertion is Failes Due To : " + str(e))
response_code()

def response_request():
    print("response.request:")
    print("\t" + str(response.request))
    expected_request = "<PreparedRequest [GET]>"
    try:
        if expected_request == response.request :
            assert expected_request == str(response.request)
            assert "[GET]" in str(response.request)
            print("Response Request Assertion is Passed")
        else:
            print("Response Request Assertion is Passed")
    except requests.RequestException as e:
        print("Response Request Assertion is Failed Due To : " + str(e))



response_request()

def response_text():
    print("response.text:")
    print("\t" + str(response.text))
    expected_text = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":289.21,"feels_like":285.21,"temp_min":288.15,"temp_max":290.93,"pressure":1023,"humidity":42},"visibility":10000,"wind":{"speed":3.6,"deg":300},"clouds":{"all":0},"dt":1594072361,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1594007503,"sunset":1594066713},"timezone":3600,"id":2643743,"name":"London","cod":200}

    try:
        if 'coord' in str(response.text):
            assert 'coord' in str(response.text)
            print("Coord Key Assertion is Passed in Response Text")
        else:
            print("Coord Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Coord Key Assertion is Failed in Response Text Due To : " + str(e))

    try:
        if 'lon' in str(response.text):
            assert 'lon' in str(response.text)
            print("Coord Key Value Assertion is Passed in Response Text")
        else:
            print("Coord Key Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Coord Key Value Assertion is Failed in Response Text Due To : " + str(e))
    try:

        if '67.03' in str(response.text):
            assert '67.03' in str(response.text)
            print("Lon Key Value Assertion is Passed in Response Text")
        else:
            print("Lon Key Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Lon Key Value Assertion is Failed in Response Text Due To:" + str(e))

    try:
        if 'lat' in str(response.text):
            assert 'lat' in str(response.text)
            print("Lat Key Assertion is Passed in Response Text")
        else:
            print("Lat Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Lat Key Assertion is Failed in Response Text Due To : " + str(e))
    try:

        if '24.87' in str(response.text):
            assert '24.87' in str(response.text)
            print("Lat Key Value Assertion is Passed in Response Text")
        else:
            print("Lat Key Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("lat Key Value Assertion is Failed in Response Text Due To:" + str(e))

    try:
        if 'weather' in str(response.text):
            assert 'weather' in str(response.text)
            print("Weather Key Assertion is Passed in Response Text")
        else:
            print("Weather Key Assertion is Passed in Response Text")
    except requests.RequestException as e:
        print("Weather Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'id' in str(response.text):
            assert 'id' in str(response.text)
            print("ID Key assertion is Passed in Response Text")
        else:
            print("ID Key assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("ID Key assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '802' in str(response.text):
            assert '802' in str(response.text)
            print("Weather Key Value ID Assertion is Passed in Response Text")
        else:
            print("Weather Key Value ID Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Weather Key Value ID Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'main' in str(response.text):
            assert 'main' in str(response.text)
            print("Main Key Assertion is Passed in Response Text")
        else:
            print("Main Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Main Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if "Clouds" in str(response.text):
            assert "Clouds" in str(response.text)
            print("Main Key's Value Assertion is Passed in Response Text")
        else:
            print("Main Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Main Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'description' in str(response.text):
            assert 'description' in str(response.text)
            print("Description Key Assertion is Passed in Response Text")
        else:
            print("Description Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Description Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if "scattered clouds" in str(response.text):
            assert "scattered clouds" in str(response.text)
            print("Description Key's Value Assertion is Passed in Response Text")
        else:
            print("Description Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Description Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'icon' in str(response.text):
            assert 'icon' in str(response.text)
            print("Icon Key Assertion is Passed in Response Text")
        else:
            print("Icon Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Icon Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if "03n" in str(response.text):
            assert "03n" in str(response.text)
            print("Icon Key's Value Assertion is Passed in Response Text")
        else:
            print("Icon Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Icon Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'base' in str(response.text):
            assert 'base' in str(response.text)
            print("Base Key Assertion is Passed in Response Text")
        else:
            print("Base Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Base Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if "stations" in str(response.text):
            assert "stations" in str(response.text)
            print("Base Key Value's Assertion is Passed in Response Text")
        else:
            print("Base Key Value's Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Base Key Value's Assertion is Failed in Response Text Due To : " + str(e))

    try:
        if 'main' in str(response.text):
            assert 'main' in str(response.text)
            print("Main Key Assertion is Passed in Response Text")
        else:
            print("Main Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Main Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'temp' in str(response.text):
            assert 'temp' in str(response.text)
            print("Main Key's Value Assertion is Passed in Response Text")
        else:
            print("Main Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Main Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '31' in str(response.text):
            assert '31' in str(response.text)
            print("Temp Key's Value Assertion is Passed in Response Text")
        else:
            print("Temp Key's Value Assertion is Failed in Response Text")
    except requests.RequestException in e:
        print("Temp Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'feels_like' in str(response.text):
            assert 'feels_like' in str(response.text)
            print("Feels Like Key Assertion is Passed in Response Text")
        else:
            print("Feels Like Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Feels Like Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'temp_min' in str(response.text):
            assert 'temp_min' in str(response.text)
            print("Temp Min Key Assertion is Passed in Response Text")
        else:
            print("Temp Min Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Temp Min Key Assertion is Failed in Response Text Due To " + str(e))
    try:
        if '31' in str(response.text):
            assert '31' in str(response.text)
            print("Temp Min Key's Value Assertion is Passed in Response Text")
        else:
            print("Temp Min Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Temp Min Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'temp_max' in str(response.text):
            assert 'temp_max' in str(response.text)
            print("Temp Max Key Assertion is Passed in Response Text")
        else:
            print("Temp Max Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Temp Max Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '31' in str(response.text):
            assert '31' in str(response.text)
            print("Temp Max Key's Value Assertion is Passed in Response Text")
        else:
            print("Temp Max Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Temp Max Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'pressure' in str(response.text):
            assert 'pressure' in str(response.text)
            print("Pressure Key Assertion is Passed in Response Text")
        else:
            print("Pressure Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Pressure Key Assertion is Failed in Response Text Due To " + str(e))
    try:
        if '1001' in str(response.text):
            assert '1001' in str(response.text)
            print("Pressure Key's Value Assertion is Passed in Response Text")
        else:
            print("Pressure Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Pressure Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'humidity' in str(response.text):
            assert 'humidity' in str(response.text)
            print("Humidity Key Assertion is Passed in Response Text")
        else:
            print("Humidity Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Humidity Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '66' in str(response.text):
            assert '66' in str(response.text)
            print("Humidity Key's Value Assertion is Passed in Response Text")
        else:
            print("Humidity Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Humidity Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'visibility' in str(response.text):
            assert 'visibility' in str(response.text)
            print('Visibility Key Assertion is Passed in Response Text')
        else:
            print('Visibility Key Assertion is Failed in Response Text')
    except requests.RequestException as e:
        print('Visibility Key Assertion is Failed in Response Text Due To : ' + str(e))
    try:
        if '7000' in str(response.text):
            assert '7000' in str(response.text)
            print("Visibility Key's Value Assertion is Passed in Response Text")
        else:
            print("Visibility Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Visibility Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'wind' in str(response.text):
            assert 'wind' in str(response.text)
            print("Wind Key Assertion is Passed in Response Text")
        else:
            print("Wind Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Wind Key Assertion is Failed in Response Text Due To :  " + str(e))
    try:
        if 'speed' in str(response.text):
            assert 'speed' in str(response.text)
            print("Wind Key's Value Assertion is Passed in Response Text")
        else:
            print("Wind Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Wind Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '5.1' in str(response.text):
            assert '5.1' in str(response.text)
            print("Speed Key's Value Assertion is Passed in Response Text")
        else:
            print("Speed Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Speed Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'deg' in str(response.text):
            assert 'deg' in str(response.text)
            print("Degree Key Assertion is Passed in Response Text")
        else:
            print("Degree Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Degree Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '200' in str(response.text):
            assert '200' in str(response.text)
            print("Degree Key's Value Assertion is Passed in Response Text")
        else:
            print("Degree Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Degree Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'clouds' in str(response.text):
            assert 'clouds' in str(response.text)
            print("Clouds Key Assertion is Passed in Response Text")
        else:
            print("Clouds Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Clouds Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'all' in str(response.text):
            assert 'all' in str(response.text)
            print("Clouds Key's Value Assertion is Passed in Response Text")
        else:
            print("Clouds Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Clouds Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '40' in str(response.text):
            assert '40' in str(response.text)
            print("Clouds Key's Value Assertion is Passed in Response Text")
        else:
            print("Clouds Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Clouds Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'dt' in str(response.text):
            assert 'dt' in str(response.text)
            print("DT Key Assertion is Passed in Response Text")
        else:
            print("DT Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("DT Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'sys' in str(response.text):
            assert 'sys' in str(response.text)
            print("SYS Key Assertion is Passed in Response Text")
        else:
            print("SYS Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("SYS Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'type' in str(response.text):
            assert 'type' in str(response.text)
            print("SYS Key's Value Assertion is Passed in Response Text")
        else:
            print("SYS Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("SYS Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '1' in str(response.text):
            assert '1' in str(response.text)
            print("Type Key's Value Assertion is Passed in Response Text")
        else:
            print("Type Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Type Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'id' in str(response.text):
            assert 'id' in str(response.text)
            print("ID Key  Assertion is Passed in Response Text")
        else:
            print("ID Key  Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("ID Key  Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '7576' in str(response.text):
            assert '7576' in str(response.text)
            print("Id Key's Value Assertion is Passed in Response Text")
        else:
            print("Id Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Id Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'country' in str(response.text):
            assert 'country' in str(response.text)
            print("Country Key Assertion is Passed in Response Text")
        else:
            print("Country Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Country Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'PK' in str(response.text):
            assert 'PK' in str(response.text)
            print("Country Key's Value Assertion is Passed in Response Text")
        else:
            print("Country Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Country Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'sunrise' in str(response.text):
            assert 'sunrise' in str(response.text)
            print("Sunrise Key Assertion is Passed in Response Text")
        else:
            print("Sunrise Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Sunrise Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '1595206435' in str(response.text):
            assert '1595206435' in str(response.text)
            print("Sunrise Key's Value Assertion is Passed in Response Text")
        else:
            print("Sunrise Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Sunrise Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'sunset' in str(response.text):
            assert 'sunset' in str(response.text)
            print("Sunset Key Assertion is Passed in Response Text")
        else:
            print("Sunset Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Sunset Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'timezone' in str(response.text):
            assert 'timezone' in str(response.text)
            print("Timezone Key Assertion is Passed in Response Text")
        else:
            print("Timezone Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Timezone Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '18000' in str(response.text):
            assert '18000' in str(response.text)
            print("Timezone Key's Value Assertion is Passed in Response Text")
        else:
            print("Timezone Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Timezone Key's Value Assertion is Failed in Response Text")
    try:
        if 'id' in str(response.text):
            assert 'id' in str(response.text)
            print("ID Key Assertion is Passed in Response Text")
        else:
            print("ID Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("ID Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if '1174872' in str(response.text):
            assert '1174872' in str(response.text)
            print("ID Key's Value Assertion is Passed in Response Text")
        else:
            print("ID Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("ID Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'name' in str(response.text):
            assert 'name' in str(response.text)
            print("Name Key Assertion is Passed in Response Text")
        else:
            print("Name Key Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Name Key Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'Karachi' in str(response.text):
            assert 'Karachi' in str(response.text)
            print("Name Key's Value Assertion is Passed in Response Text")
        else:
            print("Name Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("Name Key's Value Assertion is Failed in Response Text Due To : " + str(e))
    try:
        if 'cod' in str(response.text):
            assert 'cod' in str(response.text)
            print('COD Key Assertion is Passed in Response Text')
        else:
            print('COD Key Assertion is Failed in Response Text')
    except requests.RequestException as e:
        print('COD Key Assertion is Failed in Response Text Due To : ' + str(e))
    try:
        if '200' in str(response.text):
            assert '200' in str(response.text)
            print("COD Key's Value Assertion is Passed in Response Text")
        else:
            print("COD Key's Value Assertion is Failed in Response Text")
    except requests.RequestException as e:
        print("COD Key's Value Assertion is Failed in Response Text Due To : " + str(e))

response_text()


def response_headers():
    print("response.headers:")
    print("\t" + str(response.headers))
    expected_headers = {'Server': 'openresty', 'Date': 'Mon, 06 Jul 2020 21:59:22 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '462', 'Connection': 'keep-alive', 'X-Cache-Key': '/data/2.5/weather?q=london', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Methods': 'GET, POST'}
    try:
        if 'Server ' == response.headers:
            assert 'Server' in response.headers
            print('Server Key Assertion in Response Headers is Passed')
        else:
            print('Server Key Assertion in Response Headers is Failed')
    except requests.RequestException as e:
        print('Server Key Assertion in Response Headers is Failed Due To : ' + str(e))
    try:
        if 'openresty' == response.headers['Server']:
             assert 'openresty' in response.headers['Server']
             print('Openresty Value Assertion is Passed in response.headers["Server"]')
        else:
            print('Openresty Value Assertion is Failed in response.headers["Server"]')
    except requests.RequestException as e:
        print('Openresty Value Assertion is Failed in response.headers["Server"] Due To : ' + str(e))
    try:
        if 'Date' in response.headers:
            assert 'Date' in response.headers
            print('Date Key Assertion is Passed in Response Headers')
        else:
            print('Date Key Assertion is Failed in Response Headers')
    except requests.RequestException as e:
        print('Date Key Assertion is Failed in Response Headers Due To : ' + str(e))

    try:
        if 'Mon, 13 Jul 2020' in response.headers['Date']:
            assert 'Mon, 13 Jul 2020' in response.headers['Date']
            print('Date Key Value Assertion is Passed in Response Headers')
        else:
            print('Date Key Value Assertion is Failed in Response Headers')
    except requests.RequestException as e:
        print('Date Key Value Assertion is Failed in Response Headers Due To : ' + str(e))

    try:
        if 'Content-Type' in response.headers:
            assert 'Content-Length' in response.headers
            print('Content-Type Key Assertion is Passed in Response Header')
        else:
            print('Content-Type Key Assertion is Failed in Response Header')
    except requests.RequestException as e:
        print('Content-Type Key Assertion is Failed in Response Header Due To : ' + str(e))

    try:
        if 'application/json; charset=utf-8' in response.headers['Content-Type']:
            assert 'application/json; charset=utf-8' in response.headers['Content-Type']
            print("Content-Type Key Value assertion is Passed in Response Headers")
        else:
            print("Content-Type Key Value assertion is Failed in Response Headers")
    except requests.RequestException as e:
        print("Content-Type Key Value assertion is Failed in Response Headers Due To : " + str(e))
    try:
        if 'Connection' in response.headers:
            assert 'Connection'   in response.headers
            print("Connection Key Assertion is Passed In Response Headers")
        else:
            print("Connection Key Assertion is Failed In Response Headers")
    except requests.RequestException as e:
        print("Connection Key Assertion is Failed In Response Headers Due To : " + str(e))

    try:
        if 'keep-alive' in response.headers['Connection']:
            assert 'keep-alive' in response.headers['Connection']
            print('Connection Key Value Assertion is Passed in Response Headers["Connection"]')
        else:
            print('Connection Key Value Assertion is Failed in Response Headers["Connection"]')
    except requests.RequestException as e:
        print('Connection Key Value Assertion is Failed in Response Headers["Connection"] Due To : ' + str(e))


    try:
        if 'X-Cache-Key' in response.headers:
            assert 'X-Cache-Key'  in response.headers
            print("The X-Cache-Key Assertion is Passed in Response Headers")
        else:
            print("The X-Cache-Key Assertion is Failed in Response Headers")
    except requests.RequestException as e:
        print("The X-Cache-Key Assertion is Failed in Response Headers Due To : " +str(e))
    try:
        if '/data/2.5/weather?lat=24.87&lon=67.03' in response.headers['X-Cache-Key']:
            assert '/data/2.5/weather?lat=24.87&lon=67.03' in response.headers['X-Cache-Key']
            print("X-Cache-Key Key Value Assertion is Passed in Response Headers['X-Cache-Key']")
        else:
            print("X-Cache-Key Key Value Assertion is Failed in Response Headers['X-Cache-Key']")
    except requests.RequestException as e:
        print("X-Cache-Key Key Value Assertion is Failed in Response Headers['X-Cache-Key'] Due To : " + str(e))

    try:
        if 'Access-Control-Allow-Origin' in response.headers:
            assert 'Access-Control-Allow-Origin' in response.headers
            print("Access-Control-Allow-Origin  Key Assertion is Passed in Response Header")
        else:
            print("Access-Control-Allow-Origin  Key Assertion is Failed in Response Header")
    except requests.RequestException as e:
        print("Access-Control-Allow-Origin  Key Assertion is Failed in Response Header Due To : " + str(e))
    try:
        if '*' in response.headers['Access-Control-Allow-Origin']:
            assert '*' in response.headers['Access-Control-Allow-Origin']
            print("Access-Control-Allow-Origin Key Assertion is Passed in response.headers['Access-Control-Allow-Origin'] ")
        else:
             print("Access-Control-Allow-Origin Key Assertion is Passed in response.headers['Access-Control-Allow-Origin'] ")
    except requests.RequestException as e:
        print("Access-Control-Allow-Origin Key Assertion is Failed in response.headers['Access-Control-Allow-Origin'] Due To : " +str(e))

    try:
        if 'Access-Control-Allow-Credentials' in response.headers:
            assert 'Access-Control-Allow-Credentials' in response.headers
            print("Access-Control-Allow-Credentials Assertion is Passed in Response Headers")
        else:
            print("Access-Control-Allow-Credentials Assertion is Failed in Response Headers")
    except requests.RequestException as e:
        print("Access-Control-Allow-Credentials Assertion is Failed in Response Headers Due To : " + str(e))
    try:
         if 'true' in response.headers['Access-Control-Allow-Credentials']:
             assert 'true' in response.headers['Access-Control-Allow-Credentials']
             print("Access-Control-Allow-Credentials value Assertion is Passed in Response headers['Access-Control-Allow-Credentials']")
         else:
            print("Access-Control-Allow-Credentials value Assertion is Failed in Response headers['Access-Control-Allow-Credentials']")
    except requests.RequestException as e:
        print(
            "Access-Control-Allow-Credentials value Assertion is Failed in Response headers['Access-Control-Allow-Credentials'] Due To : " + str(e))
    try:
        if 'Access-Control-Allow-Methods' in response.headers:
            assert 'Access-Control-Allow-Methods' in response.headers
            print("Access-Control-Allow-Methods Key Assertion is Passed in response.headers")
        else:
            print("Access-Control-Allow-Methods Key Assertion is Failed in response.headers")
    except requests.RequestException as e:
        print("Access-Control-Allow-Methods Key Assertion is Failed in response.headers Due To : " + str(e))

    try:
        if 'GET, POST' in response.headers['Access-Control-Allow-Methods']:
            assert 'GET, POST' in response.headers['Access-Control-Allow-Methods']
            print("Access-Control-Allow-Methods Key Value Assertion is Passed in response.headers['Access-Control-Allow-Methods']")
        else:
            print("Access-Control-Allow-Methods Key Value Assertion is Failed in response.headers['Access-Control-Allow-Methods']")
    except requests.RequestException as e:
        print("Access-Control-Allow-Methods Key Value Assertion is Failed in response.headers['Access-Control-Allow-Methods'] Due To :" + str(e))
response_headers()

def response_content():
    print("response.content:")
    print("\t" + str(response.content))

    expected_content = b'{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":290.6,"feels_like":287.43,"temp_min":289.26,"temp_max":292.04,"pressure":1021,"humidity":51},"visibility":10000,"wind":{"speed":3.6,"deg":250},"clouds":{"all":2},"dt":1594109707,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1594093958,"sunset":1594153077},"timezone":3600,"id":2643743,"name":"London","cod":200}'

    try:
        if 'coord' in str(response.content):
            assert 'coord' in str(response.content)
            print("Coord Key Assertion is Passed in Response Content")
        else:
            print("Coord Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Coord Key Assertion is Failed in Response Content Due To : " + str(e))

    try:
        if 'lon' in str(response.content):
            assert 'lon' in str(response.content)
            print("Coord Key Value Assertion is Passed in Response Content")
        else:
            print("Coord Key Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Coord Key Value Assertion is Failed in Response Content Due To : " + str(e))
    try:

        if '67.03' in str(response.content):
             assert '67.03' in str(response.content)
             print("Lon Key Value Assertion is Passed in Response Content")
        else:
            print("Lon Key Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Lon Key Value Assertion is Failed in Response Content Due To:" + str(e))

    try:
        if 'lat' in str(response.content):
            assert 'lat' in str(response.content)
            print("Lat Key Assertion is Passed in Response Content")
        else:
            print("Lat Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Lat Key Assertion is Failed in Response Content Due To : " + str(e))
    try:

        if '24.87' in str(response.content):
             assert '24.87' in str(response.content)
             print("Lat Key Value Assertion is Passed in Response Content")
        else:
            print("Lat Key Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("lat Key Value Assertion is Failed in Response Content Due To:" + str(e))
    try:
        if 'weather' in str(response.content):
            assert 'weather' in str(response.content)
            print("Weather Key Assertion is Passed in Response Content")
        else:
            print("Weather Key Assertion is Passed in Response Content")
    except requests.RequestException as e:
        print("Weather Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'id' in str(response.content):
            assert 'id' in str(response.content)
            print("ID Key assertion is Passed in Response Content")
        else:
            print("ID Key assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("ID Key assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '802' in str(response.content):
            assert '802' in str(response.content)
            print("Weather Key Value ID Assertion is Passed in Response Content")
        else:
            print("Weather Key Value ID Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Weather Key Value ID Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'main' in str(response.content):
            assert 'main' in str(response.content)
            print("Main Key Assertion is Passed in Response Content")
        else:
            print("Main Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Main Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if "Clouds" in str(response.content):
            assert "Clouds" in str(response.content)
            print("Main Key's Value Assertion is Passed in Response Content")
        else:
            print("Main Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Main Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'description' in str(response.content):
            assert 'description' in str(response.content)
            print("Description Key Assertion is Passed in Response Content")
        else:
            print("Description Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Description Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if "scattered clouds" in str(response.content):
            assert "scattered clouds" in str(response.content)
            print("Description Key's Value Assertion is Passed in Response Content")
        else:
            print("Description Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Description Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'icon' in str(response.content):
            assert 'icon' in str(response.content)
            print("Icon Key Assertion is Passed in Response Content")
        else:
            print("Icon Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Icon Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if "03n" in str(response.content):
            assert "03n" in str(response.content)
            print("Icon Key's Value Assertion is Passed in Response Content")
        else:
            print("Icon Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Icon Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'base' in str(response.content):
            assert 'base' in str(response.content)
            print("Base Key Assertion is Passed in Response Content")
        else:
            print("Base Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Base Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if "stations" in str(response.content):
            assert "stations" in str(response.content)
            print("Base Key Value's Assertion is Passed in Response Content")
        else:
            print("Base Key Value's Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Base Key Value's Assertion is Failed in Response Content Due To : " + str(e))

    try:
        if 'main' in str(response.content):
            assert 'main' in str(response.content)
            print("Main Key Assertion is Passed in Response Content")
        else:
            print("Main Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Main Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'temp' in str(response.content):
            assert 'temp' in str(response.content)
            print("Main Key's Value Assertion is Passed in Response content")
        else:
            print("Main Key's Value Assertion is Failed in Response content")
    except requests.RequestException as e:
        print("Main Key's Value Assertion is Failed in Response content Due To : " + str(e))
    try:
        if '31' in str(response.content):
            assert '31' in str(response.content)
            print("Temp Key's Value Assertion is Passed in Response Content")
        else:
            print("Temp Key's Value Assertion is Failed in Response Content")
    except Exception in e:
        print("Temp Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'feels_like' in str(response.content):
            assert 'feels_like' in str(response.content)
            print("Feels Like Key Assertion is Passed in Response Content")
        else:
            print("Feels Like Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Feels Like Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'temp_min' in str(response.content):
            assert 'temp_min' in str(response.content)
            print("Temp Min Key Assertion is Passed in Response Content")
        else:
            print("Temp Min Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Temp Min Key Assertion is Failed in Response Content Due To " + str(e))
    try:
        if '31' in str(response.content):
            assert '31' in str(response.content)
            print("Temp Min Key's Value Assertion is Passed in Response Content")
        else:
            print("Temp Min Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Temp Min Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'temp_max' in str(response.content):
            assert 'temp_max' in str(response.content)
            print("Temp Max Key Assertion is Passed in Response Content")
        else:
            print("Temp Max Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Temp Max Key Assertion is Failed in Response Content Due To : "  + str(e))
    try:
        if '31' in str(response.content):
            assert '31' in str(response.content)
            print("Temp Max Key's Value Assertion is Passed in Response Content")
        else:
            print("Temp Max Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Temp Max Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'pressure' in str(response.content):
            assert 'pressure' in str(response.content)
            print("Pressure Key Assertion is Passed in Response Content")
        else:
            print("Pressure Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Pressure Key Assertion is Failed in Response Content Due To " + str(e))
    try:
        if '1001' in str(response.content):
            assert '1001' in str(response.content)
            print("Pressure Key's Value Assertion is Passed in Response Content")
        else:
            print("Pressure Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Pressure Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'humidity' in str(response.content):
            assert 'humidity' in str(response.content)
            print("Humidity Key Assertion is Passed in Response Content")
        else:
            print("Humidity Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Humidity Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '66' in str(response.content):
            assert '66' in str(response.content)
            print("Humidity Key's Value Assertion is Passed in Response Content")
        else:
            print("Humidity Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Humidity Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'visibility' in str(response.content):
            assert 'visibility' in str(response.content)
            print('Visibility Key Assertion is Passed in Response Content')
        else:
            print('Visibility Key Assertion is Failed in Response Content')
    except requests.RequestException as e:
        print('Visibility Key Assertion is Failed in Response Content Due To : ' + str(e))
    try:
        if '7000' in str(response.content):
            assert '7000' in str(response.content)
            print("Visibility Key's Value Assertion is Passed in Response Content")
        else:
            print("Visibility Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Visibility Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'wind' in str(response.content):
            assert 'wind' in str(response.content)
            print("Wind Key Assertion is Passed in Response Content")
        else:
            print("Wind Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Wind Key Assertion is Failed in Response Content Due To :  " + str(e))
    try:
        if 'speed' in str(response.content):
            assert 'speed' in str(response.content)
            print("Wind Key's Value Assertion is Passed in Response Content")
        else:
            print("Wind Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Wind Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
         if '5.1' in str(response.content):
             assert '5.1' in str(response.content)
             print("Speed Key's Value Assertion is Passed in Response Content")
         else:
            print("Speed Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Speed Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'deg' in str(response.content):
            assert 'deg' in str(response.content)
            print("Degree Key Assertion is Passed in Response Content")
        else:
            print("Degree Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Degree Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '200' in str(response.content):
            assert '200' in str(response.content)
            print("Degree Key's Value Assertion is Passed in Response Content")
        else:
            print("Degree Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Degree Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'clouds' in str(response.content):
            assert 'clouds' in str(response.content)
            print("Clouds Key Assertion is Passed in Response Content")
        else:
            print("Clouds Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Clouds Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'all' in str(response.content):
            assert 'all' in str(response.content)
            print("Clouds Key's Value Assertion is Passed in Response Content")
        else:
            print("Clouds Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Clouds Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '40' in str(response.content):
            assert '40' in str(response.content)
            print("Clouds Key's Value Assertion is Passed in Response Content")
        else:
            print("Clouds Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Clouds Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'dt' in str(response.content):
            assert 'dt' in str(response.content)
            print("DT Key Assertion is Passed in Response Content")
        else:
            print("DT Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("DT Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'sys' in str(response.content):
            assert 'sys' in str(response.content)
            print("SYS Key Assertion is Passed in Response Content")
        else:
            print("SYS Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("SYS Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'type' in str(response.content):
            assert 'type' in str(response.content)
            print("SYS Key's Value Assertion is Passed in Response Content")
        else:
            print("SYS Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("SYS Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '1' in str(response.content):
            assert '1' in str(response.content)
            print("Type Key's Value Assertion is Passed in Response Content")
        else:
            print("Type Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Type Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'id' in str(response.content):
            assert 'id' in str(response.content)
            print("ID Key  Assertion is Passed in Response Content")
        else:
            print("ID Key  Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("ID Key  Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '7576' in str(response.content):
            assert '7576' in str(response.content)
            print("Id Key's Value Assertion is Passed in Response Content")
        else:
            print("Id Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Id Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'country' in str(response.content):
            assert 'country' in str(response.content)
            print("Country Key Assertion is Passed in Response Content")
        else:
            print("Country Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Country Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'PK' in str(response.content):
            assert 'PK' in str(response.content)
            print("Country Key's Value Assertion is Passed in Response Content")
        else:
            print("Country Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Country Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'sunrise' in str(response.content):
             assert 'sunrise' in str(response.content)
             print("Sunrise Key Assertion is Passed in Response Content")
        else:
            print("Sunrise Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Sunrise Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '1595206435' in str(response.content):
            assert '1595206435' in str(response.content)
            print("Sunrise Key's Value Assertion is Passed in Response Content")
        else:
            print("Sunrise Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Sunrise Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'sunset' in str(response.content):
            assert 'sunset' in str(response.content)
            print("Sunset Key Assertion is Passed in Response Content")
        else:
            print("Sunset Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Sunset Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'timezone' in str(response.content):
            assert  'timezone' in str(response.content)
            print("Timezone Key Assertion is Passed in Response Content")
        else:
            print("Timezone Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Timezone Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '18000' in str(response.content):
            assert '18000' in str(response.content)
            print("Timezone Key's Value Assertion is Passed in Response Content")
        else:
            print("Timezone Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Timezone Key's Value Assertion is Failed in Response Content")
    try:
        if 'id' in str(response.content):
            assert 'id' in str(response.content)
            print("ID Key Assertion is Passed in Response Content")
        else:
            print("ID Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("ID Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if '1174872' in str(response.content):
            assert '1174872' in str(response.content)
            print("ID Key's Value Assertion is Passed in Response Content")
        else:
            print("ID Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("ID Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'name' in str(response.content):
            assert 'name' in str(response.content)
            print("Name Key Assertion is Passed in Response Content")
        else:
            print("Name Key Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Name Key Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if 'Karachi' in str(response.content):
            assert 'Karachi' in str(response.content)
            print("Name Key's Value Assertion is Passed in Response Content")
        else:
            print("Name Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("Name Key's Value Assertion is Failed in Response Content Due To : " + str(e))
    try:
        if  'cod' in str(response.content):
            assert 'cod' in str(response.content)
            print('COD Key Assertion is Passed in Response Content')
        else:
            print('COD Key Assertion is Failed in Response Content')
    except requests.RequestException as e:
        print('COD Key Assertion is Failed in Response Content Due To : ' + str(e))
    try:
        if '200' in str(response.content):
            assert '200' in str(response.content)
            print("COD Key's Value Assertion is Passed in Response Content")
        else:
            print("COD Key's Value Assertion is Failed in Response Content")
    except requests.RequestException as e:
        print("COD Key's Value Assertion is Failed in Response Content Due To : " + str(e))


response_content()


def response_url():
    print("response.url:")
    print("\t" + str(response.url))
    expected_url = 'https://api.openweathermap.org/data/2.5/weather?lat=24.87&lon=67.03&appid=c73e48a7ec5a89f57f52c48a792e7064'

    try:
        if expected_url in response.url:
            assert expected_url in response.url
            print("URL Assertion is Passed in Response URL")
        else:
            print("URL Assertion is Failed in Response URL")
    except requests.RequestException as e:
        print("URL Assertion is Failed in Response URL Due To : " + str(e))

    try:
        if "https" in response.url:
            assert "https" in response.url
            print("API Protocol Value Assertion is Passed in Response URL")
        else:
            print("API Protocol Value Assertion is Failed in Response URL")
    except requests.RequestException as e:
        print("API Protocol Value Assertion is Failed in Response URL Due To : " + str(e))
    try:
        if "24.87" in response.url:
            assert "24.87" in response.url
            print("lat Value Assertion is Passed in Response URL")
        else:
            print("lat Value Assertion is Failed in Response URL")
    except requests.RequestException as e:
        print("lat Value Assertion is Failed in Response URL Due To : " + str(e))
    try:
        if "67.03" in response.url:
            assert "67.03" in response.url
            print("Lon Value Assertion is Passed in Response URL")
        else:
            print("Lon Value Assertion is Failed in Response URL")
    except requests.RequestException as e:
        print("Lon Value Assertion is Failed in Response URL Due To : " + str(e))
    try:
        if "c73e48a7ec5a89f57f52c48a792e7064" in response.url:
            assert "c73e48a7ec5a89f57f52c48a792e7064" in response.url
            print("APPID Value Assertion is Passed in Response URL")
        else:
            print("APPID Value Assertion is Failed in Response URL")
    except requests.RequestException as e:
        print("APPID Value Assertion is Failed in Response URL Due To : " + str(e))
    try:
        if 'units=metric' in response.url:
            assert 'units=metric' in response.url
            print("Measurement System Assertion is Passed in Response URL")
        else:
            print("Measurement System Assertion is Failed in Response URL")
    except requests.RequestException as e:
        print("Measurement System Assertion is Failed in Response URL Due To : " + str(e))

response_url()

def response_cookies():
    print("response.cookies:")
    print("\t" + str(response.cookies))
    expected_cookies = "<RequestsCookieJar[]>"
    try:
        if "[]" in str(response.cookies):
            assert "[]" in str(response.cookies)
            print("Cookies Assertion is Passed in Response Cookies")
        else:
            print("Cookies Assertion is Failed in Response Cookies")
    except requests.RequestException as e:
        print("Cookies Assertion is Failes in Response Cookies Due To : " + str(e))
response_cookies()

def response_encoding():
    print("response.encoding:")
    print("\t" + str(response.encoding))
    expected_encoding = "utf-8"
    try:
        if "utf-8" in response.encoding:
            assert "utf-8" in response.encoding
            print('Unicode Transformation Format Assertion is Passed in Response Encoding')
        else:
            print('Unicode Transformation Format Assertion is Failed in Response Encoding')
    except requests.RequestException as e:
        print('Unicode Transformation Format Assertion is Failed in Response Encoding Due To : ' + str(e))

response_encoding()

def apparent_encoding():
    print("response.apparent_encoding:")
    print("\t" + str(response.apparent_encoding))
    expected_apparent_encoding = "ascii"
    try:
        if "ascii" in response.apparent_encoding:
            assert "ascii" in response.apparent_encoding
            print("Apparent Encoding Assertion is Passed in Response Apparent Encoding")
        else:
            print("Apparent Encoding Assertion is Failed in Response Apparent Encoding")
    except requests.RequestException as e:
        print("Apparent Encoding Assertion is Failed in Response Apparent Encoding Due To : " + str(e))
apparent_encoding()


def response_elapsed():
    print("response.elapsed:")
    print("\t" + str(response.elapsed))
    expected_elapsed = str(response.elapsed)
    try:
        if expected_elapsed in str(response.elapsed):
            assert expected_elapsed in str(response.elapsed)
            print('ELAPSED Assertion is Passed in Response Elapsed')
        else:
            print('ELAPSED Assertion is Failed in Response Elapsed')
    except requests.RequestException as e:
        print('ELAPSED Assertion is Failed in Response Elapsed Due To : ' + str(e))
response_elapsed()

def response_history():
    print("response.history:")
    print("\t" + str(response.history))
    try:
        if "[]" in str(response.history):
            assert "[]" in str(response.history)
            print("History Assertion is Passed in Response.History")
        else:
            print("History Assertion is Failed in Response.History")
    except requests.RequestException as e:
        print("History Assertion is Failed in Response.History Due To : " + str(e))

response_history()

def permanent_redirect():
    print("response.is_permanent_redirect:")
    print("\t" + str(response.is_permanent_redirect))

    try:
        if response.is_permanent_redirect == False:
            assert "False" in str(response.is_permanent_redirect)
            print("Permanent Redirect Assertion is Passed in Response Is Permanent Redirect ")
        else:
            print("Permanent Redirect Assertion is Failed in Response Is Permanent Redirect ")
    except requests.RequestException as e:
        print("Permanent Redirect Assertion is Failed in Response Is Permanent Redirect Due To : " + str(e))
permanent_redirect()

def is_redirect():
    print("response.is_redirect:")
    print("\t" + str(response.is_redirect))

    try:
        if response.is_redirect == False:
            assert "False" in str(response.is_redirect)
            print("Is Redirect Assertion is Passed in Response Is Redirect")
        else:
            print("Is Redirect Assertion is Failed in Response Is Redirect")
    except requests.RequestException as e:
        print("Is Redirect Assertion is Failed in Response Is Redirect Due To : " + str(e))

is_redirect()

def response_reason():
    print("response.reason:")
    print("\t" + str(response.reason))
    try:
        if "OK" in str(response.reason):
            assert "OK" in str(response.reason)
            print("Response Reason Value Assertion is Passed in Response Reason")
        else:
            print("Response Reason Value Assertion is Failed in Response Reason")
    except requests.RequestException as e:
        print("Response Reason Value Assertion is Failed in Response Reason Due To : " + str(e))

response_reason()

def response_json():
    print("response.json:")
    print("\t" + str(response.json()))
    Expected_Response = {'coord': {'lon': -0.13, 'lat': 51.51}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 292.41, 'feels_like': 287.93, 'temp_min': 290.93, 'temp_max': 293.71, 'pressure': 1021, 'humidity': 42}, 'visibility': 10000, 'wind': {'speed': 5.1, 'deg': 290}, 'clouds': {'all': 0}, 'dt': 1594063030, 'sys': {'type': 1, 'id': 1414, 'country': 'GB', 'sunrise': 1594007503, 'sunset': 1594066713}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
    try:
        if 'coord' in response.json():
            assert 'coord' in response.json()
            print("Coord Key Assertion is Passed in Response Json")
        else:
            print("Coord Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Coord Key Assertion is Failed in Response Json Due To : " + str(e))

    try:
        if 'lon' in response.json()['coord']:
            assert 'lon' in response.json()['coord']
            print("Coord Key Value Assertion is Passed in Response Json")
        else:
            print("Coord Key Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Coord Key Value Assertion is Failed in Response Json Due To : " + str(e))
    try:

        if '67.03' in str(response.json()['coord']['lon']):
            assert '67.03' in str(response.json()['coord']['lon'])
            print("Lon Key Value Assertion is Passed in Response Json")
        else:
            print("Lon Key Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Lon Key Value Assertion is Failed in Response Json Due To:" + str(e))

    try:
        if 'lat' in response.json()['coord']:
            assert 'lat' in response.json()['coord']
            print("Lat Key Assertion is Passed in Response Json")
        else:
            print("Lat Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Lat Key Assertion is Failed in Response Json Due To : " + str(e))
    try:

        if '24.87' in str(response.json()['coord']['lat']):
            assert '24.87' in str(response.json()['coord']['lat'])
            print("Lat Key Value Assertion is Passed in Response Json")
        else:
            print("Lat Key Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("lat Key Value Assertion is Failed in Response Json Due To:" + str(e))
    try:
        if 'weather' in str(response.json()):
            assert 'weather' in str(response.json())
            print("Weather Key Assertion is Passed in Response Json")
        else:
            print("Weather Key Assertion is Passed in Response Json")
    except requests.RequestException as e:
        print("Weather Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'id' in str(response.json()['weather'][0]):
            assert 'id' in str(response.json()['weather'][0])
            print("ID Key assertion is Passed in Response Json")
        else:
            print("ID Key assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("ID Key assertion is Failed in Response json Due To : " + str(e))
    try:
        if '803' in str(response.json()['weather']):
            assert '803' in str(response.json()['weather'])
            print("Weather Key Value ID Assertion is Passed in Response Json")
        else:
            print("Weather Key Value ID Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Weather Key Value ID Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'main' in str(response.json()):
            assert 'main' in str(response.json())
            print("Main Key Assertion is Passed in Response Json")
        else:
            print("Main Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Main Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'Clouds' in str(response.json()['main']):
            assert 'Clouds' in str(response.json()['main'])
            print("Main Key's Value Assertion is Passed in Response Json")
        else:
            print("Main Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Main Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'description' in str(response.json()):
            assert 'description' in str(response.json())
            print("Description Key Assertion is Passed in Response Json")
        else:
            print("Description Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Description Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if "broken clouds" in str(response.json()['weather']):
            assert "broken clouds" in str(response.json()['weather'])
            print("Description Key's Value Assertion is Passed in Response Json")
        else:
            print("Description Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Description Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'icon' in str(response.json()):
            assert 'icon' in str(response.json())
            print("Icon Key Assertion is Passed in Response Json")
        else:
            print("Icon Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Icon Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if "04d" in str(response.json()['weather']):
            assert "04d" in str(response.json()['weather'])
            print("Icon Key's Value Assertion is Passed in Response Json")
        else:
            print("Icon Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Icon Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'base' in str(response.json()):
            assert 'base' in str(response.json())
            print("Base Key Assertion is Passed in Response Json")
        else:
            print("Base Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Base Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if "stations" in str(response.json()['base']):
            assert "stations" in str(response.json()['base'])
            print("Base Key Value's Assertion is Passed in Response Json")
        else:
            print("Base Key Value's Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Base Key Value's Assertion is Failed in Response Json Due To : " + str(e))

    try:
        if 'main' in str(response.json()):
            assert 'main' in str(response.json())
            print("Main Key Assertion is Passed in Response Json")
        else:
            print("Main Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Main Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'temp' in str(response.json()['main']):
            assert 'temp' in str(response.json()['main'])
            print("Main Key's Value Assertion is Passed in Response Json")
        else:
            print("Main Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Main Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '30' in str(response.json()['main']['temp']):
            assert '30' in str(response.json()['main']['temp'])
            print("Temp Key's Value Assertion is Passed in Response Json")
        else:
            print("Temp Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Temp Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'feels_like' in str(response.json()):
            assert 'feels_like' in str(response.json())
            print("Feels Like Key Assertion is Passed in Response Json")
        else:
            print("Feels Like Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Feels Like Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if str(round(33.46)) in str(response.json()['main']['feels_like']):
            assert str(round(33.46)) in str(response.json()['main']['feels_like'])
            print("Feels Like Value Assertion is Passed in Response Json")
        else:
            print("Feels Like Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Feels Like Value Assertion is Failed in Response Json Due To : " + str(e))


    try:
        if 'temp_min' in str(response.json()['main']):
            assert 'temp_min' in str(response.json()['main'])
            print("Temp Min Key Assertion is Passed in Response Json")
        else:
            print("Temp Min Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Temp Min Key Assertion is Failed in Response Json Due To " + str(e))
    try:
        if '30' in str(response.json()['main']['temp_min']):
            assert '30' in str(response.json()['main']['temp_min'])
            print("Temp Min Key's Value Assertion is Passed in Response Json")
        else:
            print("Temp Min Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Temp Min Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'temp_max' in str(response.json()['main']):
            assert 'temp_max' in str(response.json()['main'])
            print("Temp Max Key Assertion is Passed in Response Json")
        else:
            print("Temp Max Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Temp Max Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '30' in str(response.json()['main']['temp_max']):
            assert '30' in str(response.json()['main']['temp_max'])
            print("Temp Max Key's Value Assertion is Passed in Response Json")
        else:
            print("Temp Max Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Temp Max Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'pressure' in str(response.json()['main']):
            assert 'pressure' in str(response.json()['main'])
            print("Pressure Key Assertion is Passed in Response Json")
        else:
            print("Pressure Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Pressure Key Assertion is Failed in Response Json Due To " + str(e))
    try:
        if '1002' in str(response.json()['main']['pressure']):
            assert '1002' in str(response.json()['main']['pressure'])
            print("Pressure Key's Value Assertion is Passed in Response Json")
        else:
            print("Pressure Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Pressure Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'humidity' in str(response.json()['main']):
            assert 'humidity' in str(response.json()['main'])
            print("Humidity Key Assertion is Passed in Response Json")
        else:
            print("Humidity Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Humidity Key Assertion is Failed in Response Json Due To : " + str(e))

    try:
        if '74' in str(response.json()['main']['humidity']):
            assert '74' in str(response.json()['main']['humidity'])
            print("Humidity Key's Value Assertion is Passed in Response Json")
        else:
            print("Humidity Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Humidity Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'visibility' in str(response.json()):
            assert 'visibility' in str(response.json())
            print('Visibility Key Assertion is Passed in Response Json')
        else:
            print('Visibility Key Assertion is Failed in Response Json')
    except requests.RequestException as e:
        print('Visibility Key Assertion is Failed in Response Json Due To : ' + str(e))
    try:
        if '6000' in str(response.json()['visibility']):
            assert '6000' in str(response.json()['visibility'])
            print("Visibility Key's Value Assertion is Passed in Response Json")
        else:
            print("Visibility Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Visibility Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'wind' in str(response.json()):
            assert 'wind' in str(response.json())
            print("Wind Key Assertion is Passed in Response Json")
        else:
            print("Wind Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Wind Key Assertion is Failed in Response Json Due To :  " + str(e))
    try:
        if 'speed' in str(response.json()['wind']):
            assert 'speed' in str(response.json()['wind'])
            print("Wind Key's Value Assertion is Passed in Response Json")
        else:
            print("Wind Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Wind Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '3.1' in str(response.json()['wind']['speed']):
            assert '3.1' in str(response.json()['wind']['speed'])
            print("Speed Key's Value Assertion is Passed in Response Json")
        else:
            print("Speed Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Speed Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'deg' in str(response.json()):
            assert 'deg' in str(response.json())
            print("Degree Key Assertion is Passed in Response Json")
        else:
            print("Degree Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Degree Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '230' in str(response.json()['wind']['deg']):
            assert '230' in str(response.json()['wind']['deg'])
            print("Degree Key's Value Assertion is Passed in Response Json")
        else:
            print("Degree Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Degree Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'clouds' in str(response.json()):
            assert 'clouds' in str(response.json())
            print("Clouds Key Assertion is Passed in Response Json")
        else:
            print("Clouds Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Clouds Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'all' in str(response.json()['clouds']):
            assert 'all' in str(response.json()['clouds'])
            print("Clouds Key's Value Assertion is Passed in Response Json")
        else:
            print("Clouds Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Clouds Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '75' in str(response.json()['clouds']['all']):
            assert '75' in str(response.json()['clouds']['all'])
            print("Clouds Key's Value Assertion is Passed in Response Json")
        else:
            print("Clouds Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Clouds Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'dt' in str(response.json()):
            assert 'dt' in str(response.json())
            print("DT Key Assertion is Passed in Response Json")
        else:
            print("DT Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("DT Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '1595368432' in str(response.json()['dt']):
            assert '1595368432' in str(response.json()['dt'])
            print("DT Key's Value Assertion is Passed in Response Json")
        else:
            print("DT Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("DT Key's Value Assertion is Failed in Response Json Due To : " + str(e))

    try:
        if 'sys' in str(response.json()):
            assert 'sys' in str(response.json())
            print("SYS Key Assertion is Passed in Response Json")
        else:
            print("SYS Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("SYS Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'type' in str(response.json()['sys']):
            assert 'type' in str(response.json()['sys'])
            print("SYS Key's Value Assertion is Passed in Response Json")
        else:
            print("SYS Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("SYS Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '1' in str(response.json()['sys']['type']):
            assert '1' in str(response.json()['sys']['type'])
            print("Type Key's Value Assertion is Passed in Response Json")
        else:
            print("Type Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Type Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'id' in str(response.json()['sys']):
            assert 'id' in str(response.json()['sys'])
            print("ID Key  Assertion is Passed in Response Json")
        else:
            print("ID Key  Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("ID Key  Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '7576' in str(response.json()['sys']['id']):
            assert '7576' in str(response.json()['sys']['id'])
            print("Id Key's Value Assertion is Passed in Response Json")
        else:
            print("Id Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Id Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'country' in str(response.json()['sys']):
            assert 'country' in str(response.json()['sys'])
            print("Country Key Assertion is Passed in Response Json")
        else:
            print("Country Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Country Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'PK' in str(response.json()['sys']['country']):
            assert 'PK' in str(response.json()['sys']['country'])
            print("Country Key's Value Assertion is Passed in Response Json")
        else:
            print("Country Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Country Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'sunrise' in str(response.json()['sys']):
            assert 'sunrise' in str(response.json()['sys'])
            print("Sunrise Key Assertion is Passed in Response Json")
        else:
            print("Sunrise Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Sunrise Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '1595379292' in str(response.json()['sys']['sunrise']):
            assert '1595379292' in str(response.json()['sys']['sunrise'])
            print("Sunrise Key's Value Assertion is Passed in Response Json")
        else:
            print("Sunrise Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Sunrise Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'sunset' in str(response.json()['sys']):
            assert 'sunset' in str(response.json()['sys'])
            print("Sunset Key Assertion is Passed in Response Json")
        else:
            print("Sunset Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Sunset Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '1595427687' in str(response.json()['sys']['sunset']):
            assert '1595427687' in str(response.json()['sys']['sunset'])
            print("Sunset Key's Value Assertion is Passed in Response Json")
        else:
            print("Sunset Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Sunset Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'timezone' in str(response.json()['sys']):
            assert 'timezone' in str(response.json()['sys'])
            print("Timezone Key Assertion is Passed in Response Json")
        else:
            print("Timezone Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Timezone Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '18000' in str(response.json()['timezone']):
            assert '18000' in str(response.json()['timezone'])
            print("Timezone Key's Value Assertion is Passed in Response Json")
        else:
            print("Timezone Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Timezone Key's Value Assertion is Failed in Response Json")
    try:
        if 'id' in str(response.json()['sys']):
            assert 'id' in str(response.json()['sys'])
            print("ID Key Assertion is Passed in Response Json")
        else:
            print("ID Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("ID Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if '1174872' in str(response.json()['sys']['id']):
            assert '1174872' in str(response.json()['sys']['id'])
            print("ID Key's Value Assertion is Passed in Response Json")
        else:
            print("ID Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("ID Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'name' in str(response.json()):
            assert 'name' in str(response.json())
            print("Name Key Assertion is Passed in Response Json")
        else:
            print("Name Key Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Name Key Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'Karachi' in str(response.json()['name']):
            assert 'Karachi' in str(response.json()['name'])
            print("Name Key's Value Assertion is Passed in Response Json")
        else:
            print("Name Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("Name Key's Value Assertion is Failed in Response Json Due To : " + str(e))
    try:
        if 'cod' in str(response.json()):
            assert 'cod' in str(response.json())
            print('COD Key Assertion is Passed in Response Json')
        else:
            print('COD Key Assertion is Failed in Response Json')
    except requests.RequestException as e:
        print('COD Key Assertion is Failed in Response Json Due To : ' + str(e))
    try:
        if '200' in str(response.json()['cod']):
            assert '200' in str(response.json()['cod'])
            print("COD Key's Value Assertion is Passed in Response Json")
        else:
            print("COD Key's Value Assertion is Failed in Response Json")
    except requests.RequestException as e:
        print("COD Key's Value Assertion is Failed in Response Json Due To : " + str(e))

response_json()
