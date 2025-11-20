###
# Sums numbers entered by user
#
total_sum = 0
how_many = 0   

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        if how_many == 0:
            arithmetical_sum = 0  
        else:
            arithmetical_sum = total_sum / how_many 

        break  # Exit the loop when 0 is entered

    total_sum += number
    how_many += 1

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetical mean of the numbers is: {arithmetical_sum}")
