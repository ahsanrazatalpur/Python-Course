from flask import Flask, render_template, request, send_from_directory
import requests
import os

app = Flask(__name__)

API_KEY = "a77a9d0652f3368316cc27380720b84d"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            print("URL Requested:", url)           # DEBUG
            print("Status Code:", response.status_code)
            print("Response Text:", response.text) # DEBUG
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"]
                }
            else:
                data = response.json()
                weather_data = {"error": data.get("message", "City not found!")}
    return render_template("index.html", weather=weather_data)

# Serve CSS
@app.route('/style.css')
def css():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'style.css')

# <--- THIS PART STARTS THE SERVER --->
if __name__ == "__main__":
    app.run(debug=True)
