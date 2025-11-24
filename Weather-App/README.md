# README.md — Weather App

## Project Overview

This is a simple **Weather App** built with **Python (Flask)** for the backend and **JavaScript/HTML/CSS** for the frontend. Users can enter a city name and get current weather information including temperature and description.

## Features

* Search weather by city name
* Displays temperature in Celsius
* Shows weather description
* Responsive and simple frontend

## Tech Stack

* **Backend:** Python, Flask, Requests
* **Frontend:** HTML, CSS, JavaScript
* **API:** OpenWeatherMap

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd weather-app
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set your OpenWeatherMap API key in `app.py`:

```python
API_KEY = "YOUR_API_KEY"
```

## Running the App

```bash
python app.py
```

* Backend will run on `http://127.0.0.1:5000`
* Open `index.html` in your browser to access the frontend.

## Usage

1. Enter a city name in the input box.
2. Click **Get Weather**.
3. View the temperature and description.

## Requirements

Create a `requirements.txt` file:

```
Flask==2.3.2
requests==2.32.0
```

## Optional Enhancements

* Add modern UI with Tailwind CSS or Bootstrap.
* Use React for a dynamic frontend.
* Show weather icons for different conditions.
* Deploy backend and frontend to cloud platforms.
