first = 1
second = 2
third  = 3
if first == second and second == third:
    print(3)
elif (first == second or second == third or first == third):
    print(2)
else:
    print(0)