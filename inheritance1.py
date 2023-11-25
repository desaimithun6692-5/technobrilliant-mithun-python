class Vehical:

    def __init__(self, colour, rto_no):
        self.colour = colour
        self.rto_no = rto_no

    def get_colour(self):
        print(f"colour is {self.colour}")

    def get_rto_no(self):
        print(f"colour is {self.rto_no}")

    def get_all_details(self):
        self.get_colour()
        self.get_rto_no()


class Car(Vehical):

    def __init__(self, colour, rto_no, car_type, gear_type, fuel_type):
        super(Car, self).__init__(colour, rto_no)
        self.car_type = car_type
        self.gear_type = gear_type
        self.fuel_type = fuel_type

    def get_car_type(self):
        print(f"colour is {self.car_type}")

    def get_gear_type(self):
        print(f"colour is {self.gear_type}")

    def get_fuel_type(self):
        print(f"colour is {self.fuel_type}")

    def get_all_details(self):
        super(Car,self).get_all_details()
        self.get_car_type()
        self.get_gear_type()
        self.get_fuel_type()


class bike(Vehical):

    def __init__(self, colour, rto_no, bike_name, bike_type):
        super(bike, self).__init__(colour, rto_no)
        self.bike_name = bike_name
        self.bike_type = bike_type

    def get_bike_name(self):
        print(f"colour is {self.bike_name}")

    def get_bike_type(self):
        print(f"colour is {self.bike_type}")


# c = Car("red", "MH-100", "SUV", "manual", "petrol")
# c.get_rto_no()
# c.get_colour()
# c.get_fuel_type()
#
# v =  Vehical("red","MH-102")
# v.get_colour()
# v.get_rto_no()
#
#
# b =  bike("blue", "MH-103","Activa","mopaid")
# b.get_rto_no()
# b.get_colour()
# b.get_bike_name()
#


c = Car("red", "MH-100", "SUV", "manual", "petrol")
c.get_all_details()
