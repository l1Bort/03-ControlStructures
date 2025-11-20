
###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:
    print(countdown)
    countdown -= 1
    if countdown == 5:
        print("five")
        countdown -= 1
        time.sleep(1)  
        print("four")
        countdown -= 1
        time.sleep(1)  
        print("three")
        countdown -= 1
        time.sleep(1)  
        print("two")
        countdown -= 1
        time.sleep(1)  
        print("one")
        countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")





























# Ten zrobiłem sam bo nie widziałem że jest timer.py do zmodyfikowania
# number = int(input('Enter a number to count down from: '))

# for i in reversed(range(1, number + 1)):
#     if i == 5:
#         print("five")
#         continue
#     if i == 4:
#         print("four")
#         continue
#     if i == 3:
#         print("three")
#         continue
#     if i == 2:
#         print("two")
#         continue
#     if i == 1:
#         print("one")
#         continue
#     print(i)

