num = 1

for row in range(7):       
    for col in range(7):    
        print(num, end=' ')
        num += 7            
    print()
    num = row + 2          