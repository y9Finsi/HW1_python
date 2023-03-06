# вводим координаты первой точки
x1 = int(input())
y1 = int(input())

# вводим координаты второй точки
x2 = int(input())
y2 = int(input())

# определяем знаки координат x и y для обеих точек
znak_x1 = 1 if x1 > 0 else -1
znak_y1 = 1 if y1 > 0 else -1
znak_x2 = 1 if x2 > 0 else -1
znak_y2 = 1 if y2 > 0 else -1

# проверяем, совпадают ли знаки координат у обеих точек
if znak_x1 == znak_x2 and znak_y1 == znak_y2:
    print("YES")
else:
    print("NO")
