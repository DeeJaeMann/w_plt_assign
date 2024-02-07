#!/usr/bin/env python3.12
class CarManager:
    """Manages a collection of cars"""
    # Class Attributes
    # Stores all car instances created
    all_cars = []
    # Total number of cars
    total_cars = 0
    
    # Constructor
    def __init__(self, id, make, model, year, mileage, services) :
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services

        CarManager.total_cars += 1

    # Methods
    def display_menu(self) :
        print("\n----  WELCOME  ----\n\
1. Add a car\n\
2. View all cars\n\
3. View total number of cars\n\
4. See a car's details\n\
5. Service a car\n\
6. Update mileage\n\
7. Quit\n")
        
car1 = CarManager(1, "Dodge", "Charger", 1978, 50000, "None")

car1.display_menu()