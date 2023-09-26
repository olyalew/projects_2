#1
number = float(input("Введите положительное число: "))
if number > 0:
    print("Молодец!")
else:
    print("Это не положительное число.")

#2
grades = input("Введите список оценок студентов (через пробел): ").split()
grades = [int(grade) for grade in grades]
for grade in grades:
    if grade < 1 or grade > 10:
        print("Оценка вне диапазона (допустимы оценки от 1 до 10)")
    elif grade == 1 or grade == 2:
        print(f"{grade}: Плохо")
    elif grade == 3 or grade == 4:
        print(f"{grade}: Удовлетворительно")
    elif grade == 5 or grade == 6:
        print(f"{grade}: Хорошо")
    else:
        print(f"{grade}: Отлично")

#3
# Задаем верный пароль
correct_password = "my_secret_password"
while True:
    user_password = input("Введите пароль: ")
    if user_password == correct_password:
        print("Login success")
        break
    else:
        print("Incorrect password, try again!")

#4
favorites = [3, 7, 11, 23, 18, 48, 81]
user_number = int(input("Введите целое число: "))
if user_number in favorites:
    print("Мое любимое число!")
else:
    print("Эх, ну почему?")

#5
user_number = int(input("Введите число: "))
if user_number % 2 == 0:
    print("Это число чётное")
else:
    print("Это число нечётное")

#6
word = input("Введите существительное: ")
if word.istitle():
    print("Это имя собственное.")
else:
    print("Это имя нарицательное.")
