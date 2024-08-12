
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append(70)


my_list[2], my_list[3] = my_list[3], my_list[2]


large_number = 999999
my_list.append(large_number)


my_list.pop(5)   
my_list.pop(0)   


my_list[3] = 888888


print(my_list)
