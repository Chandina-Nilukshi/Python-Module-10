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

elevator = Elevator(1, 10)
elevator.go_to_floor(7)
elevator.go_to_floor(1)

