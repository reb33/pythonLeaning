import pyowm

owm = pyowm.OWM('1ddfb3ddbdd76c5ae25e0e0ba31e49c4')

city = input("Город: ")

observation = owm.weather_at_place(city)
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']

print(w)
print ("Температура "+str(temp))
print ("Статус "+ str(w.get_detailed_status()))