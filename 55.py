n = int(input("Enter a number: "))

is_prime = True

if n <= 1:
    is_prime = False

i = 2
while i < n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print("It is a prime number!")
else:
    print("That is not a prime number!")