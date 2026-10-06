from datetime import datetime
from typing import Any, Iterable, Sequence

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class WeatherData(Base):
    """Represents one weather observation stored in PostgreSQL."""

    # Table Name
    __tablename__ = "weather_data"

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    temperature_feels_like = Column(Float, nullable=False)
    temperature_min = Column(Float, nullable=False)
    temperature_max = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    wind_speed = Column(Float, nullable=False)
    wind_direction = Column(Float, nullable=False)
    city = Column(String(255), nullable=False)
    country = Column(String(2), nullable=False)
    is_valid = Column(Boolean, nullable=False, default=True)

    # String Representation of the OBject
    def __repr__(self) -> str:
        return f"Weather Data for {self.city}, {self.country} at {self.timestamp}"

