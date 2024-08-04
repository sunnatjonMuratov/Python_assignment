class Meal:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.reservation = None


class Reservation:
    def __init__(self, reservation_id, table, meals, date_time):
        self.reservation_id = reservation_id
        self.table = table
        self.meals = meals
        self.date_time = date_time


class Restaurant:
    staff_members = ['Leo']
    menu = {
            "1": Meal("Pie", 12),
            "2": Meal("Edana Kabab", 20),
            "3": Meal("Pizza", 10),
            "4": Meal("Tea", 2),
    }

    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self.reservations = []

    def display_menu(self):

        print("Menu:")
        for key, meal in self.menu.items():
            print(f"{key}. {meal.name} - ${meal.price}")

    def make_reservation(self, table_number, meal_choices, date_time):
        table = next((t for t in self.tables if t.table_number == table_number and not t.reservation), None)

        if table:
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(reservation_id, table, meal_choices, date_time)
            table.reservation = reservation
            self.reservations.append(reservation)
            print(f"Reservation successful! Reservation ID: {reservation_id}")
        else:
            print("Table not available for reservation.")

    def cancel_reservation(self, reservation_id):
        reservation = next((r for r in self.reservations if r.reservation_id == reservation_id), None)

        if reservation:
            reservation.table.reservation = None
            self.reservations.remove(reservation)
            print("Reservation canceled successfully.")
        else:
            print("Reservation not found.")

    def display_tables(self):
        print("Tables:")
        for table in self.tables:
            if table.reservation:
                print(f"Table {table.table_number} - Reserved")
            else:
                print(f"Table {table.table_number} - Available")

    @property
    def restaurant_info(self):
        return f"Restaurant: {self.name}, Tables: {len(self.tables)}"


# Additional code for staff members and requests can be added here
