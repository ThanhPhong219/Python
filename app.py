import requests 
import datetime as dt
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = '48163848c8b82384b9d2e678bb860728'
CITY = input("Enter City: ")
url = base_url + "appid=" + api_key + "&q=" + CITY
response = requests.get(url).json()
def k_t_c_f (kelvin):
    c = kelvin - 275.13
    fa = c * (9/5) + 32
    return c ,fa
temp_k = response['main']['temp']
temp_c , temp_fa = k_t_c_f(temp_k)
feel_like_k = response['main']['feels_like']
feel_like_c , feel_like_fa = k_t_c_f(feel_like_k)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
des = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
print(f"Temperature in {CITY}: {temp_c:.2f}C or {temp_fa}F")
print(f"Temperature in {CITY} feels like : {feel_like_c:.2f}C or {feel_like_fa}F")
print(f"Humidcity in {CITY} : {humidity:}%")
print(f"Wind Speed in {CITY} : {wind_speed}m/s")
print(f"Genaral Weather in {CITY} : {des}")
print(f"Sunrise in {CITY} at : {sunrise_time} local time.")
print(f"Sunset in {CITY} at : {sunset_time} local time.")