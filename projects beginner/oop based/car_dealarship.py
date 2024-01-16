# car class 

class car:
    def __init__(self, maker, name, model, year, price):
        self.maker = maker
        self.name = name
        self.model = model
        self.year = year 
        self.price = price
        self.available = True
    def display_car(self):
        return f'''Maker: {self.maker}
Car Name: {self.name}
Model: {self.model}
Year: {self.year}
Price: {self.price}'''
    
class dealarship:
    def __init__(self, dealar):
        self.dealar = dealar
        self.inventory = []
    def add_car_to_inventory(self, car):
        self.inventory.append(car)

    def display_availableCar(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(count)
                print(car.display_car())
                print()
                count += 1
    def sell_car(self, customer, index_car):
        if 0 < index_car <= len(self.inventory):
            if self.inventory[index_car-1].available:
                customer.purchase(self.inventory[index_car-1])
                return self.inventory[index_car-1]


class customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.purchased_car = []

    def purchase(self, car):
         self.purchased_car.append(car)
         car.available = False


# driven Code 
car1 = car('Honda', 'Honda City', 'S4', 2018, 12000000)
car2 = car('Hyundai', 'Creta', 'Kinght Edition', 2023, 2000000)
car3 = car('Tata', 'Nano', 'Zero', 2012, 122000)

d1 = dealarship('ABC Motors')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)

d1.display_availableCar()
customer1 = customer('Ravi')

purchasedCar = d1.sell_car(customer1, 3)
if purchasedCar:
    print(f'{customer1.customer_name}\npurchased {purchasedCar.display_car()}\n\n')
else:
    print('Not able to purchase')
print("After Selling Available cars")
d1.display_availableCar()