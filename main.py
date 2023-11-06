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

# vacuum_cleaner.py
class VacuumCleaner(Device):
    def __init__(self, name: str, plug_type: str):
        super().__init__(name)
        self.plug_type = plug_type

# adapter.py
class VacuumCleanerAdapter(Device):
    def __init__(self, vacuum_cleaner: VacuumCleaner):
        self.vacuum_cleaner = vacuum_cleaner
        super().__init__(vacuum_cleaner.name)

    def turn_on(self):
        if self.vacuum_cleaner.plug_type == "E":
            super().turn_on()
            print(f"{self.name} is now vacuuming.")
        else:
            print(f"Cannot turn on {self.name} - Incompatible plug type.")


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

    def add_vacuum_cleaner(self, vacuum_cleaner: VacuumCleaner):
        self.devices.append(vacuum_cleaner)

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

    def add_vacuum_cleaner(self, vacuum_cleaner: VacuumCleaner):
        self.devices.append(vacuum_cleaner)
        
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

    def add_vacuum_cleaner(self, vacuum_cleaner: VacuumCleaner):
        self.devices.append(vacuum_cleaner)

    def control_vacuum_cleaner(self, device_name):
        device_name_lower = device_name.lower()
        vacuum_cleaner = None
        for device in self.devices:
            if isinstance(device, VacuumCleaner) and device.name.lower() == device_name_lower:
                vacuum_cleaner = device
                break

        if vacuum_cleaner is not None:
            plug_type = input(f"Enter the plug type for {vacuum_cleaner.name} (E for compatible, other for adapter): ")
            if plug_type.lower() == "e":
                vacuum_cleaner.turn_on()
                print(f"{vacuum_cleaner.name} is now vacuuming with E plug type.")
            else:
                adapter = VacuumCleanerAdapter(vacuum_cleaner)
                adapter.turn_on()
                print(f"{vacuum_cleaner.name} is now vacuuming with an adapter because of the incompatible plug type.")
        else:
            print(f"Device {device_name} not found.")

if __name__ == "__main__":
    controller = HomeController()

    living_room_heating = Device("Living Room Heating")
    kitchen_light = Device("Kitchen Light")
    vacuum_cleaner = VacuumCleaner("Vacuum Cleaner", "E") 

    controller.add_device(living_room_heating)
    controller.add_device(kitchen_light)
    controller.add_vacuum_cleaner(vacuum_cleaner)

    heating_strategy = HeatingStrategy()
    lighting_strategy = LightingStrategy()

    user_device = input("Enter the device you want to control: ")

    if user_device.lower() == "vacuum cleaner":
        controller.control_vacuum_cleaner(user_device)
    else:
        decorator = ColorSelectorDecorator(controller)
        decorator.control_device(user_device)
