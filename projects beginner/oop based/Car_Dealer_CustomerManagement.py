class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.available = True

    def display_info(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"


class Dealership:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_car_to_inventory(self, car):
        self.inventory.append(car)

    def display_available_cars(self):
        available_cars = [car.display_info() for car in self.inventory if car.available]
        return "Available Cars:\n" + "\n".join(available_cars)

    def sell_car(self, customer, car_index):
        if 0 <= car_index < len(self.inventory) and self.inventory[car_index].available:
            car = self.inventory.pop(car_index)
            customer.purchase_car(car)
            return car
        else:
            return None


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_cars = []

    def purchase_car(self, car):
        self.purchased_cars.append(car)
        car.available = False


# Example usage:
car1 = Car("Toyota", "Camry", 2022, 25000)
car2 = Car("Honda", "Civic", 2021, 22000)
car3 = Car("Ford", "Mustang", 2023, 35000)

dealership = Dealership("ABC Motors")
dealership.add_car_to_inventory(car1)
dealership.add_car_to_inventory(car2)
dealership.add_car_to_inventory(car3)

customer1 = Customer("John Doe")

print(dealership.display_available_cars())

# Simulate a customer purchase
purchased_car = dealership.sell_car(customer1, 1)

if purchased_car:
    print(f"{customer1.name} purchased: {purchased_car.display_info()}")
else:
    print("Invalid car index or car not available")

print(dealership.display_available_cars())
