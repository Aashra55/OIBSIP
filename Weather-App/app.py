from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"

@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City is required"}), 400
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return jsonify({"error": response.get("message", "Error fetching data")}), 400
    
    data = {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
