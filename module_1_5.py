immutable_var = 12,'green',True
print('Immutable tuple:',immutable_var)
# immutable_var[1] = 'black' элементы кортежа не изменяются
mutable_list=[76,'blue',False]
mutable_list[0] = 23
mutable_list[1] = 'black'
mutable_list[2] = True
print('Mutable list:', mutable_list)