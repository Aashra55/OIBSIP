document.addEventListener('DOMContentLoaded', () => {
    const cityInput = document.getElementById('city');
    const searchBtn = document.getElementById('search-btn');
    const localWeatherBtn = document.getElementById('local-weather-btn');
    const resultDiv = document.getElementById('result');
    const loader = document.getElementById('loader');
    const weatherIcon = document.getElementById('weather-icon');

    searchBtn.addEventListener('click', () => {
        const city = cityInput.value.trim();
        if (city) {
            getWeatherByCity(city);
        }
    });

    localWeatherBtn.addEventListener('click', () => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(position => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                getWeatherByCoords(lat, lon);
            }, () => {
                showError('Unable to retrieve your location.');
            });
        } else {
            showError('Geolocation is not supported by your browser.');
        }
    });

    async function getWeatherByCity(city) {
        showLoader();
        try {
            const res = await fetch(`http://127.0.0.1:5000/weather?city=${city}`);
            const data = await res.json();
            hideLoader();
            if (data.error) {
                showError(data.error);
            } else {
                displayWeather(data);
            }
        } catch (error) {
            hideLoader();
            showError('An error occurred while fetching the weather data.');
        }
    }

    async function getWeatherByCoords(lat, lon) {
        showLoader();
        try {
            const res = await fetch(`http://127.0.0.1:5000/weather?lat=${lat}&lon=${lon}`);
            const data = await res.json();
            hideLoader();
            if (data.error) {
                showError(data.error);
            } else {
                displayWeather(data);
            }
        } catch (error) {
            hideLoader();
            showError('An error occurred while fetching the weather data.');
        }
    }

    function displayWeather(data) {
        resultDiv.innerHTML = `
            <p><strong>City:</strong> ${data.city}</p>
            <p><strong>Temperature:</strong> ${data.temperature}°C</p>
            <p><strong>Description:</strong> ${data.description}</p>
        `;
        weatherIcon.innerHTML = getWeatherIcon(data.description);
    }

    function getWeatherIcon(description) {
        const lowerCaseDescription = description.toLowerCase();
        if (lowerCaseDescription.includes('clear')) {
            return '<i class="fas fa-sun"></i>';
        } else if (lowerCaseDescription.includes('clouds')) {
            return '<i class="fas fa-cloud"></i>';
        } else if (lowerCaseDescription.includes('rain')) {
            return '<i class="fas fa-cloud-showers-heavy"></i>';
        } else if (lowerCaseDescription.includes('snow')) {
            return '<i class="fas fa-snowflake"></i>';
        } else if (lowerCaseDescription.includes('thunderstorm')) {
            return '<i class="fas fa-bolt"></i>';
        } else if (lowerCaseDescription.includes('drizzle')) {
            return '<i class="fas fa-cloud-rain"></i>';
        } else if (lowerCaseDescription.includes('mist') || lowerCaseDescription.includes('fog') || lowerCaseDescription.includes('haze')) {
            return '<i class="fas fa-smog"></i>';
        } else {
            return '<i class="fas fa-question-circle"></i>';
        }
    }

    function showError(message) {
        resultDiv.innerHTML = `<p class="error">${message}</p>`;
    }

    function showLoader() {
        loader.style.display = 'block';
        resultDiv.innerHTML = '';
        weatherIcon.innerHTML = '';
    }

    function hideLoader() {
        loader.style.display = 'none';
    }
});