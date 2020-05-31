import requests
import json


api_key = "Enter api key"

base_url =  "http://api.openweathermap.org/data/2.5/weather?"

city = input("enter city name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x['main']
    current_temp = y["temp"]
    current_press = y["pressure"]
    current_humidity = y["humidity"] 
    z = x["weather"]
    weather_desc = z[0]["description"]
    celsiusTemp = current_temp - 273.15

    print("\n Temperature (in kelvin unit) = " +
                    str(current_temp) + 
        "\n Temperature (in Celsius) = " +
                    str(celsiusTemp) +
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_press) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n weather description = " +
                    str(weather_desc) + "\n") 

else:
    print("Not found")
  