from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

load_dotenv()  

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    elif lat and lon:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    else:
        return jsonify({"error": "City or coordinates are required"}), 400
    
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return jsonify({"error": response.get("message", "Error fetching data")}), response.get("cod")
    
    data = {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
