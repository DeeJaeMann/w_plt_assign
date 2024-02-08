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
        
car1 = CarManager("Jeep", "Wrangler", 2002, 30000, ['oil change', 'tire rotation'])
car2 = CarManager("Dodge", "challenger", 1970, 79000, ['tune up'])
car3 = CarManager("Chevrolet", "impala", 1995, 150000)

