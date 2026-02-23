from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from typing import List



class WeatherStation:
    def __init__(self):
        self._temperature: int = 0
        self._observers: List[NewsService] = []

    def attach(self, observer: NewsService) -> None:
        print("WeatherStation: Додано службу новин.")
        self._observers.append(observer)

    def detach(self, observer: NewsService) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("WeatherStation: Сповіщення служб новин...")
        for observer in self._observers:
            observer.update(self)

    def change_temperature(self) -> None:
        print("\nWeatherStation: Вимірювання температури...")
        self._temperature = randint(-10, 35)
        print(f"WeatherStation: Нова температура: {self._temperature}°C")
        self.notify()


class NewsService(ABC):
    @abstractmethod
    def update(self, station: WeatherStation) -> None:
        pass



class TVNews(NewsService):
    def update(self, station: WeatherStation) -> None:
        if station._temperature > 30:
            print("TVNews: Термінова новина! Сильна спека!")
        elif station._temperature < 0:
            print("TVNews: Попередження про мороз!")


class InternetNews(NewsService):
    def update(self, station: WeatherStation) -> None:
        print(f"InternetNews: Оновлення погоди: {station._temperature}°C")



if __name__ == "__main__":
    station = WeatherStation()

    tv = TVNews()
    internet = InternetNews()

    station.attach(tv)
    station.attach(internet)

    station.change_temperature()
    station.change_temperature()

    station.detach(tv)

    station.change_temperature()