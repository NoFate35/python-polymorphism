API_URL = 'http://localhost:8080/api/v2/'


class WeatherService():
# BEGIN (write your solution here)
    def __init__(self, http_client):
        self.http_client = http_client
        
    def look_up(self, city):
        response = self.http_client.get('http://localhost:8080/api/v2/cities/' + city)
        return response.json()
# END