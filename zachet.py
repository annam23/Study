#1.5 Записать логическое выражение, которое определяет, принадлежит ли число А интервалу от -137 до -51 или интервалу от 123 до 55.

a = int(input("ВВедите число: "))

if a in range(-137, -50):
    print('Число принадлежит интервалу от -137 до 50')
elif a in range(55, 124):
    print('Число принадлежит интервалу от 55 до 123')
else:
    print('Число не принадлежит никакому заданному интервалу')

#1.15 Записать логические выражения, которые имеют значение «истина» только при выполнении указанных условий - неверно, что x>0 и x<5.

x = -1
if not x > 0 and not x < 5:
    print("True")
else:
    print("False")


#1.25 Дано натуральное число. Определить, является ли оно четным, или оканчивается цифрой 3.

a = int(input("ВВедите число: "))
spisok_zifr = [int(d) for d in str(a)]
if a % 2 == 0:
    print('Число четное')
elif spisok_zifr[-1] == 3:
    print('Число оканчивается на 3')
else:
    print('Число нечетное и заканчивается не на 3')

#2.5 Дано трехзначное число. Определить: а) является ли сумма его цифр двузначным числом; б) является ли произведение его цифр трехзначным числом.

number = 990
list_number = [int(d) for d in str(number)]
sum_num = "".join([str(d) for d in [sum(list_number)]])
if len(sum_num) == 2:
    print("сумма цифр двузначная")
else:
    print("сумма цифр не двузначная")

mult = 1
for i in list_number:
    mult *= i

if len(str(mult)) == 3:
    print("произведение цифр трехзначное")
else:
    print("произведение цифр не трехзначное")

#3.5
m = int(input("Введите значение от 1 до 4:"))

if m == 1:
    print('пики')
elif m == 2:
    print('трефы')
elif m == 3:
    print('буби')
elif m == 4:
    print('червы')
else:
    print("Введено число вне диапазона")

#4.5 Найти количество и произведение отрицательных элементов, а также сумму нечетных элементов.
list_ = [-1, 2, -5, -8, 7, -2, 9]

new_list_negative = [i for i in list_ if i <0]
mult_neg = 1
for i in new_list_negative:
    mult_neg *= i
print(f'Количество отрицательных значений {len(new_list_negative)}, их произведение {mult_neg}')

#5.1
m = int(input("Введите число: "))

while m != 1:
    if m % 2 == 0:
        m = m / 2
    else:
        m = (m * 3 + 1) / 2

    print(m)

#5.2
day_distance_n = 12
progress_y = day_distance_n * 0.2
days_x = list(range(1, 8))
full_dist = 0
for day in days_x:
    day_distance_n += progress_y
    full_dist += day_distance_n
    print(full_dist)

#5.3
n = int(input("Введите число: "))
chet = 0
nechet = 0

while n > 0:
    if n % 2 == 0:
        chet += 1
    else:
        nechet += 1
    n //= 10
print(f'В числе четных цифр {chet}, нечетных {nechet}')

#5.4


