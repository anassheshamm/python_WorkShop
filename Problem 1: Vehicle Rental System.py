class vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, vehicle_id, vehicle_type, rental_rate):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.vehicle_type = vehicle_type
        self.rental_rate = rental_rate
        self.is_available = False # True if available for rent
        

    def rent_vehicle(self):
        if not self.is_available:  # Vehicle is already rented
            print(f"{self.brand} {self.model} is already rented")
        else:
            self.is_available = False
            print(f"{self.brand} {self.model} has been rented")

    def return_vehicle(self):
        if self.is_available:  # Vehicle was not rented
            print("Vehicle was not rented")
        else:
            self.is_available = True
            print(f"{self.brand} {self.model} has been returned")

    def calculate_rental_cost(self, days):
        return self.rental_rate * days
    
    def get_details(self):
        availability = "Available" if self.is_available else "Rented"
        return f"ID: {self.vehicle_id}, Type: {self.vehicle_type}, Rate: ${self.rental_rate}/day, Status: {availability}"
    

class Car(vehicle):
    def __init__(self, brand, model, vehicle_id, rental_rate, num_doors):
        super().__init__(brand, model, vehicle_id, "Car", rental_rate)
        self.num_doors = num_doors
        self.multiplier = 1.0

    def calculate_rental_cost(self, days):
        return self.rental_rate * days * self.multiplier
    
    def get_details(self):
        availability = "Avilabile" if self.is_available else "Rented"
        return f"Car - {self.brand} {self.model} {self.num_doors} doors - ID {self.vehicle_id} - ${self.rental_rate}/day - {availability}"
        
class bike(vehicle):
    def __init__(self, brand, model, vehicle_id, rental_rate, engine_cc):
        super().__init__(brand, model, vehicle_id,  rental_rate, "Bike")
        self.engine_cc = engine_cc
        self.multiplier = 0.7

    def calculate_rental_cost(self, days):
        return self.rental_rate * days * self.multiplier
    
    def get_details(self):
        availability = "Avilabile" if self.is_available else "Rented"
        return f"Bike - {self.brand} {self.model} {self.engine_cc}cc - ID {self.vehicle_id} - ${self.rental_rate}/day - {availability}"

class truck(vehicle):
    def __init__(self, brand, model, vehicle_id, rental_rate,cargo_capacity_tons):
        super().__init__(brand, model, vehicle_id, 'truck',rental_rate)
        self.cargo_capacity_tons = cargo_capacity_tons
        self.multiplier = 1.5

    def calculate_rental_cost(self, days):
        return self.rental_rate * days * self.multiplier
    
    def get_details(self):
        availability = "Avilabile" if self.is_available else "Rented"
        return f"Truck - {self.brand} {self.model} {self.cargo_capacity_tons} tons - ID {self.vehicle_id} - ${self.rental_rate}/day - {availability}"


# Create some vehicles
car1 = Car("Toyota", "Camry", "C001", 50, 4)
bike1 = bike("Yamaha", "R3", "B001", 30, 321)
truck1 = truck("Volvo", "FH16", "T001", 120, 10)

# Show initial details
print("\n=== Vehicle Details ===")
print(car1.get_details())
print(bike1.get_details())
print(truck1.get_details())

# Rent a car
print("\n=== Renting Car ===")
car1.rent_vehicle()
print(car1.get_details())

# Try renting it again (should show already rented)
car1.rent_vehicle()

# Return the car
print("\n=== Returning Car ===")
car1.return_vehicle()
print(car1.get_details())

# Calculate rental costs
print("\n=== Rental Cost ===")
print(f"Car cost for 5 days: ${car1.calculate_rental_cost(5)}")
print(f"Bike cost for 3 days: ${bike1.calculate_rental_cost(3)}")
print(f"Truck cost for 2 days: ${truck1.calculate_rental_cost(2)}")

# Show total vehicles created
print(f"\nTotal vehicles created: {vehicle.total_vehicles}")