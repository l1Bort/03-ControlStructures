num_of_hours = int(input("Enter number of hours parked: "))
if num_of_hours == 1 or num_of_hours == 2:
    fee = 5
elif num_of_hours >= 3 and num_of_hours <= 6:
    fee = 15
elif num_of_hours >= 7:
    fee = 20
print(f'The parking fee is: {fee} PLN')