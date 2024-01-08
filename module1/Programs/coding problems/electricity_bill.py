# Input the electricity unit charges
unit_charges = float(input("Enter the electricity unit charges: "))

# Initialize variables to store the total bill and surcharge
total_bill = 0
surcharge_percentage = 20  # 20% surcharge

# Calculate the bill based on the given conditions
if unit_charges <= 50:
    total_bill = unit_charges * 0.50
elif unit_charges <= 150:
    total_bill = (50 * 0.50) + ((unit_charges - 50) * 0.75)
elif unit_charges <= 250:
    total_bill = (50 * 0.50) + (100 * 0.75) + ((unit_charges - 150) * 1.20)
else:
    total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit_charges - 250) * 1.50)

# Calculate the surcharge amount
surcharge = (surcharge_percentage / 100) * total_bill

# Add the surcharge to the total bill
total_bill += surcharge

# Display the total electricity bill
print(f"Total electricity bill: Rs. {total_bill:.2f}")
