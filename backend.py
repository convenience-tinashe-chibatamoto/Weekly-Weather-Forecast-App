import requests

API_KEY = os.getenv("API_KEY")

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    if kind == "Temperature":
        filtered_data = [d["main"]["temp"] for d in filtered_data]
    elif kind == "Sky":
        filtered_data = [d["weather"][0]["main"] for d in filtered_data]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))
