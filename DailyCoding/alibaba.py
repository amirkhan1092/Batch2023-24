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
    
class dealership:
    def __init__(self, name) -> None:
        self.name = name
        self.inventory = []

    def add_car_to_inventory(self, car):
        self.inventory.append(car)

    def display_available_car(self):
        count = 1
        for car in self.inventory:
            if car.available:
                print(count)
                print(car.display_car())
                print('------\n')
                count += 1
    def sell_car(self, c, index):
        if 0 < index <= len(self.inventory) and self.inventory[index-1].available:
            c.purchase(self.inventory[index-1])
            return self.inventory[index-1]
        



class customer:
    def __init__(self, name):
        self.name = name
        self.purchased_car = []
    def purchase(self, car):
        self.purchased_car.append(car)
        car.available = False




# main code 
car1 = car('Hyundai', 'Creta', 'KnightEdition', 2023, 1800000)
car2 = car('BMW', 'Competition', 'M3', 2017, 300000000)
car3 = car('Tata', 'Nano', 'Zero', 2012, 114000)

d1 = dealership('Varshney Motors')
d1.add_car_to_inventory(car1)
d1.add_car_to_inventory(car2)
d1.add_car_to_inventory(car3)

d1.display_available_car()
cname = input('Enter the customer name: ')
cnum = int(input(f'Enter the car number [1-{len(d1.inventory)}] '))
c1 = customer(cname)
ret = d1.sell_car(c1, cnum)
if ret:
    print(f'{c1.name} purchased car\n{ret.display_car()}')
else:
    print('Car is not available ')

print('\nAfter selling available cars')
d1.display_available_car()