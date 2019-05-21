import requests
weather_reposonse=requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=0583a32030db119217dc0595d49acc33')
print(weather_reposonse.json())