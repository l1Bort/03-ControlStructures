number = int(input("Number of products purchased: "))
price = float(input("Product price: "))

if number > 2:
    total_price = (2 * price) + ((number - 2) * price * 0.75) # 25% discount for each product over two
    print(f"Amount to pay {total_price}")
else:
    total_price = number * price
    print(f"Amount to pay {total_price}")