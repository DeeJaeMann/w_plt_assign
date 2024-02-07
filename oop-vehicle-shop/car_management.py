#!/usr/bin/env python3.12
class CarManager:
    """Manages a collection of cars"""
    # Class Attributes
    # Stores all car instances created
    all_cars = []
    # Total number of cars
    total_cars = 0

    TPLE_MENU = (
        "Add a car",
        "View all cars",
        "View total number of cars",
        "See a car's details",
        "Service a car",
        "Update mileage",
        "Quit",
    )
    
    # Constructor
    def __init__(self, make, model, year, mileage, services = []) :
        self._id = CarManager.total_cars
        self._make = str(make).lower()
        self._model = str(model).lower()
        self._year = int(year)
        self._mileage = int(mileage)
        # Ensures our property is a list
        self._services = self.convert_services(services)

        CarManager.total_cars += 1
        self.add_car()


    def __str__(self) :
        return f"ID: {self.id} Make: {self.make} Model: {self.model} Year: {self.year} Mileage: {self.mileage} Services: {self.services}"
    
    def __repr__(self) :
        return str(self)

    # Getters and Setters

    @property
    def id(self) :
        """Getter: Returns the ID of the car (Note: This is automatically assigned. No setter)

        Args:
            None
        Returns:
            (integer) Integer of car ID
        """
        return self._id
    
    @property
    def make(self) :
        """Getter: Returns the make of the car

        Args:
            None
        Returns
            (string) Make property of car
        """
        return self._make
    
    @make.setter
    def make(self, str_make) :
        """Setter: Sets the make of the car

        Args:
            str_make - String to change the make into
        Returns:
            None
        """
        self._make = str(str_make).lower()

        self.update_cars(self._id)
    
    @property
    def model(self) :
        """Getter: Returns the model of the car

        Args:
            None
        Returns:
            (string) Model property of car 
        """
        return self._model
    
    @model.setter
    def model(self, str_model) :
        """Setter: Sets the model of the car

        Args:
            str_model - String to change the model into
        Returns:
            None
        """
        self._model = str(str_model).lower()

        self.update_cars(self._id)

    @property
    def year(self) :
        """Getter: Returns the year of the car

        Args:
            None
        Returns:
            (integer) Year property of car 
        """
        return self._year

    @year.setter
    def year(self, int_year) :
        """Setter: Sets the year of the car

        Args:
            int_year - Int to change the year into
        Returns:
            Warning on fail
        """
        if type(int_year) == int:
            self._year = int_year

            self.update_cars(self._id)
        else :
            print("Warning: Year must be an integer! Property not updated!")

    @property
    def mileage(self) :
        """Getter: Returns the mileage property

        Args:
            None
        Returns:
            (integer) Mileage of car 
        """
        return self._mileage
    
    @mileage.setter
    def mileage(self, int_mileage) :
        """Setter: Sets the mileage property
        
        Args:
            int_mileage - Integer to set mileage property to
        Returns:
            Warning on fail
        """
        if type(int_mileage) == int:
            self._mileage = int_mileage

            self.update_cars(self._id)
        else :
            print("Warning: Mileage must be an integer! Property not updated!")

    @property
    def services(self) :
        """Getter: Gets the list of services from

        Args:
            None
        Returns:
            (list) List of services
        """
        return self._services

    @services.setter
    def services(self, lst_services) :
        """Setter: Sets the services property

        Args:
            lst_services List of services to set property to
        Returns:
            None
        """
        self._services = self.convert_services(lst_services)

        self.update_cars(self._id)

    # End Getters and Setters


    def add_car(self) :
        """Helper Method: Adds new car to all_cars

        Args:
            None
        Returns:
            None
        """
        CarManager.all_cars.append({
                "id" : self._id,
                "make" : self._make,
                "model" : self._model,
                "year" : self._year,
                "mileage" : self._mileage,
                "services" : self._services
                })

    def update_cars(self, int_id) :
        """Helper Method: Updates a car in all_cars

        Args:
            int_id - Integer of car ID
        Returns:
            None
        """
        print(f"Updating Car ID {int_id}")
        CarManager.all_cars[int_id] = {
                "id" : self._id,
                "make" : self._make,
                "model" : self._model,
                "year" : self._year,
                "mileage" : self._mileage,
                "services" : self._services
                }
        
    def convert_services(self, lst_services) :
        """Validates input is a list and converts if necessary

        Args:
            lst_services - Input to validate and convert
        Returns:
            (list) Validated and converted list
        """
        #TODO: Verify how much validation/processing logic is needed
        if lst_services == [] :
            # No conversion necessary
            return lst_services
        elif type(lst_services) == list :
            # No conversion necessary
            return lst_services
        else : 
            # Create empty list
            lst_result = []
            
            # Check if our input is a string
            if type(lst_services) == str :
                # Force to lowercase
                lst_services = lst_services.lower()
            else :
                # Convert to string and lowercase
                lst_services = f"{lst_services}".lower()

            # Append our input to our list
            lst_result.append(lst_services)
            return lst_result

    # Class methods

    @classmethod
    def display_menu(cls) :
        """Displays the menu

        Args:
            None
        Returns:
            (string) Menu display
        """
        str_result = "\n---- WELCOME ----\n"

        for int_index, str_option in enumerate(CarManager.TPLE_MENU) :
            str_result += f"{int_index + 1}. {str_option}\n"

        return str_result
    
    @classmethod
    def get_menu_input(cls) :
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
            print(CarManager.display_menu())

    @classmethod
    def menu_sel_add_car(cls) :
        """Selection: Add a car
        """
        print("\n---- Add A Car ----")

    @classmethod
    def menu_sel_view_all_cars(cls) :
        """Selection: View all cars

        Args:
            None
        Returns:
            None
        """
        print("\n---- View All Cars ----")

        for str_element in CarManager.all_cars :
            str_service_list = ""

            if len(str_element['services']) > 0 :
                for int_index, str_service in enumerate(str_element['services']) :
                    str_service_list += f"{str_service.title()}"

                    if int_index < len(str_element['services']) - 1 :
                        str_service_list += ", "
            else:
                str_service_list = "None"

            print(f"ID: {str_element['id']} | \
Make: {str_element['make'].title()} | \
Model: {str_element['model'].title()} | \
Year: {str_element['year']} | \
Mileage: {str_element['mileage']} | \
Services: {str_service_list}")

        input("\nPress any key to continue...")

    @classmethod
    def menu_sel_view_total_car_num(cls) :
        """Selection: View total number of cars

        Args:
            None
        Returns:
            None
        """
        print("\n---- View Total Number of Cars ----")
        print(f"Total Cars: {CarManager.total_cars}\n")
        input("Press any key to continue...")

    @classmethod
    def menu_sel_see_car_details(cls) :
        """Selection: See a car's details
        """
        print("\n---- See A Car's Details ----")

    @classmethod
    def menu_sel_service_car(cls) :
        """Selection: Service a car
        """
        print("\n---- Service A Car ----")

    @classmethod
    def menu_sel_update_mileage(cls) :
        """Selection: Update Mileage
        """
        print("\n---- Update Mileage ----")

    @classmethod
    def run_ui(cls) :
        """Runs the user interface

        Args:
            None
        Returns:
            None
        """
        int_selection = 0

        while not(int_selection == 7) :
            print(CarManager.display_menu())
            int_selection = CarManager.get_menu_input()

            match int_selection :
                case 1:
                    CarManager.menu_sel_add_car()
                case 2:
                    CarManager.menu_sel_view_all_cars()
                case 3:
                    CarManager.menu_sel_view_total_car_num()
                case 4:
                    CarManager.menu_sel_see_car_details()
                case 5:
                    CarManager.menu_sel_service_car()
                case 6:
                    CarManager.menu_sel_update_mileage()


        print("Goodbye!")


#CarManager.menu_sel_add_car()
car1 = CarManager("Jeep", "Wrangler", 2002, 30000, ['oil change', 'tire rotation'])
car2 = CarManager("Dodge", "challenger", 1970, 79000, ['tune up'])
car3 = CarManager("Chevrolet", "impala", 1995, 150000)


CarManager.run_ui()