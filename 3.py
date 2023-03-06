# вводим координаты первой точки
x1 = int(input())
y1 = int(input())

# вводим координаты второй точки
x2 = int(input())
y2 = int(input())

# определяем, лежат ли точки в одной координатной четверти
if (x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0) or (x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0) or (x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0) or (x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0):
    print("YES")
else:
    print("NO")
