#!/usr/bin/env python3.12
from car_management import CarManager

TPLE_MENU = (
    "Add a car",
    "View all cars",
    "View total number of cars",
    "See a car's details",
    "Service a car",
    "Update mileage",
    "Quit",
)

def display_menu():
    """Displays the menu

    Args:
        None
    Returns:
        (string) Menu display
    """
    str_result = "\n---- WELCOME ----\n"

    for int_index, str_option in enumerate(TPLE_MENU) :
        str_result += f"{int_index + 1}. {str_option}\n"

    return str_result

def get_menu_input():
    """Displays the input prompt and receives user input

    Args:
        None
    Returns:

    """
    bl_valid = False

    while bl_valid == False :
        int_result = input("Please enter a menu option: ")

        if int_result.isnumeric() :
            int_result = int(int_result)
            if 0 < int_result < 8 :
                # We have a valid option
                return int_result

        print("Please enter a valid option from the menu.")
        print(display_menu())

def sel_any_key() :
    """Generates Select any key to continue prompt
    
    Args:
        None
    Returns:
        None
    """
    input("Press any key to continue...")

def format_service_list(lst_services) :
    """Formats the services list

    Args:
        lst_services List of services
    Returns:
        (string) Formatted list of services
    """
    str_service_list = ""

    if len(lst_services) > 0 :
        for int_index, str_service in enumerate(lst_services) :
            str_service_list += f"{str_service.title()}"

            # If there are more elements left, append a comma
            if int_index < len(lst_services) - 1 :
                str_service_list += ", "
    else:
        str_service_list = "None"

    return str_service_list

def format_all_car_output() :
    """Formats CarManager.all_cars for pretty output
    
    Args:
        None
    Returns:
        (string) Formatted output
    """
    str_output = ""

    for str_element in CarManager.all_cars :
        str_service_list = format_service_list(str_element['services'])

        str_output += f"ID: {str_element['id']} | \
Make: {str_element['make'].title()} | \
Model: {str_element['model'].title()} | \
Year: {str_element['year']} | \
Mileage: {str_element['mileage']} | \
Services: {str_service_list}\n" 
    
    return str_output

# Menu Selections
    
def menu_sel_add_car() :
    """Selection: Add a car
    """
    print("\n---- Add A Car ----")

    str_model_in = input("Model: ")
    str_make_in = input("Make: ")
    str_year_in = input("Year: ")
    # str_mileage_in

def menu_sel_view_all_cars() :
    """Selection: View all cars

    Args:
        None
    Returns:
        None
    """
    print("\n---- View All Cars ----")

    # print(f"{CarManager.all_cars}")
    print(format_all_car_output())
    
def menu_sel_view_total_car_num() :
    """Selection: View total number of cars

    Args:
        None
    Returns:
        None
    """
    print("\n---- View Total Number of Cars ----")
    print(f"Total Cars: {CarManager.total_cars}\n")

def menu_sel_see_car_details() :
    """Selection: See a car's details
    """
    print("\n---- See A Car's Details ----")
    # List ID options to choose from

def menu_sel_service_car() :
    """Selection: Service a car
    """
    print("\n---- Service A Car ----")

def menu_sel_update_mileage() :
    """Selection: Update Mileage
    """
    print("\n---- Update Mileage ----")

def process_menu_input(int_selection) :
    """Takes user input and executes menu selection

    Args:
        int_selection - Integer of menu choice
    Returns:
        None
    """
    
    match int_selection :
        case 1:
            menu_sel_add_car()
        case 2:
            menu_sel_view_all_cars()
        case 3:
            menu_sel_view_total_car_num()
        case 4:
            menu_sel_see_car_details()
        case 5:
            menu_sel_service_car()
        case 6:
            menu_sel_update_mileage()

def run_ui() :
    """Runs the user interface

    Args:
        None
    Returns:
        None
    """
    int_selection = 0

    while int_selection != 7:
        print(display_menu())
        int_selection = get_menu_input()
        process_menu_input(int_selection)

        # We do not need the 'any key' prompt if we quit
        if int_selection != 7:
            sel_any_key()

    
    print("Goodbye!")

run_ui()