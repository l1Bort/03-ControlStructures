star = "* "
n = 2

for i in range(1, 10):
    result = star * i
    if i > 5:
        result = star * (i - n)
        n += 2 
    print(result)