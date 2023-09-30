class HomeController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_controller()
        return cls._instance

    def init_controller(self):
        self.devices = []
        self.strategy = None

    def run(self):
        if self.strategy:
            self.strategy.execute(self.devices)

    def add_device(self, device):
        self.devices.append(device)

    def set_strategy(self, strategy):
        self.strategy = strategy

    def control_device(self, device_name):
        for device in self.devices:
            if device.name.lower() == device_name.lower():
                self.strategy.execute([device])
                break
        else:
            print(f"Device {device_name} not found")

class Device:
    def __init__(self, name):
        self.name = name

class HeatingStrategy:
    def execute(self, devices):
        for device in devices:
            if "heating" in device.name.lower():
                print(f"Turning on heating for {device.name}")

class LightingStrategy:
    def execute(self, devices):
        for device in devices:
            if "light" in device.name.lower():
                print(f"Turning on lights for {device.name}")


controller = HomeController()


living_room_heating = Device("Living Room Heating")
kitchen_light = Device("Kitchen Light")

controller.add_device(living_room_heating)
controller.add_device(kitchen_light)

heating_strategy = HeatingStrategy()
controller.set_strategy(heating_strategy)

lighting_strategy = LightingStrategy()
controller.set_strategy(lighting_strategy)


user_device = input("Enter the device you want to control: ")
if "heating" in user_device.lower():
    controller.set_strategy(heating_strategy)
elif "light" in user_device.lower():
    controller.set_strategy(lighting_strategy)

controller.control_device(user_device)