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
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services

        CarManager.total_cars += 1
        CarManager.all_cars.append({
                "id" : self._id,
                "make" : self._make,
                "model" : self._model,
                "year" : self._year,
                "mileage" : self._mileage,
                "services" : self._services
                })

    def __str__(self) :
        return f"ID: {self._id} Make: {self._make} Model: {self._model} Year: {self._year} Mileage: {self._mileage} Services: {self._services}"
    
    def __repr__(self) :
        return str(self)



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

print(car1)

car2 = CarManager("Chevy", "Camaro", 1969, 90000)

print(car2)

print(CarManager.all_cars)
# print(CarManager.total_cars)