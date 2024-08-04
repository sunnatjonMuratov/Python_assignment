from restaurant import Restaurant
from staff import Staff
from customer import Customer
from restaurant import Restaurant, Table

tables = [Table(1, 4), Table(2, 6), Table(3, 2)]  # Add more tables as needed
restaurant = Restaurant("Awesome Restaurant", tables)
staff = Staff(restaurant)
customer = Customer(restaurant)

while True:
    role = input(f"\n\n\nAre you staff or Customer? (1 - Customer; 2 - Staff): ")
    if not role.isdigit():
        print("faqat raqam kiriting!")
        continue
    if int(role) == 1:
        while True:
            action_num = int(input(
                f"\nChoose one of the actions: \n1. View the menu \n2. Make a reservation \n3. View reservation \n4. View the information of Restaurant\n0. Exit \n-> "))
            if action_num == 1:
                customer.show_menu()
            elif action_num == 2:
                customer.make_reservation()
            elif action_num == 3:
                customer.show_reservation()
            elif action_num == 4:
                print(restaurant.restaurant_info)
            elif action_num == 0:
                break
            elif action_num >= 5:
                print('There is no such action!!!')
            else:
                print('There is no such action!!!')
    elif int(role) == 2:
        name_surname = staff.make_reservation_name()
        if name_surname not in restaurant.staff_members:
            print("There is no such worker!!!")
        else:
            while True:
                action_num = int(input(
                    '\nChoose one of the actions: \n1. View the menu \n2. Add food \n3. Update food \n4. Remove food \n5. Update reservation \n6. Delete reservation \n7. Show reservation \n8. Show all reservations \n9. View the information of Restaurant \n0. Exit \n-> '))
                if action_num == 1:
                    staff.show_menu()
                elif action_num == 2:
                    staff.add_new_food()
                elif action_num == 3:
                    staff.update_food()
                elif action_num == 4:
                    staff.remove_food()
                elif action_num == 5:
                    staff.update_reservation()
                elif action_num == 6:
                    staff.remove_reservation()
                elif action_num == 7:
                    staff.show_reservation()
                elif action_num == 8:
                    staff.show_all_reservation()
                elif action_num == 9:
                    print(restaurant.restaurant_info)
                elif action_num == 0:
                    break
                else:
                    print('There is no such action!!!')
    elif int(role) >= 3:
        print("There is no such action!")
    else:
        break
