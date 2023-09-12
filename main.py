import requests
import json
import os
city=input("Enter the name of the city: ")
url= f"https://api.weatherapi.com/v1/current.json?key=eb2d6398645d49fbaa3145114231209&q={city}"
r=requests.get(url)
weather_dic=json.loads(r.text)
w=weather_dic["current"]["temp_c"]
print(weather_dic["current"]["temp_c"])
command=f"PowerShell -Command "f"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('The Current weather in {city} is {w} degrees');"
os.system(command)