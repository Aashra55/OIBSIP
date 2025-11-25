# Weather App

A simple and modern weather application that allows users to get the current weather for any city in the world, or for their current location.

## Features

- **Search by City:** Get the current weather by entering a city name.
- **Local Weather:** Get the weather for your current location with a single click.
- **Dynamic UI:** A clean and responsive user interface with a loading indicator.
- **Error Handling:** Clear error messages for invalid cities or network issues.

## Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **API:** OpenWeatherMap

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd Weather-App
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the environment variables:**
    - Rename the `.env.example` file to `.env`.
    - Open the `.env` file and replace `your_api_key_here` with your actual OpenWeatherMap API key.
    ```
    API_KEY=your_api_key_here
    ```

## Running the Application

1.  **Start the Flask server:**
    ```bash
    python app.py
    ```
    The backend server will start running at `http://127.0.0.1:5000`.

2.  **Open the application in your browser:**
    - Simply open the `index.html` file in your web browser to use the application.

## How to Use

- **To get weather by city:** Enter the name of a city in the input field and click the "Get Weather" button.
- **To get local weather:** Click the "Get Local Weather" button and allow the browser to access your location.

