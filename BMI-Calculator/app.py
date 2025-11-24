import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in cm"""
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    """Get BMI category and color"""
    if bmi < 18.5:
        return "Underweight", "#3498db", "🔵"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "#2ecc71", "🟢"
    elif 25 <= bmi < 30:
        return "Overweight", "#f39c12", "🟡"
    else:
        return "Obese", "#e74c3c", "🔴"

def main():
    # Page configuration
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon="⚖️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        font-size: 4rem;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .bmi-result {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        padding: 0.8rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        margin: 0.5rem 0;
    }
    .stSelectbox > div > div {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="main-header">⚖️ BMI Calculator</h1>', unsafe_allow_html=True)
    
    # Sidebar for inputs
    with st.sidebar:
        st.header("📊 Enter Your Details")
        
        # Weight input
        weight_unit = st.selectbox("Weight Unit", ["kg", "lbs"])
        if weight_unit == "kg":
            weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
        else:
            weight_lbs = st.number_input("Weight (lbs)", min_value=2.2, max_value=1100.0, value=154.0, step=0.1)
            weight = weight_lbs / 2.205  # Convert lbs to kg
        
        # Height input
        height_unit = st.selectbox("Height Unit", ["cm", "ft & in"])
        if height_unit == "cm":
            height = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)
        else:
            feet = st.number_input("Feet", min_value=1, max_value=10, value=5)
            inches = st.number_input("Inches", min_value=0, max_value=11, value=7)
            height = feet * 30.48 + inches * 2.54  # Convert ft & in to cm
        
        # Calculate button
        calculate = st.button("Calculate BMI", type="primary", use_container_width=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Calculate BMI automatically (always show results)
        bmi = calculate_bmi(weight, height)
        category, color, emoji = get_bmi_category(bmi)
        
        # Display BMI result
        st.markdown(f"""
        <div class="bmi-result" style="background-color: {color}20; color: {color}; border: 2px solid {color};">
            {emoji} Your BMI: {bmi}
        </div>
        """, unsafe_allow_html=True)
        
        # Display category
        st.markdown(f"""
        <div style="text-align: center; font-size: 1.5rem; margin-bottom: 2rem;">
            Category: <strong style="color: {color};">{category}</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # BMI ranges table
        st.subheader("📋 BMI Categories")
        bmi_data = {
            "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
            "BMI Range": ["< 18.5", "18.5 - 24.9", "25.0 - 29.9", "≥ 30.0"],
            "Color": ["🔵", "🟢", "🟡", "🔴"]
        }
        bmi_df = pd.DataFrame(bmi_data)
        st.dataframe(bmi_df, use_container_width=True, hide_index=True)
        
        # BMI chart
        st.subheader("📈 BMI Visualization")
        
        # Create a simple bar chart showing where the user's BMI falls
        categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
        ranges = [17, 21.7, 27.5, 32.5]  # Midpoints for visualization
        colors = ["#3498db", "#2ecc71", "#f39c12", "#e74c3c"]
        
        # Highlight current BMI category
        highlight_colors = []
        for i, cat in enumerate(categories):
            if cat == category:
                highlight_colors.append(colors[i])
            else:
                highlight_colors.append("#ecf0f1")
        
        fig = px.bar(
            x=categories, 
            y=ranges,
            color=categories,
            color_discrete_sequence=highlight_colors,
            title="BMI Categories Overview"
        )
        fig.add_hline(y=bmi, line_dash="dash", line_color="red", 
                     annotation_text=f"Your BMI: {bmi}")
        fig.update_layout(
            showlegend=False,
            xaxis_title="Category",
            yaxis_title="BMI Value",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💡 Health Tips")
        
        # Dynamic tips based on BMI category (always show category-specific tips)
        if category == "Underweight":
            st.info("""
            **Tips for Underweight:**
            - Eat more frequent, nutrient-dense meals
            - Include healthy fats (nuts, avocados)
            - Strength training to build muscle
            - Consult a healthcare provider
            """)
        elif category == "Normal weight":
            st.success("""
            **Maintain Your Health:**
            - Keep up your current healthy habits
            - Regular exercise (150 min/week)
            - Balanced diet with variety
            - Regular health checkups
            """)
        elif category == "Overweight":
            st.warning("""
            **Tips for Overweight:**
            - Focus on portion control
            - Increase physical activity
            - Choose whole, unprocessed foods
            - Set realistic weight loss goals
            """)
        else:  # Obese
            st.error("""
            **Important - Consult Healthcare Provider:**
            - Medical supervision recommended
            - Structured weight management program
            - Address underlying health conditions
            - Professional dietary guidance
            """)
        
        # Additional information
        st.markdown("""
        <div class="metric-card">
            <h4>📏 About BMI</h4>
            <p>Body Mass Index (BMI) is calculated using your weight and height. It's a useful screening tool to identify weight categories that may lead to health problems.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="metric-card">
            <h4>⚠️ Limitations</h4>
            <p>BMI doesn't account for muscle mass, bone density, or fat distribution. Athletes and elderly may have misleading BMI values.</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()