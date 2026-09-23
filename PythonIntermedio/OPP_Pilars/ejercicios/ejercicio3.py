class LandVehicle:
    def __init__(self, max_speed_land):
        self.max_speed_land = max_speed_land

    def drive(self):
        return f"Driving at {self.max_speed_land} km/h on land"

class WaterVehicle:
    def __init__(self, max_speed_water):
            self.max_speed_water = max_speed_water
    
    def sail(self):
        return f"Sailing at {self.max_speed_water} km/h on water"

class AmphibiousCar(LandVehicle, WaterVehicle):
    def __init__(self, max_speed_land, max_speed_water):
        LandVehicle.__init__(self, max_speed_land)
        WaterVehicle.__init__(self, max_speed_water)

    def transition_mode(self):
        if self.max_speed_land > self.max_speed_water:
            return "Switching to land mode — faster on land"
        elif self.max_speed_water > self.max_speed_land:
            return "Switching to water mode — faster on water"
        else:
            return "Both modes have the same top speed"


car = AmphibiousCar(max_speed_land=120, max_speed_water=60)

print(car.drive())
print(car.sail())
print(car.transition_mode())

print(car.max_speed_land)
print(car.max_speed_water)