#!/usr/bin/env python3.12
class CarManager:
    """Manages a collection of cars"""
    # Class Attributes
    # Stores all car instances created
    all_cars = []
    # Total number of cars
    total_cars = 0
    
    # Constructor
    def __init__(self, make, model, year, mileage, services = []) :
        self._id = CarManager.total_cars
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage
        self._services = services

        CarManager.total_cars += 1
        self.add_car()


    def __str__(self) :
        return f"ID: {self._id} Make: {self.make} Model: {self.model} Year: {self.year} Mileage: {self._mileage} Services: {self._services}"
    
    def __repr__(self) :
        return str(self)

    @property
    def id(self) :
        """Getter: Returns the ID of the car (Note: This is automatically assigned. No setter)

        Args:
            None
        Returns:
            self._id - Integer of car ID
        """
        return self._id
    
    @property
    def make(self) :
        """Getter: Returns the make of the car

        Args:
            None
        Returns
            self._make - Make property of car
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
    
    @property
    def model(self) :
        """Getter: Returns the model of the car

        Args:
            None
        Returns:
            self._model - Model property of car
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

    @property
    def year(self) :
        """Getter: Returns the year of the car

        Args:
            None
        Returns:
            self._year - Year property of car
        """
        return self._year

    @year.setter
    def year(self, int_year) :
        """Setter: Sets the year of the car

        Args:
            int_year - Int to change the year into
        Returns:
            None
        """
        if type(int_year) == int:
            self._year = int_year
        else :
            print("Year must be an int!  Property not updated!")


    def add_car(self) :
        """Helper Method: Adds new car to all_cars

        Args:
            None
        Returns:
            None
        """
        CarManager.all_cars.append({
                "id" : self.id,
                "make" : self.make,
                "model" : self.model,
                "year" : self.year,
                "mileage" : self._mileage,
                "services" : self._services
                })

    def update_cars(self, int_id) :
        """Helper Method: Updates a car in all_cars

        Args:
            id - Integer of car ID
        Returns:
            None
        """
        CarManager.all_cars[int_id] = {
                "id" : self._id,
                "make" : self.make,
                "model" : self._model,
                "year" : self._year,
                "mileage" : self._mileage,
                "services" : self._services
                }

    def display_menu(self) :
        """Displays the menu

        Args:
            None
        Returns:
            Menu display
        """
        print("\n----  WELCOME  ----\n\
1. Add a car\n\
2. View all cars\n\
3. View total number of cars\n\
4. See a car's details\n\
5. Service a car\n\
6. Update mileage\n\
7. Quit\n")

    def get_input(self) :
        pass



car1 = CarManager("Dodge", "Charger", 1978, 50000)

# print(car1)

# car1.make = "Jeep"

# print(car1)

car2 = CarManager("Chevy", "Camaro", 1969, 90000)

# print(car2)



print(CarManager.all_cars)
# # print(CarManager.total_cars)