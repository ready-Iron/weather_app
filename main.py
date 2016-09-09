from sys import argv, exit

import requests

def main():
    try:
        api_key = argv[1]
    except:
        print ("Please enter valid API key")
        exit(0)

        

    print ("What City and Country are you looking for?")
    print ("Use [city,country], use 2 letter country abbreviation")
    print ("Enter city,country") 
    answer = input(">>> ")


    payload = { 
        "appid": api_key,
        "q": answer,
        "units": "imperial"}

    w = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)
    print (w.url)

    f = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=payload)
    print (f.url) 
    weather = w.json()
    forecast = f.json()
    
    

    print("Current Temp:{}".format(weather["main"]["temp"]))

    print("Current Humidity:{}".format(weather["main"]["humidity"]))

    print("Current Description:{}".format(weather["weather"][0]["description"]))

    for count, day in enumerate(forecast["list"]):
        if forecast["list"][count]["dt_txt"].split(" ")[1] == "12:00:00":    
            print("Date:{}".format(forecast["list"][count]["dt_txt"]))
            print ("Forecast Temp:{}".format(forecast["list"][count]["main"]["temp"]))
            print ("Humidity:{}".format(forecast["list"][count]["main"]["humidity"]))




    
     


if __name__ == '__main__':
    main()