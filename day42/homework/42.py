# 1)  გადმოგვეცემა რიცხვებით სავსე სია, ჩვენ ამ სიიდან უნდა შევკრიბოთ ყველა ხუთის ჯერადი რიცხვი და დავბეჭდოთ მათი ჯამი


numbers = [10, 23, 35, 47, 50, 62, 75, 83, 95]

multiples_of_five = [num for num in numbers if num % 5 == 0]

sum_of_multiples_of_five = sum(multiples_of_five)

print("ხუთის ჯერადი რიცხვების ჯამი არის:", sum_of_multiples_of_five)