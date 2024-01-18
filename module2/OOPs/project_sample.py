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
Name: {self.name}
Model: {self.model}
YOM: {self.year}
On Road Price: {self.price}'''
    
class dealership:
    def __init__(self, dealer_name):
        self.dealer_name = dealer_name
        self.inventory = []
    def add_car_to_inventory(self, car):
        self.inventory.append(car)
    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(count)
                print(car.display_car())
                print("-----------\n")
                count += 1

    def sell_car(self, customer, index):
        if 0 < index <= len(self.inventory) and self.inventory[index-1].available:
            customer.purchase(self.inventory[index-1])
            return self.inventory[index-1]
class customer:
    def __init__(self, cname):
        self.cname = cname
        self.purchased_car = []
    def purchase(self, car):
        self.purchased_car.append(car)
        car.available = False



# main code or driver code 
car1 = car('Honda', 'HondaCity', 'S4', 2018, 14000000)
car2 = car('Hyundai', 'Creta', 'KnightEdition', 2023, 2200000)
car3 = car('Tata', 'Nano', 'Zero', 2014, 114300)

d1 = dealership('ABC Motors')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)
d1.display_available_car()
name = input('Enter Customer1 Name ')
index = int(input(f'Enter the car index [1-{len(d1.inventory)}]'))
c1 = customer(name)
purchased_car = d1.sell_car(c1, index)
if purchased_car:
    print(f'{c1.cname} purchased Car\n{purchased_car.display_car()}')
else:
    print('Car is not available ')

d1.display_available_car() 