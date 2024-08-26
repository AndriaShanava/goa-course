# 1. ფუნქცია, რომელიც იღებს x და y პარამეტრებს და აბრუნებს მათ სხვაობას:

def difference(x, y):
    return x - y

result = difference(10, 5)
print(result)  # გამოიტანა: 5

# 2. ფუნქცია, რომელიც იღებს word1 და word2 პარამეტრებს და აბრუნებს მათ ერთად შერწყმულს:

def merge_words(word1, word2):
    return word1 + " " + word2

result = merge_words("გამარჯობა", "მეგობარო")
print(result)  # გამოიტანა: "გამარჯობა მეგობარო"

# 3. ფუნქცია, რომელიც იღებს length და width პარამეტრებს და ითვლის მართკუთხედის ფართობს:

def rectangle_area(length, width):
    return length * width

result = rectangle_area(4, 6)
print(result)  # გამოიტანა: 24

# 4. ფუნქცია, რომელიც იღებს name პარამეტრს და აბრუნებს "გამარჯობა, [name]" შეტყობინებას:

def greet(name):
    return f"გამარჯობა, {name}"

result = greet("ანა")
print(result)  # გამოიტანა: "გამარჯობა, ანა"

# 5. ფუნქცია, რომელიც აბრუნებს "დიდია" თუ number 10-ზე მეტია და "პატარა" თუ ნაკლებია:

def check_number(number):
    if number > 10:
        return "დიდია"
    else:
        return "პატარა"

result = check_number(9)
print(result)  # გამოიტანა: "პატარა"

# 6. ფუნქცია, რომელიც აბრუნებს შეტყობინებას "კარგი დღე გქონდეს!":

def good_day():
    return "კარგი დღე გქონდეს!"

result = good_day()
print(result)  # გამოიტანა: "კარგი დღე გქონდეს!"

# 7. ფუნქცია, რომელიც იღებს a და b პარამეტრებს და აბრუნებს მათ ჯამს:

def add_numbers(a, b):
    return a + b

result = add_numbers(7, 3)
print(result)  # გამოიტანა: 10

# 8. ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს number-ის კუბს:

def cube(number):
    return number ** 3

result = cube(3)
print(result)  # გამოიტანა: 27

# 9. ფუნქცია, რომელიც აბრუნებს შეტყობინებას "საუკეთესო ხარ!":

def best_message():
    return "საუკეთესო ხარ!"

result = best_message()
print(result)  # გამოიტანა: "საუკეთესო ხარ!"

# 10. ფუნქცია, რომელიც იღებს number პარამეტრს და აბრუნებს "კენტი" ან "ლუწი":

def odd_or_even(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"

result = odd_or_even(8)
print(result)  # გამოიტანა: "ლუწი"
