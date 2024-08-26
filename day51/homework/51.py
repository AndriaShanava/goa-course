# Creating an initial empty list
my_list = []

# Adding 7 elements to the list
my_list.extend([1, 2, 3, 4, 5, 6, 7])

# Swapping elements at index 2 and index 3
my_list[2], my_list[3] = my_list[3], my_list[2]

# Adding a large number at index 4
my_list.insert(4, 1000000)

# Removing elements at index 5 and index 0
del my_list[5]
del my_list[0]

# Printing the updated list
my_list


# მომხმარებლის მიერ შემოტანილი რიცხვის შეყვანა
user_input = int(input("გთხოვთ შეიტანოთ რიცხვი: "))

# რიცხვის ნიშნის შეცვლა საპირისპიროთი
if user_input > 0:
    user_input = -user_input
else:
    user_input = abs(user_input)

# შედეგის დაბეჭდვა
print("შედეგი: ", user_input)
