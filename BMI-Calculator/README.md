# BMI Calculator - Streamlit App

A beautiful and interactive BMI (Body Mass Index) Calculator built with Streamlit.

## Features

- 🎯 **Easy Input**: Support for both metric (kg/cm) and imperial (lbs/ft & in) units
- 📊 **Visual Results**: Color-coded BMI results with emoji indicators
- 📈 **Interactive Charts**: Plotly charts showing BMI categories
- 💡 **Health Tips**: Personalized recommendations based on BMI category
- 🎨 **Modern UI**: Clean, responsive design with custom styling
- 📱 **Mobile Friendly**: Works great on all device sizes

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run bmi_calculator.py
```

The app will open in your default web browser at `http://localhost:8501`

## How to Use

1. **Select Units**: Choose your preferred weight and height units from the sidebar
2. **Enter Details**: Input your weight and height using the number inputs
3. **Calculate**: Click the "Calculate BMI" button
4. **View Results**: See your BMI, category, and personalized health tips

## BMI Categories

- 🔵 **Underweight**: BMI < 18.5
- 🟢 **Normal weight**: BMI 18.5 - 24.9
- 🟡 **Overweight**: BMI 25.0 - 29.9
- 🔴 **Obese**: BMI ≥ 30.0

## Technical Details

- Built with Streamlit for the web interface
- Uses Plotly for interactive visualizations
- Responsive design with custom CSS
- Supports both metric and imperial units
- Real-time BMI calculation and categorization

## Disclaimer

BMI is a screening tool and should not be used as a diagnostic tool. Always consult with healthcare professionals for medical advice.