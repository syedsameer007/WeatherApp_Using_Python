import requests
import datetime as dt
import json #issey hum string to dictionary ko type casting karsakte hai
import pyttsx3 #bolsake
Speak = pyttsx3.init()
city = input("Enter the name of the City :")
URL=f"https://api.weatherapi.com/v1/current.json?key=9f0623a8e3e5402db07112633231712&q={city}"
r = requests.get(URL)
# print(r.text)
# print(type(r.text)) #issey kaunsa type hai voh dekh sakte hai, jaise ki yeh string type hai,and if we want to convert this str to dictionary then use json method for that
Weather_Dict = json.loads(r.text) #abb yeh dictionary meh convert hogaya, issey hum specific part bhi print karasakte hai
print(Weather_Dict["current"]["temp_c"]) #yeh particular temparature lakar deydeyga
W=Weather_Dict["current"]["temp_c"]
Speak.say(f"The current weather in {city}is{W}Degrees") #i have applied to speak here
Speak.runAndWait()


# 9f0623a8e3e5402db07112633231712 

# api_key = '9f0623a8e3e5402db07112633231712'