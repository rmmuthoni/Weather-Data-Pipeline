from datetime import datetime

from pydantic import BaseModel,Field 


class WeatherDataValidator(BaseModel):
    timestamp: str = Field(..., default_factory=lambda: datetime.now(), description="Timestamp of the weather data in ISO 8601 format")
    temperature: float = Field(..., description="Temperature in Celsius")
    temperature_feels_like: float = Field(..., description="Feels like temperature in Celsius")
    temperature_min: float = Field(..., description="Minimum temperature in Celsius")
    temperature_max: float = Field(..., description="Maximum temperature in Celsius")
    pressure: float = Field(..., description="Atmospheric pressure in hPa")
    humidity: float = Field(..., description="Humidity percentage")
    wind_speed: float = Field(..., description="Wind speed in km/h")
    wind_direction: float = Field(..., description="Wind direction in degrees")
    city: str = Field(..., description="City name") 
    country: str = Field(..., description="Country name") 