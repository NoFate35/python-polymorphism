import argparse
import requests
from weather_service import WeatherService


def main(city_name):
    # BEGIN (write your solution here)
    ws = WeatherService(requests)
    response = ws.look_up('Moscow')
    return response.text
    # END


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, required=True)
    args = parser.parse_args()
    print(main(args.city))
