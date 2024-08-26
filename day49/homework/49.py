total_sum = 0

# Use a for loop to iterate through numbers from 1 to 10
for number in range(1, 11):
    total_sum += number

# Print the result
print("The sum of numbers from 1 to 10 is:", total_sum)






number = int(input("Enter a number: "))

total_sum = 0

for i in range(1, number + 1):
    total_sum += i

print(f"The sum of all numbers up to {number} is {total_sum}.")



# Iterate over the range of numbers and print their squares
for num in range(1, 16):
    print(f"The square of {num} is {num ** 2}")