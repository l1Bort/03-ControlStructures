barcode = input("Enter product barcode: ")

if len(barcode) == 13 and barcode.isdigit():
    print("Article number is correct")
    if barcode[0:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Article number is incorrect")

    

