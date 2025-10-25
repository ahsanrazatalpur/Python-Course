import requests
import sys
from datetime import datetime, timezone, timedelta

class Weather:
    """
    Simple weather app using OpenWeatherMap current weather API.
    All functionality is inside this class.
    """

    def __init__(self, api_key: str, units: str = "metric", timeout: int = 10):
        self.api_key = api_key
        self.units = units
        self.timeout = timeout
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def _build_params(self, city: str) -> dict:
        return {
            "q": city,
            "appid": self.api_key,
            "units": self.units,
        }

    def _fetch(self, city: str) -> dict:
        params = self._build_params(city)
        try:
            resp = requests.get(self.base_url, params=params, timeout=self.timeout)
        except requests.exceptions.Timeout:
            raise RuntimeError("Network error: request timed out.")
        except requests.exceptions.ConnectionError:
            raise RuntimeError("Network error: could not connect to the weather service.")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Network error: {e}")

        if resp.status_code == 401:
            raise RuntimeError("Invalid API key. Please check your API key and try again.")
        if resp.status_code == 404:
            # OpenWeatherMap returns 404 for city not found
            raise RuntimeError("City not found. Please check the city name and try again.")
        if resp.status_code >= 400:
            # Generic error
            try:
                message = resp.json().get("message", resp.text)
            except Exception:
                message = resp.text
            raise RuntimeError(f"API error ({resp.status_code}): {message}")

        try:
            return resp.json()
        except ValueError:
            raise RuntimeError("Invalid response from server (not JSON).")

    def _format_time(self, ts: int, tz_offset: int) -> str:
        # ts: unix timestamp (UTC), tz_offset: seconds east of UTC
        tz = timezone(timedelta(seconds=tz_offset))
        return datetime.fromtimestamp(ts, tz).strftime("%Y-%m-%d %H:%M:%S %Z")

    def _deg_to_compass(self, deg: float) -> str:
        # Convert wind degree to compass direction
        dirs = [
            "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
        ]
        idx = int((deg / 22.5) + 0.5) % 16
        return dirs[idx]

    def _display(self, data: dict) -> None:
        name = data.get("name", "Unknown location")
        sys_data = data.get("sys", {})
        country = sys_data.get("country", "")
        coords = data.get("coord", {})
        weather_list = data.get("weather", [])
        main = data.get("main", {})
        wind = data.get("wind", {})
        clouds = data.get("clouds", {})
        visibility = data.get("visibility")
        tz_offset = data.get("timezone", 0)

        weather_desc = ", ".join(w.get("description", "") for w in weather_list) or "N/A"
        temp = main.get("temp")
        feels_like = main.get("feels_like")
        temp_min = main.get("temp_min")
        temp_max = main.get("temp_max")
        humidity = main.get("humidity")
        pressure = main.get("pressure")
        wind_speed = wind.get("speed")
        wind_deg = wind.get("deg")
        wind_dir = self._deg_to_compass(wind_deg) if wind_deg is not None else "N/A"
        sunrise = sys_data.get("sunrise")
        sunset = sys_data.get("sunset")

        print(f"\nWeather for: {name}{', ' + country if country else ''}")
        if coords:
            print(f" Coordinates: lat={coords.get('lat')}, lon={coords.get('lon')}")
        print(f" Condition: {weather_desc.capitalize()}")
        if temp is not None:
            unit = "°C" if self.units == "metric" else "°F" if self.units == "imperial" else "K"
            print(f" Temperature: {temp}{unit} (feels like {feels_like}{unit})")
            if temp_min is not None and temp_max is not None:
                print(f" Min/Max: {temp_min}{unit} / {temp_max}{unit}")
        if humidity is not None:
            print(f" Humidity: {humidity}%")
        if pressure is not None:
            print(f" Pressure: {pressure} hPa")
        if wind_speed is not None:
            spd_unit = "m/s" if self.units in ("metric", "standard") else "mph"
            print(f" Wind: {wind_speed} {spd_unit} ({wind_dir})")
        if visibility is not None:
            print(f" Visibility: {visibility} meters")
        if clouds:
            print(f" Cloudiness: {clouds.get('all', 'N/A')}%")
        if sunrise:
            print(f" Sunrise: {self._format_time(sunrise, tz_offset)}")
        if sunset:
            print(f" Sunset:  {self._format_time(sunset, tz_offset)}")
        print()

    def run(self):
        try:
            city = input("Enter city name (e.g. London or London,UK): ").strip()
            if not city:
                print("No city entered. Exiting.")
                return
            data = self._fetch(city)
            self._display(data)
        except RuntimeError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nInterrupted by user.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Replace the API key below with your key (the user provided key is used here).
    API_KEY = "a77a9d0652f3368316cc27380720b84d"
    app = Weather(api_key=API_KEY, units="metric")
    app.run()