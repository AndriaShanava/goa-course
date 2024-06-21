# 1) გააკეთეთ საკლასო დავალება ხელახლა თქვენით და კარგად გაანალიზეთ და გაიაზრეთ "მომხმარებელს შემოვატანინოთ 10 რიცხვი შემდეგ დავამატოთ სიაში,
#  გავფილტროთ ეს სია ორ ნაწილად
# ლუწებად და კენტებად და დავამატოთ ახალ სიაში ლუწები ცალკე კენტები ცალკე"

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



# 2) მომხმარებელს შემოატანინეთ რიცხვები, ამ რიცხვებისგან შექმენით სია შემდეგ კი დაითვალეთ რამდენი ორნიშნა რიცხვია სიაში

# რიცხვების შეყვანა
numbers = input("შემოიტანეთ რიცხვები: ")

# სიაში გადაყვანა რიცხვებისგან
numbers_list = list(map(int, numbers.split()))

# ორნიშნა რიცხვების რაოდენობის დათვლა
two_digit_count = sum(1 for num in numbers_list if 10 <= num <= 99)

# შედეგის გამოტანა
print(f"სიაში არის {two_digit_count} ორნიშნა რიცხვი.")

