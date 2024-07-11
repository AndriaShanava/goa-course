# 2) მოიფიქრეთ რამე ამოცანა და დაწერეთ ამოცანის კოდი

def find_median(numbers):
    # სიის დალაგება
    numbers.sort()
    
    # სიის ზომის პოვნა
    n = len(numbers)
    
    # თუ რაოდენობა კენტი რიცხვია, მედიანა იქნება შუა ელემენტი
    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        # თუ რაოდენობა ლუწია, მედიანა იქნება შუა ორი ელემენტის საშუალო
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    
    return median

# მაგალითი გამოყენება
numbers = [3, 5, 1, 4, 2]
median = find_median(numbers)
print(f"რიცხვების სიაში {numbers}, მედიანა არის: {median}")