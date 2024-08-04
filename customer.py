from restaurant import Meal, Reservation

class Customer:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def show_menu(self):
        self.restaurant.display_menu()

    def make_reservation(self):
        table_number = int(input("Enter the table number for the reservation: "))
        meal_choices = input("Enter the meal choices (comma-separated): ").split(',')
        date_time = input("Enter the date and time for the reservation(e.g. 02.2.2024): ")

        self.restaurant.make_reservation(table_number, meal_choices, date_time)

    def show_reservation(self):
        reservation_id = int(input("Enter the ID of the reservation to show: "))
        reservation = next((r for r in self.restaurant.reservations if r.reservation_id == reservation_id), None)

        if reservation:
            print(f"Reservation ID: {reservation.reservation_id}")
            print(f"Table Number: {reservation.table.table_number}")
            print(f"Meals: {', '.join(reservation.meals)}")
            print(f"Date and Time: {reservation.date_time}")
        else:
            print(f"Reservation with ID {reservation_id} not found.")

    def send_request(self):
        # Implement code to send a request
        pass


    def make_reservation_name(self):
        return input("Enter customer's name and surname: ")
