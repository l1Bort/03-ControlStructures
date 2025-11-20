for i in range(0,3):
    
    pin_code = int(input("Enter the PIN code: "))
    if pin_code == int('0850'):
        print("PIN is correct")
    else:
        print("Incorrect...")

    if i == 2 and pin_code != int('0850'): 
        print("Sorry, your payment card has been blocked.")    
    