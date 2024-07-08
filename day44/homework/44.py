#1)For loop

print("Task 1:")
for i in range(21):
    print(i)
print()


print("Task 2:")
for i in range(1, 11):
    print(i)
print()


print("Task 3:")
print("Even numbers:")
for i in range(0, 101, 2):
    print(i)
print("\nOdd numbers:")
for i in range(1, 101, 2):
    print(i)
print()



print("Task 4:")
number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print("Sum of numbers up to", number, "is:", sum)



print("Task 5:")
print("Multiples of 5:")
for i in range(1, 51):
    if i % 5 == 0:
        print(i)
print()

#2)while loop

print("While Loop Task 1:")
num = 0
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1
print()


print("While Loop Task 2:")
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print("Sum of numbers from 1 to 10 is:", total)


print("While Loop Task 3:")
guess = 0
while guess != 7:
    guess = int(input("Guess a number between 1 and 10: "))
print("Congratulations! You guessed the correct number.")


print("While Loop Task 4:")
numbers = [3, 6, 9, 12, 15]
index = 0
while index < len(numbers):
    numbers[index] *= 2
    index += 1
print("Doubled list:", numbers)


print("While Loop Task 5:")
password = ""
while password != "password123":
    password = input("Enter the password: ")
print("Access granted!")


#3)If-Else Statements:

import datetime

print("If-Else Task 1:")
current_hour = datetime.datetime.now().hour
if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")


print("If-Else Task 2:")
number = 15
if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


print("If-Else Task 3:")
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")


print("If-Else Task 4:")
age = 17
if age >= 13 and age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")
