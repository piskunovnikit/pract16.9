from kvadrat import Rectangle, sqare, circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.getArea())
print(rect_2.getArea())

sqare_1 = sqare(5)
sqare_2 = sqare(10)

print(sqare_1.getAreaSqare())
print(sqare_2.getAreaSqare())

circle_1 = circle(3)
circle_2 = circle(5)
figures = [rect_1, rect_2, sqare_1, sqare_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, sqare):
         print(figure.getAreaSqare())
    elif isinstance(figure, circle):
        print(figure.getAreaCircle())
    else:
         (print(figure.getArea()))


