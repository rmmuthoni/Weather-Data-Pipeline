import requests 
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from typing import Any


@retry(
    stop=stop_after_attempt(3), 
    wait=wait_exponential(multiplier=1, min=4, max=10), 
    retry=retry_if_exception_type(requests.exceptions.RequestException),
)
def fetch_weather_data() -> Any:
    """
    Fetches weather data from the OpenWeatherMap API.
    Returns:
        dict: A dictionary containing the weather data.
    Raises:
        requests.exceptions.RequestException: If the API request fails.
    """ 

    pass
