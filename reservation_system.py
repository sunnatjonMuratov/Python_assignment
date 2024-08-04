import csv
from datetime import datetime

class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def load_reservations(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                self.reservations = list(reader)
        except FileNotFoundError:
            self.reservations = []

    def save_reservations(self, filename):
        with open(filename, mode='w') as file:
            writer = csv.writer(file)
            writer.writerows(self.reservations)

    def add_reservation(self, name, date, time, guests):
        self.reservations.append([name, date, time, guests])

    def list_reservations(self):
        return self.reservations

    def run(self):
        print("Running the reservation system...")
        # Code to handle interaction, e.g., loading HTML, form submission, etc.
