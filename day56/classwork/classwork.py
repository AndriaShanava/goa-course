# 1. შექმენით პროგრამა, რომელიც ბეჭდავს 5-ის ჯერადებს 1-დან 50-ის ჩათვლით for loop-ის გამოყენებით.

for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# 2. დაწერეთ პროგრამა, რომელიც ბეჭდავს ლუწ რიცხვებს 2-დან 20-ის ჩათვლით for loop-ის გამოყენებით.

def multiply_range():
    product = 1
    for i in range(5, 11):
        product *= i
    return product

# 3. ფუნქცია, რომელიც ითვლის რიცხვის ფაქტორიალს:

def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# 4. ფუნქცია, რომელიც ამოწმებს რიცხვის ლუწობას და შემდეგ ასრულებს შესაბამის ოპერაციას:

def process_number(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1
    
# 5. შექმენით ფუნქცია რომელსაც ექნება ერთი პარამეტრი ასაკისთვის და ამ ფუნქციამ უნდა დააბრუნოს მხოლოდ თქვენი ასაკი,
# ფუნქციის გამოძახების დროს ფუნქციას არგუმენტად გადაეცით თქვენი ასაკი

def return_age(age):
    return age

my_age = return_age(25)  
print("ჩემი ასაკი არის:", my_age)

# 1. ოთხი მათემატიკური ფუნქცია: +, -, *, /

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "გაყოფა ნულზე შეუძლებელია"

# 2. მართკუთხედის ფართობის გამოთვლის ფუნქცია:

def calculate_area(length, width):
    return length * width

# 3. მართკუთხედის პერიმეტრის გამოთვლის ფუნქცია:

def calculate_perimeter(side1, side2, side3, side4):
    return side1 + side2 + side3 + side4

# 4. ფუნქცია, რომელიც მიიღებს სიას და დააბრუნებს სიის რიცხვების ჯამს:

def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# 5. ფუნქცია, რომელიც დაბეჭდავს სიიდან მინიმალურ და მაქსიმალურ რიცხვებს:

def find_min_max(numbers):
    if len(numbers) == 0:
        return "სია ცარიელია"

    min_value = numbers[0]
    max_value = numbers[0]

    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number

    print("მინიმალური რიცხვი:", min_value)
    print("მაქსიმალური რიცხვი:", max_value)

# 6. შექმენით ფუნქცია, რომელიც დაბეჭდავს კონკრეტული სიიდან მინიმალურ და მაქსიმალურ რიცხვებს,
# არ გამოიყენოთ min და max. გამოიყენეთ def, for, if/else, indexing, print.

# მათემატიკური ფუნქციები
print("2 + 3 =", add(2, 3))
print("5 - 2 =", subtract(5, 2))
print("4 * 3 =", multiply(4, 3))
print("10 / 2 =", divide(10, 2))

# მართკუთხედის ფართობის გამოთვლა
length = 5
width = 3
print("მართკუთხედის ფართობი:", calculate_area(length, width))

# მართკუთხედის პერიმეტრის გამოთვლა
side1 = 5
side2 = 3
side3 = 5
side4 = 3
print("მართკუთხედის პერიმეტრი:", calculate_perimeter(side1, side2, side3, side4))

# სიის რიცხვების ჯამი
numbers_list = [1, 2, 3, 4, 5]
print("სიის რიცხვების ჯამი:", list_sum(numbers_list))

# მინიმალური და მაქსიმალური რიცხვების პოვნა სიიდან
find_min_max(numbers_list)
