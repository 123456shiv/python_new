cost_price=int(input("Enter the cost price of the product: "))
selling_price=int(input("Enter the selling price of the product: "))

if selling_price > cost_price:
    # Profit logic
    profit = selling_price - cost_price
    print(f"Result: Profit of {profit:.2f}")

elif cost_price > selling_price:
    # Loss logic
    loss = cost_price - selling_price
    print(f"Result: Loss of {loss:.2f}")

else:
    # Break-even logic (when selling price equals cost price)
    print("Result: No Profit, No Loss (Break-even)")
