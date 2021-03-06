class Car():
    #initializing all variable within this init method
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 125 # as this value if defined here we need not it to be included as parameter

    #describe all methods like this one
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+ " miles on it")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:# using self is a must
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car("audi",'a4',2016) #Instance
my_new_car.model = "z35"
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 12544 #1. modify attib value directly
my_new_car.read_odometer()

my_new_car.update_odometer(28876) #2. modification using method
my_new_car.read_odometer()

my_new_car.increment_odometer(1) #3. incrementing attrib value through method
my_new_car.read_odometer()

my_used_car = Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()