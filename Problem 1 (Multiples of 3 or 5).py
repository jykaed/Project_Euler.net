# Ввод количества чисел в последовательности:
n=int(input("Введите кол-во чисел"))
# Первоначальное значение суммы чисел кратных 3 и 5
a=0
# Цикл начиная с 1
for n in range(n+1):
    if n%3==0:
        a=a+n
    if n%5==0:
        a=a+n
print(a)

