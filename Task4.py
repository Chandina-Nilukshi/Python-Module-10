import random
from tabulate import tabulate

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self):
        self.current_speed += random.randint(10, 15)
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance
        return distance


car1 = Car("ABC-1", random.randint(100, 200))
car2 = Car("ABC-2", random.randint(100, 200))

while car1.travelled_distance < 10000 and car2.travelled_distance < 10000:
    if car1.current_speed < car1.maximum_speed:
        car1.accelerate()
    if car2.current_speed < car2.maximum_speed:
        car2.accelerate()
    car1.travelled_distance += car1.drive(1)
    car2.travelled_distance += car2.drive(1)


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
        self.hour = 0

    def hour_passes(self):
        self.hour += 1
        for car in self.cars:
            car.accelerate()
            car.drive(1)

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)

    def print_status(self):
        print(f"Status of the race after {self.hour} hours:")
        car_status = [[car.registration_number, car.current_speed, car.maximum_speed, car.travelled_distance] for car in self.cars]
        print(tabulate(car_status, headers=["Registration number", "Current_speed", "Maximum speed", "Travelled Distance"], tablefmt='psql'))

cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
race = Race("Grand Demolition Derby", 8000, cars)
while not race.race_finished():
    race.hour_passes()
    if race.hour % 10 == 0:
        race.print_status()

print("Race finished")
race.print_status()
