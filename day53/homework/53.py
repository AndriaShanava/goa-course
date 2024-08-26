import random

choices = ["ქაღალდი", "მაკრატელი", "ქვა"]

# მომხმარებლის არჩევანი
user_choice = input("აირჩიეთ ქაღალდი, მაკრატელი ან ქვა: ").lower()
while user_choice not in ["ქაღალდი", "მაკრატელი", "ქვა"]:
    print("არასწორი არჩევანი. სცადეთ კიდევ.")
    user_choice = input("აირჩიეთ ქაღალდი, მაკრატელი ან ქვა: ").lower()

# კომპიუტერის არჩევანი
computer_choice = random.choice(choices)
print(f"კომპიუტერის არჩევანი: {computer_choice}")

# გამარჯვებულის დადგენა
if user_choice == computer_choice:
    print("ფრეა!")
elif (user_choice == "ქაღალდი" and computer_choice == "ქვა") or \
     (user_choice == "მაკრატელი" and computer_choice == "ქაღალდი") or \
     (user_choice == "ქვა" and computer_choice == "მაკრატელი"):
    print("თქვენ მოიგეთ!")
else:
    print("თქვენ წააგეთ!")


# 2) შექმენით სია, რომელიც თავდაპირველად იქნება ცარიელი შემდეგ კი ამ სიაში ჩაამატეთ 10 ელემენტი
list1 = []
list1.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 3) შექმენით ორი სია ერთში თქვენი ხელით ჩაწერეთ ლუწი რიცხვები, მეორეში კენტი რიცხვები შემდეგ კი ეს ორი სია გააერთიანეთ extend ის გამოყენებით 
even_numbers = [2, 4, 6, 8, 10]
odd_numbers = [1, 3, 5, 7, 9]
combined_list = even_numbers.copy()  # making a copy to keep the original even_numbers intact
combined_list.extend(odd_numbers)

# 4) შექმენით სია რომელშიც იქნება 20 ელემენტი, შემდეგ კი დაბეჭდეთ თითოეული სათითაოდ for loop ის გამოყენებით
list2 = list(range(1, 21))
individual_elements = [element for element in list2]

# 5) შექმენით რიცხვებით სავსე სია რომელშიც იქნება 1 დან 20 მდე ყველა რიცხვი, შემდეგ კი ამ სიიდან ამოშალეთ ყველა კენტი რიცხვი და დაამატეთ ახალ სიაში, ორივე სია დაბეჭდეთ
list3 = list(range(1, 21))
even_numbers_list3 = [number for number in list3 if number % 2 == 0]
remaining_list3 = [number for number in list3 if number % 2 != 0]

# 6) შექმენით სია რომელშიც იქნება 10 განსხვავებული რიცხვი შემდეგ კი დაბეჭდეთ ყველა ლისტის ელემენტის ჯამი
list4 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
sum_list4 = sum(list4)

# 7) შექმენით რიცხვებით სავსე სია, გამოითვალეთ ამ სიის ელემენტების საშუალო არითმეტიკული
list5 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
average_list5 = sum(list5) / len(list5)

# Printing results
list1, combined_list, individual_elements, even_numbers_list3, remaining_list3, sum_list4, average_list5