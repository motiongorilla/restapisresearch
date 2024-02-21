import requests
from datetime import datetime

API_KEY = "af6802d23eca95bf109c703dbc8dbf17"

def makeUrl(city, country_code, api_key, units="metric"):
    urlbase = "https://api.openweathermap.org/data/2.5/forecast"
    citySearch = f"?q={city},{country_code}"
    measureUnits = f"&units={units}"
    api = f"&appid={api_key}"

    url = urlbase + citySearch + measureUnits + api
    return url

def makeRequest(url):
    request = requests.get(url)
    content = request.json()
    return content

def main():
    url = makeUrl(city="London", country_code="uk", units="metric", api_key=API_KEY)
    data = makeRequest(url)

    listOfData = data["list"]
    city = data["city"]["name"]

    with open("weather.txt", "w") as file:
        file.write("City,Time,Temperature,Condition\n")
        for l in listOfData:
            time = datetime.fromtimestamp(l["dt"])
            temperature = l["main"]["temp"]
            weather_condition = l["weather"][0]["description"]
            file.write(f"{city},{time},{temperature},{weather_condition}\n")


if __name__ == "__main__":
    main()
