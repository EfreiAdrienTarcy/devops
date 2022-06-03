import os
import requests
import json


def main():

    latitude = os.environ["LAT"]
    longitude = os.environ["LONG"]
    key = os.environ["API_KEY"]

    complete_url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)+"&appid="+str(key)
   

    response = requests.get(complete_url)

    rep = response.json()

    if rep["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = rep["main"]
 
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
 
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
 
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
 
        # store the value of "weather"
        # key in variable z
        z = rep["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
    
        # print following values
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidity) +
            "\n description = " +
                        str(weather_description))
    
    else:
        print(" City Not Found ")



if __name__ == '__main__':
    main()