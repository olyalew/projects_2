#1
def square(number):
    return number ** 2

def square_and_print(number):
    print(f"Квадрат числа равен: {number}")

def square_and_print_with_return(number):
    result = number ** 2
    print(f"Квадрат числа равен: {result}")
    return result

number = float(input("Введите число: "))

result1 = square(number)
print(result1)

square_and_print(number)

result2 = square_and_print_with_return(number)
print(result2)

#2
def nums(n):
    previous = n - 1
    next_number = n + 1

    result = [previous, next_number]
    return result

input_number = int(input("Введите целое число: "))
output_list = nums(input_number)
print(output_list)

#3
def str_lower(input_string):
    words = input_string.split()

    lower_words = [word.lower() for word in words]

    return lower_words

input_string = input("Введите строку: ")
output_list = str_lower(input_string)
print(output_list)

#4
import math


def my_log(numbers):
    result = []

    for num in numbers:
        if num <= 0:
            result.append(None)
        else:
            result.append(math.log(num))

    return result

input_numbers = [1, 3, 2.5, -1, 9, 0, 2.71]
output_logs = my_log(input_numbers)
print(output_logs)

#5
def create_age_dictionary(names, ages):
    if len(names) == len(ages):
        age_dict = dict(zip(names, ages))
        return age_dict
    else:
        print("Списки имеют разную длину")
        return {}

names1 = ["Ann", "Tim", "Sam"]
ages1 = [12, 23, 17]

result1 = create_age_dictionary(names1, ages1)
print(result1)

names2 = ["Ann", "Tim", "Sam"]
ages2 = [12, 23, 17, 45]

result2 = create_age_dictionary(names2, ages2)
print(result2)

#6
import math

def binom_coefficient(n, k):
    if 0 <= k <= n: #под вопросиком
        return math.comb(n, k)
    else:
        return 0

def binom_prob(p, n, k):
    if 0 <= k <= n: #под вопросиком
        coefficient = binom_coefficient(n, k)
        probability = coefficient * (p ** k) * ((1 - p) ** (n - k))
        return probability
    else:
        return 0

p = 0.5
n = 10
k = 5

result = binom_prob(p, n, k)
print(f"Вероятность получить {k} успехов из {n} испытаний при вероятности успеха {p} равна {result}")

#7
def all_sort(*args):
    sorted_list = sorted(args)
    return sorted_list

input_values = 7, 6, 1, 3, 8, 0, -2
sorted_values = all_sort(*input_values)
print(sorted_values)
