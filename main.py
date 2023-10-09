# device.py
class Device:
    def __init__(self, name: str):
        self.name = name
        self.state = "off"

    def turn_on(self):
        self.state = "on"

    def turn_off(self):
        self.state = "off"

# strategy.py
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, device):
        pass

class HeatingStrategy(Strategy):
    def execute(self, device):
        if "heating" in device.name.lower():
            device.turn_on()
            print(f"Turning on heating for {device.name}")

class LightingStrategy(Strategy):
    def execute(self, device):
        if "light" in device.name.lower():
            device.turn_on()
            print(f"Turning on lights for {device.name}")

# controller.py
from typing import List

# decorator
def require_strategy(func):
    def wrapper(controller, device_name):
        if not controller.strategy:
            print("No strategy set. Please set a strategy first.")
        else:
            func(controller, device_name)
    return wrapper

class HomeController:
    def __init__(self):
        self.devices: List[Device] = []
        self.strategy: Strategy = None

    def add_device(self, device: Device):
        self.devices.append(device)

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    @require_strategy  
    def control_device(self, device_name: str):
        for device in self.devices:
            if device.name.lower() == device_name.lower():
                self.strategy.execute(device)
                break
        else:
            print(f"Device {device_name} not found.")

if __name__ == "__main__":
    controller = HomeController()

    living_room_heating = Device("Living Room Heating")
    kitchen_light = Device("Kitchen Light")

    controller.add_device(living_room_heating)
    controller.add_device(kitchen_light)

    heating_strategy = HeatingStrategy()
    lighting_strategy = LightingStrategy()

    controller.set_strategy(heating_strategy)
    controller.set_strategy(lighting_strategy)

    user_device = input("Enter the device you want to control: ")
    controller.control_device(user_device)
