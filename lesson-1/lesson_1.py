'''
Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните
в переменные, выведите на экран.
'''

a = 10
b = 15
print("Переменные a и b - ", a, b)
string1 = input("Введите первую строку ")
number1 = int(input("Введите первое число "))
string2 = input("Введите вторую строку ")
number2 = int(input("Введите второе число "))
print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))

'''
Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды 
и выведите в формате чч:мм:сс. 
Используйте форматирование строк. 
'''

time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"{hours} : {minutes} : {seconds}")

'''
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369
'''

n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)
'''
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
input_number = input("Введите целое положительное число: ")

number_length = len(input_number)
max_element = 0
i = 0
while i < number_length:
        current_element = int(input_number[i])
        if current_element > max_element:
            max_element = current_element
        i += 1
print(max_element)
'''
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или
убыток — издержки больше выручки).
Выведите соответствующее сообщение.
Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы
и определите прибыль фирмы в расчете на одного сотрудника.
'''

profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

'''
Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % 
относительно предыдущего. 
Требуется определить номер дня, на который общий 
результат спортсмена составить не менее b километров. 
Программа должна принимать значения параметров a и b и 
выводить одно натуральное число — номер дня.
'''

a = int(input("Результат первого дня пробежки спротсмена: "))
b = int(input("Желаемый результат пробежки: "))
days = 1
while a < b:
        a *= 1.1
        days += 1
print(f"Достижение пробежки в {b} км за {days} дней")
