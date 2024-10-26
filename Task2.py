class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):

        if floor < self.current_floor:
            def floor_down():
                print(f"Elevator at floor {self.current_floor} moving to floor {floor}")
                while self.current_floor != floor:
                    self.current_floor -= 1
                    print(f"Elevator at floor {self.current_floor}")
            floor_down()

        elif floor > self.current_floor:
            def floor_up():
                print(f"Elevator at floor {self.current_floor} moving to floor {floor}")
                while self.current_floor != floor:
                    self.current_floor += 1
                    print(f"Elevator at floor {self.current_floor}")
            floor_up()

class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for i in range(elevators)]

    def run_elevator(self, number, destination):
        if number < 0 or number >= len(self.elevators):
            print("Elevator number out of range")
            return
        print(f"Elevator {number} going to floor {destination}")
        self.elevators[number].go_to_floor(destination)

building = Building(1, 10, 5)
building.run_elevator(4, 10)


