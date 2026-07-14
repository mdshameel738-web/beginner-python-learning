#TIP CALCULATOR AND BILL DIVIDER

print("Welcome to the tip calculator!")
print()

# Get inputs from user
bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculate tip amount
tip_amount = (tip_percent / 100) * bill

# Calculate total bill with tip
total_bill = bill + tip_amount

# Calculate bill per person
bill_per_person = total_bill / people

# Display results
print()
print("Bill Summary:")
print("Original Bill: $" + str(bill))
print("Tip Amount: $" + str(tip_amount))
print("Total Bill: $" + str(total_bill))
print("Number of People: " + str(people))
print("Each person pays: $" + str(bill_per_person))