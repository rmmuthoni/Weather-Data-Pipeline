import sys
from pathlib import Path
from typing import Any

import requests
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from setting import API_URL


@retry(
    stop=stop_after_attempt(3), 
    wait=wait_exponential(multiplier=1, min=4, max=10), 
    retry=retry_if_exception_type(requests.exceptions.RequestException),
    reraise=True
)
def fetch_weather_data() -> Any:
    """
    Fetches weather data from the OpenWeatherMap API.
    Returns:
        dict: A dictionary containing the weather data.
    Raises:
        requests.exceptions.RequestException: If the API request fails.
    """ 

    response_payload = requests.get(API_URL, timeout=10)  # Make a GET request to the API with a timeout of 10 seconds
    response_payload.raise_for_status()  # Raise an exception for HTTP errors
    return response_payload.json()  # Return the JSON response as a dictionary 

