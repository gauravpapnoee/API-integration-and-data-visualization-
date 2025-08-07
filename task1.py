import requests
import matplotlib.pyplot as plt

# Replace with your OpenWeatherMap API key
API_KEY = "your_api_key"
CITY = "Delhi"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = []
temps = []

# Extracting date and temperature
for item in data['list']:
    dates.append(item['dt_txt'])
    temps.append(item['main']['temp'])

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(dates[:10], temps[:10], marker='o')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date/Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()