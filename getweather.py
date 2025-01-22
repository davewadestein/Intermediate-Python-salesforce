from threading import Thread
import json
from urllib.request import urlopen
import time

cities = ['Boulder', 'Atlanta', 'Germantown',
          'Reno', 'Honolulu', 'Zurich', 'Dubai',
          'Dublin','Stuttgart', 'Rome']

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=imperial'
            '&&APPID=10d4440bbaa8581bb8da9bd1fbea5617')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']

threads = [TempGetter(c) for c in cities]
start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print(f'it is {thread.temperature:.0f}°F in {thread.city}')
