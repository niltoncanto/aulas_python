from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None
    def register_observer(self, observer):
        self._observers.append(observer)
    def remove_observer(self, observer):
        self._observers.remove(observer)
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)
    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()
class DigitalDisplay(Observer):
    def update(self, temperature):
        print(f"Digital Display: A temperatura atual é {temperature}°C")
class AnalogDisplay(Observer):
    def update(self, temperature):
        print(f"Analog Display: A temperatura atual é {temperature}°C")
if __name__ == "__main__":
    weather_station = WeatherStation()
    digital_display = DigitalDisplay()
    analog_display = AnalogDisplay()
    weather_station.register_observer(digital_display)
    weather_station.register_observer(analog_display)
    weather_station.set_temperature(25)  # Ambos displays serão notificados
    weather_station.set_temperature(30)  # Ambos displays serão notificados novamente
