# 1) მომხმარებელს შემოატანინეთ ათი რიცხვი,
#ეს რიცხვები დაამატეთ სიაში,
#ამ სიიდან დაახარისხეთ ეს რიცხვები ორ ჯგუფად, რიცხვები რომლებიც მეტია 100 ზე და რიცხვები რომლებიც ნაკლებია 100 ზე
 
numbers = []

for i in range(10):
    number = int(input("შემოიტანეთ რიცხვი: "))
    numbers.append(number)


greater_than_100 = []
less_than_100 = []



for number in numbers:
   if number > 100:
       greater_than_100.append(number)
   else:
       less_than_100.append(number)


print("100-ზე მეტი რიცხვები: ", greater_than_100)
print("100-ზე ნაკლები რიცხვები: ", less_than_100)