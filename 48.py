for i in range(1, 31):
    if i % 5 == 0 and i % 3 == 0:
        print("BINGO")
        continue

    if i % 3 == 0:
        print("THREE")
        continue

    if i % 5 == 0:
        print("FIVE")
        continue
    print(i)
