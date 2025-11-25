import re
import subprocess
from pathlib import Path

import requests
from dependency_nversion.weather_service import WeatherService


def test_weather_service():
    http_client = requests
    service = WeatherService(http_client)
    response = service.look_up("berlin")

    assert response["name"] == "berlin"


def test_weather_app():
    p = Path(__file__).absolute().parent
    app_path = p.joinpath("..", "src/scripts/weather.py")
    result = subprocess.run(
        ["poetry", "run", "python", app_path, "--city", "berlin"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert re.search(r"Temperature in berlin: \d+C", result.stdout)
