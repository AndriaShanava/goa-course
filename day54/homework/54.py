# 1) შექმენით კალკულატორის ფუნქცია  რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და მოქმედების ტიპს(მიმატება, გამოკლება, გამრავლება, გაყოფა) შესაბამისად
#  ფუნქცია დააბრუნებს ანუ დაბეჭდავს შედეგს
#  იმისდამიხედვით მომხმარებელს რა სურს და რა რიცხვები შემოიტანა,
#  მაგალითად მომხმარებელმა თუ შემოიტანა 5 და 2 და ასევე მას სურს გამრავლება ფუნქციამ უნდა დააბრუნოს დაბეჭდოს შედეგად 2 * 5 ანუ 10

# def გამრავლება(x, y):
#     return x * y

# def გაყოფა(x, y):
#     if y == 0:
#         return "გაყოფა ნაწილი 0-ით არ შეიძლება"
#     return x / y

# def ჯამი(x, y):
#     return x + y

# def გამოკლება(x, y):
#     return x - y

# # კალკულატორის მთავარი ლოგიკა
# while True:
#     print("გთხოვთ, აირჩიეთ ოპერაცია:")
#     print("1. გამრავლება")
#     print("2. გაყოფა")
#     print("3. ჯამი")
#     print("4. გამოკლება")
#     print("5. გამეორება")
#     print("6. გამოსვლა")

#     არჩევა = input("თქვენი არჩევა (1/2/3/4/5/6): ")

#     if არჩევა in ('1', '2', '3', '4'):
#         num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
#         num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

#         if არჩევა == '1':
#             print(num1, " * ", num2, " = ", გამრავლება(num1, num2))

#         elif არჩევა == '2':
#             print(num1, " / ", num2, " = ", გაყოფა(num1, num2))

#         elif არჩევა == '3':
#             print(num1, " + ", num2, " = ", ჯამი(num1, num2))

#         elif არჩევა == '4':
#             print(num1, " - ", num2, " = ", გამოკლება(num1, num2))

#     elif არჩევა == '5':
#         continue
#     elif არჩევა == '6':
#         break
#     else:
#         print("არასწორი არჩევა")




# 2) შექმენით ფუნქცია რომელშიც იქნება რიცხვებით სავსე სია და ფუნქცია დააბრუნებს ამ რიცხვების ჯამს

def list():
    print("numbers")

numbers = ["22", "33", "44", "55", "66", "77", "88", "99"]
print(len(numbers))