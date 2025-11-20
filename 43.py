format24 = input("Enter time (24-hour format): ")
hours_int = int(format24[0:2])
hours_str = format24[0:2]

if hours_int < 0 or hours_int > 23:
    print("Invalid time entered.")
elif hours_int < 12:
    format12 = hours_str + format24[2:]
    print(f"Time in 12-hour format: {format12}am")
elif hours_int == 12:
    format12 = hours_str + format24[2:]
    print(f"Time in 12-hour format: {format12}pm")
else:
    hours_int -= 12
    hours_int_str = str(hours_int)
    format12 =  hours_int_str + format24[2:]
    print(f"Time in 12-hour format: {format12}pm")
