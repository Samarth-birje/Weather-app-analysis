import streamlit as st
from weather_service import get_weather, get_forecast, get_weather_icon

st.title("🌤️ Weather App")

city = st.text_input("Enter the city name:")

unit = st.radio("Select Temparature unit",["Celsius","Fahrenheit"])

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city name")
    else:
        with st.spinner("Fetching weather data..."):
            weather, error = get_weather(city)

            if error:
                st.error(error)
            else:

                icon = get_weather_icon(weather["condition"])

                st.subheader(f"{icon}Current Weather")

                temp = weather["temperature"]
                if unit == "Fahrenheit":
                    temp = (temp*9/5)+32
                
                st.subheader("🌡️ Current Weather")
                st.write("City:", weather["city"])
                st.write("Temperature:", round(temp,2),"°",unit[0])
                st.write("Humidity:", weather["humidity"], "%")
                st.write("Wind Speed:", weather["wind_speed"], "m/s")
                st.write("Condition:", weather["condition"])
                st.write("Description:", weather["description"])

                forecast = get_forecast(city)

                if forecast:
                    st.subheader("📅 5-Day Forecast")
                    for day in forecast:
                        day_temp = day["temp"]
                        if unit == "Farhenheit":
                            day_temp = (day_temp * 9/5)+32

                        st.write(
                            f"📆 {day['date']} | {day['temp']}°C | {day['condition']}"
                        )
                else:
                    st.warning("Weather forecast data not available")

st.markdown("---")
st.caption("powered by OpenweatherMap API")