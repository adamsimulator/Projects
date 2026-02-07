import requests



API_KEY = #PUT KEY HERE#
city = str(input("Enter city name:")).lower()

default_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
metric_choice = str(input("Choose your metric system - Metric/Imperial/Default(Kelvin):")).lower()

if metric_choice == "metric":
    url = default_url + "&units=metric"
elif metric_choice == "imperial":
    url = default_url + "&units=imperial"
else:
    url = default_url

response = requests.get(url)
info = response.json()

temp = info['main']['temp']
humidity = info['main']['humidity']
wind_speed = info['wind']['speed']
weatherDesc= info['weather'][0]['description']

print(f"Temperature: {temp}")
print(f"Humidity: {humidity}")
print(f"Wind Speed: {wind_speed}")
print(f"Weather description: {weatherDesc}")


