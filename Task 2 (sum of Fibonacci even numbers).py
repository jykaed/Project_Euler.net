# Ввод количества чисел в последовательности:
n=int(input("Введите кол-во чисел в последовательности "))
# Начальное значение суммы последовательности Фибоначчи
fib=0
# Первые два числа:
a,b=1, 1
# Отображение первых двух чисел
print(a,b, end=" ")
# За каждый цикл вычисляется одно новое число
for k in range (n-2):
    # Вычисление нового числа в последовательности
    a, b=b, a+b
    # Отображение нового числа
    print(b, end=" ")
    # Сумма четных элементов последовательности Фибоначчи
    if b%2==0 : # Если надо ограничить четырьмя миллионами то пишем доп.условие - and b<4000000
        fib=fib+b
print('\n',"Сумма четных чисел Фибоначчи",fib)