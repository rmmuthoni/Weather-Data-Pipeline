from pathlib import Path
import sys

# Root Directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import setting
from db_models import WeatherData, Base 
from extract import fetch_weather_data
from transform import transform_weather_data


SessionLocal = setting.SESSION_LOCAL
engine = setting.DATABASE_ENGINE


def send_to_database(data: dict) -> None:
    """
    Sends the provided weather data to the PostgreSQL database.

    Args:
        data (dict): A dictionary containing weather data.

    Raises:
        Exception: If there is an error while sending data to the database.
    """

    # Create all the tables/Schemas incase new or never created 
    Base.metadata.create_all(bind=engine)
    
    with SessionLocal() as session:
        try:
            # Create a new WeatherData instance
            weather_data = WeatherData(
                timestamp=data.get("timestamp"),
                temperature=data.get("temperature"),
                temperature_feels_like=data.get("temperature_feels_like"),
                temperature_min=data.get("temperature_min"),
                temperature_max=data.get("temperature_max"),
                pressure=data.get("pressure"),
                humidity=data.get("humidity"),
                wind_speed=data.get("wind_speed"),
                wind_direction=data.get("wind_direction"),
                city=data.get("city"),
                country=data.get("country"),
            )

            # Add the new instance to the session and commit
            session.add(weather_data)
            session.commit()
        except Exception as e:
            session.rollback()  # Rollback in case of error
            print(f"Error sending data to database: {e}")


transformed_data = transform_weather_data()

send_to_database(transformed_data)
        