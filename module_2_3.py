my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
count = 0
while True:
    if int(my_list[count] > num):
        print(my_list[count])
        count += 1
        if count == 12:
            break
    if int(my_list[count] == num):
        count += 1
    if int(my_list[count] < num):
        break