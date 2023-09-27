import csv
from datetime import datetime


class CarPark:
    def __init__(self, num_spaces = 6):
        self.num_spaces = num_spaces
        self.available_spaces = num_spaces
        self.occupied_spaces = {}
        self.records = []
        
    def enter(self, vehicle_id):
        if vehicle_id in self.occupied_spaces:
            print("Vehicle already in parking!!")
        else:
            if self.available_spaces > 0:
                self.occupied_spaces[vehicle_id] = {
                   'entry_time': datetime.now(),
                   'space_id': self.num_spaces - self.available_spaces + 1
                    }
                self.available_spaces -= 1
                self.save_record(vehicle_id, self.occupied_spaces[vehicle_id]['entry_time'], None,
                             self.occupied_spaces[vehicle_id]['space_id'], None)
                return vehicle_id, self.occupied_spaces[vehicle_id]['space_id'],self.occupied_spaces[vehicle_id]['entry_time'], self.available_spaces
            else:
                print("Sorry, the car park is full.")

    def exit(self, vehicle_id):
        if vehicle_id in self.occupied_spaces:
            entry_time = self.occupied_spaces[vehicle_id]['entry_time']
            exit_time = datetime.now()
            space_id = self.occupied_spaces[vehicle_id]['space_id']
            fare = self.calculate_fare(entry_time, exit_time)
            self.available_spaces += 1
            self.save_record(vehicle_id, entry_time, exit_time, space_id, fare)
            return vehicle_id, self.occupied_spaces[vehicle_id]['space_id'],entry_time, exit_time, fare, self.available_spaces
        else:
            print(f"Vehicle {vehicle_id} is not in the car park.")
        del self.occupied_spaces[vehicle_id]
    def enquire(self, vehicle_id):
        if vehicle_id in self.occupied_spaces:
            entry_time = self.occupied_spaces[vehicle_id]['entry_time']
            space_id = self.occupied_spaces[vehicle_id]['space_id']
            return vehicle_id, space_id, entry_time
        else:
            print(f"Vehicle {vehicle_id} is not in the car park.")
    def calculate_fare(self, entry_time, exit_time):
        duration = exit_time - entry_time
        hours = duration.total_seconds() / 3600
        return hours*2

    def save_record(self, vehicle_id, entry_time, exit_time, space_id, fare):
        record = [vehicle_id, entry_time, exit_time, space_id, fare]
        self.records.append(record)
        with open('car_park_record.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(record)
car_park = CarPark(6)