
def display_available_items(dct):
    print("Available Items".center(30))
    print(f"{'S.No':<15}{'Item':<15}{'Quantity':<15}{'Cost/Item':<15}")
    for index, product in dct.items():
        print(f'{index:<15}{product['Item']:<15}{product['Quantity']:<15}{product['Cost/Item']:<15}')



# main code 
availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)
# user demand 
customerName = input('Enter customer Name')
address = input('Enter Address city and state')
userDemad = {}
while 1:
    item_name = input("Enter the Item (Empty Return is No Item)")
    if item_name == '':
        break
    quantity = int(input('Enter the Quantity '))
    userDemad[item_name] = quantity
# 
usercart = availableItems.copy()
bill = 0
for user_p in userDemad:
    for index, product in availableItems.items():
        if user_p.casefold() == product['Item'].casefold():
            if userDemad[user_p] <= product['Quantity']:
                tt = userDemad[user_p] * product['Cost/Item']
                bill += tt
                usercart['Quantity'] = userDemad[user_p]
                availableItems[index]['Quantity'] -= userDemad[user_p]
                usercart['Total Cost'] = tt
            else:

                usercart.pop(index)
