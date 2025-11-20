decimal = int(input("Enter a decimal number: "))
d = decimal
b = ""

while d > 0:
    b = str(d % 2) + b
    d //= 2

print(f'{decimal}(10) = {b}(2)')

