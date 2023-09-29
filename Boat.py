'''In This we are trying to make working of a boat'''

import math
import time



class Boat:
    def __init__(self, name: str, capacity: int, speed: float, location: tuple, heading: float, status: str):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.location = location
        self.heading = heading
        self.status = status
        self.last_update_time = time.time()
        self.last_update_location = location

    def set_name(self, name: str) -> None:
        self.name = name

    def set_capacity(self, capacity: int) -> None:
        self.capacity = capacity

    def set_speed(self, speed: float) -> None:
        self.speed = speed

    def set_location(self, latitude: float, longitude: float) -> None:
        # Calculate the distance between the current location and the last updated location
        distance = math.sqrt((latitude - self.last_update_location[0]) ** 2 + (longitude - self.last_update_location[1]) ** 2)

        # Check if the boat has moved a certain distance or if a certain time interval has passed since the last update
        if distance >= 0.1 or time.time() - self.last_update_time >= 60:
            # Update the last update time and location
            self.last_update_time = time.time()
            self.last_update_location = (latitude, longitude)

    def set_heading(self, heading: float) -> None:
        self.heading = heading

    def set_status(self, status: str) -> None:
        self.status = status

    def get_properties(self) -> dict:
        return {
            "name": self.name,
            "capacity": self.capacity,
            "speed": self.speed,
            "location": self.location,
            "heading": self.heading,
            "status": self.status
        }

# Create a list of Boat objects
boats = [
    Boat("Boat 1", 10, 20, (0, 0), 0, "Docked"),
    Boat("Boat 2", 20, 30, (0, 0), 0, "Docked"),
    Boat("Boat 3", 30, 40, (0, 0), 0, "Docked")
]

# Update the location of each boat
for boat in boats:
    boat.set_location(10, 20)

# Print the properties of each boat
for boat in boats:
    print(boat.get_properties())