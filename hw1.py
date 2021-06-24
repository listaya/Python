#1
a = 3
b = a + 15
print("3+15 =", b)
c = 9
d = c * 3
print("9*3 =", d)

#2
time = int(input("Enter the time in seconds: "))
hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:05}:{minutes:5}:{seconds:05}")

#3
n = input("Enter an integer: ")
while n < '0':
    print("Choose the number greater than 0")
    n = input('Enter the number greater than 0: ')
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

#4
num_init = int(input("Введите целое положительное число: "))
greatest_dig = 0
num = num_init
while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10
print(f"Наибольшая цифра в число {num_init} равна {greatest_dig}")

#5
revenue = float(input("Введите значение выручки - "))
costs = float(input("Введите значение издержек - "))
result = revenue - costs
if result > 0:
    print(f"Ура! Прибыль {result} !")
    print(f"Рентабельность {100 * result / revenue:.1f}%")
    personal_n = int(input("Численность сотрудников? "))
    print(f"Прибыль на каждого сотрудника состовляет {result / personal_n:.3f}")
elif result < 0:
    print(f"Упс, убытки {-result}")
else:
    print("Ноль")

#6
while True:
    days = 1
    start_km = float(input("Стартовый результат: "))
    last_km = float(input("Конечный результат "))
    if start_km <= 0 or last_km < 0:
        print("Результат должен быть больше нуля. Стартовое значением!= 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Спортсмен добьется результата за {days} дней")
        break
