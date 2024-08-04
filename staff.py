from restaurant import Meal, Reservation, Restaurant
# import restaurant

class Staff:
    def __init__(self, restaurant):
        self.restaurant = restaurant


    def make_reservation_name(self):
        return input("Enter staff member's name: ")

    def show_menu(self):
        self.restaurant.display_menu()

    def add_new_food(self):
        meal_name = input("Enter the name of the new meal: ")
        meal_price = float(input("Enter the price of the new meal: "))
        new_meal = Meal(meal_name, meal_price)
        self.restaurant.menu[len(self.restaurant.menu)+1] = new_meal
        print(f"New meal added: {new_meal.name} - ${new_meal.price}")

    def update_food(self):
        meal_id = input("Enter the ID of the meal to update: ")
        meal = self.restaurant.menu.get(meal_id)
        
        if meal:
            new_name = input("Enter the new name for the meal: ")
            new_price = float(input("Enter the new price for the meal: "))
            
            meal.name = new_name
            meal.price = new_price
            
            print(f"Meal {meal_id} updated successfully.")
        else:
            print(f"Meal with ID {meal_id} not found.")

    def remove_food(self):
        meal_id = input("Enter the ID of the meal to remove: ")
        meal = self.restaurant.menu(meal_id)
        
        if meal:
            del self.restaurant.menu[meal_id]
            print(f"Meal {meal_id} removed successfully.")
        else:
            print(f"Meal with ID {meal_id} not found.")

    def update_reservation(self):
        reservation_id = int(input("Enter the ID of the reservation to update: "))
        reservation = next((r for r in self.restaurant.reservations if r.reservation_id == reservation_id), None)

        if reservation:
            table_number = int(input("Enter the new table number: "))
            meal_choices = input("Enter the new meal choices (comma-separated): ").split(',')
            date_time = input("Enter the new date and time: ")

            new_table = next((t for t in self.restaurant.tables if t.table_number == table_number and not t.reservation), None)

            if new_table:
                reservation.table.reservation = None
                new_reservation = Reservation(reservation_id, new_table, meal_choices, date_time)
                new_table.reservation = new_reservation
                self.restaurant.reservations.remove(reservation)
                self.restaurant.reservations.append(new_reservation)
                print(f"Reservation {reservation_id} updated successfully.")
            else:
                print("New table not available for reservation.")
        else:
            print(f"Reservation with ID {reservation_id} not found.")

    def remove_reservation(self):
        reservation_id = int(input("Enter the ID of the reservation to remove: "))
        reservation = next((r for r in self.restaurant.reservations if r.reservation_id == reservation_id), None)

        if reservation:
            reservation.table.reservation = None
            self.restaurant.reservations.remove(reservation)
            print(f"Reservation {reservation_id} removed successfully.")
        else:
            print(f"Reservation with ID {reservation_id} not found.")

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

    def show_all_reservation(self):
        for reservation in self.restaurant.reservations:
            print(f"Reservation ID: {reservation.reservation_id}, Table Number: {reservation.table.table_number}")
