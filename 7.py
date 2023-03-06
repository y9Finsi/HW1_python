# Вводим кол-во коров
n = int(input())

# Узнаем склонение слова "корова" в зависимости от числа
if n % 10 == 1 and n % 100 != 11:
    word = "korova"
elif n % 10 >= 2 and n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
    word = "korovy"
else:
    word = "korov"

# Получаем результат
print(n, word)
