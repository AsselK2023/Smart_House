# device.py
class Device:
    def __init__(self, name: str):
        self.name = name
        self.state = "off"

    def turn_on(self, color=None):
        self.state = "on"
        if color:
            print(f"Turning on {self.name} with color {color}")
        else:
            print(f"Turning on {self.name}")

    def turn_off(self):
        self.state = "off"
        print(f"Turning off {self.name}")



# strategy.py
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, device, color=None):
        pass

class HeatingStrategy(Strategy):
    def execute(self, device, color=None):
        if "heating" in device.name.lower():
            device.turn_on(color)
            print(f"Turning on heating for {device.name}")

class LightingStrategy(Strategy):
    def execute(self, device, color=None):
        if "light" in device.name.lower():
            device.turn_on(color)
            print(f"Turning on lights for {device.name}")
            
# adapter.py
class StrategyAdapter(Strategy):
    def __init__(self, decorator):
        self.decorator = decorator

    def execute(self, device, color=None):
        return self.decorator.control_device(device.name, color)


# decorator.py
class ColorSelectorDecorator:
    def __init__(self, controller):
        self.controller = controller

    def control_device(self, device_name, color=None):
        for device in self.controller.devices:
            if device.name.lower() == device_name.lower():
                if "light" in device.name.lower() and not color:
                    color = input(f"Enter the color for the {device.name}: ")
                result = self.controller.control_device(device_name, color)
                return result
        print(f"Device {device_name} not found.")



# controller.py
from typing import List

class HomeController:
    def __init__(self):
        self.devices: List[Device] = []
        self.strategies = {}

    def add_device(self, device: Device):
        self.devices.append(device)

    def set_strategy(self, device_name, strategy):
        self.strategies[device_name.lower()] = strategy

    def control_device(self, device_name, color=None):
        device_name_lower = device_name.lower()
        for device in self.devices:
            if device.name.lower() == device_name_lower:
                if device_name_lower in self.strategies:
                    strategy = self.strategies[device_name_lower]
                else:
                    strategy = self.default_strategy(device)
                strategy.execute(device, color)
                break
        else:
            print(f"Device {device_name} not found.")

    def default_strategy(self, device):
        if "light" in device.name.lower():
            return lighting_strategy
        elif "heating" in device.name.lower():
            return heating_strategy

# Usage:
if __name__ == "__main__":
    controller = HomeController()

    living_room_heating = Device("Living Room Heating")
    kitchen_light = Device("Kitchen Light")

    controller.add_device(living_room_heating)
    controller.add_device(kitchen_light)

    heating_strategy = HeatingStrategy()
    lighting_strategy = LightingStrategy()

    user_device = input("Enter the device you want to control: ")
    decorator = ColorSelectorDecorator(controller)
    decorator.control_device(user_device)
