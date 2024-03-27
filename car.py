class Car:
    # make = None
    # model = None
    # year = None
    # color = None
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.year}"
    
    def read_odoneter(self):
        return f"Car has {self.odometer_reading} miles on it."