#დავალება 1

score = int(input("what is your score?"))
if score > 90 < 100:
    print("მთლიანი დაფინანსება")
elif score > 70 <80:
    print("დაფინანსება 1500 ლარი")
elif score > 40 < 70:
    print("დაფინანსება 500 ლარი")
elif score < 40:
    print("არ დაფინანსდება")
else:
    print("incorect")


#დავალება 2

score = int(input("what is your score?"))
if score == 10:
    print("ყოჩაქ")
elif score == 9 or 8:
    print("მეტი შეუძლია")
elif score == 5:
    print("რა არის ეს,მიხედეთ")
elif score < 5:
    print("ჩვენ ვერ ავითანთ ამ ბავშვს")
else:
    print("შეცდომა")