x = 0
y = 4
point = f'P({x}, {y})'

if x == 0 and y == 0:
    print(f'Point {point} is at the origin of the coordinate systems ')
elif x == 0:
    print(f'Point {point} is on the y axis')
elif y == 0:
    print(f'Point {point} is on the x axis')

elif x > 0 and y > 0:
    print(f'Point {point} is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point {point} is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point {point} is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point {point} is in the fourth quadrant of the coordinate system')
else:
    print(f'Point {point} cannot be determined')