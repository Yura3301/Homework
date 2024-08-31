first = input(print('Первое число: '))
second = input(print('Второе число: '))
third  = input(print('Третье число: '))
if first == second and second == third:
    print(3)
elif (first == second or second == third or first == third):
    print(2)
else:
    print(0)