units=float(input("Enter the number of units consumed: "))

fixed_charge = 150.00
bill_amount = 0.0

if units <= 100:
    bill_amount = units * 3.50
    
elif units <= 300:
    bill_amount = (100 * 3.50) + ((units - 100) * 5.00)
    
else:
    bill_amount = (100 * 3.50) + (200 * 5.00) + ((units - 300) * 7.50)

total_bill = bill_amount + fixed_charge

print(f"\n⚡ --- Electricity Bill Statement ---")
print(f"Units Consumed : {units:.2f} kWh")
print(f"Energy Charges : ₹{bill_amount:.2f}")
print(f"Fixed Charges  : ₹{fixed_charge:.2f}")
print(f"------------------------------------")
print(f"Total Amount   : ₹{total_bill:.2f}")