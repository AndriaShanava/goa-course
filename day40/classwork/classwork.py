odd_numbers = []
numbers_list = []
even_numbers = []
for i in range(10):
    numbers = int(input("enter number: "))
    list.append(numbers)

for i in range(len(list)):
    if numbers_list[i] % 2 == 0:
       even_numbers.append(list[i])
    else:
        odd_numbers.append(list[i])
print("this is even number: ",even_numbers )
print("this is odd number: ", odd_numbers )