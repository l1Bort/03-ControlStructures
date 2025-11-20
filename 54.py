a = 0
b = 1

print(a, b, end= ' ')

number = 2

while number < 20:
    c = a + b 
    print (c, end= ' ')
    a = b 
    b = c
    number += 1