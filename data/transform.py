from extract import fetch_weather_data 
from typing import Any, Dict
from validators import WeatherDataValidator
from pydantic import ValidationError





def transform_weather_data() -> Any:
    """
    Transforms raw weather data into a structured format.
    
    Args:
        raw_data (dict): The raw weather data fetched from the API.
        
    Returns:
        dict: A dictionary containing the transformed and validated weather data.
    """

    raw_data = fetch_weather_data()  # Fetch the raw weather data from the API

    cleaned_weather_data = {
        "temperature": raw_data.get("main", {}).get("temp"),
        "temperature_feels_like": raw_data.get("main", {}).get("feels_like"),
        "temperature_min": raw_data.get("main", {}).get("temp_min"),
        "temperature_max": raw_data.get("main", {}).get("temp_max"),
        "pressure": raw_data.get("main", {}).get("pressure"),
        "humidity": raw_data.get("main", {}).get("humidity"),
        "wind_speed": raw_data.get("wind", {}).get("speed"),
        "wind_direction": raw_data.get("wind", {}).get("deg"),
        "city": raw_data.get("name"),
        "country": raw_data.get("sys", {}).get("country"),
    }

    # Validate the cleaned data using Pydantic
    try:
        validated_data = WeatherDataValidator.model_validate(cleaned_weather_data)
    except ValidationError as e:
        print(f"Error validating weather data: {e}")
        validated_data = None
    else:
        return validated_data