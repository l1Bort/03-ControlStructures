current_price = 140.00
previous_price = 200.00
print(f"Current price: {current_price}")
print(f"Previous price: {previous_price}")

if current_price < previous_price * 0.9:
    print("Buy the product!!")
    reduciton = previous_price - current_price
    reduciton = (reduciton / previous_price) * 100
    print(f"Product price reduced by {reduciton:.0f}%")
else:
    print("Do not buy the product.")
