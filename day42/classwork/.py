#  შევქმნათ სია რომელშიც გვექნება რომელშიც გვექნება დადებითი და უარყოფითი რიცხვები. გავფილტროთ,
#  უნდა დავაბრუნოთ ორი სია ერთში მხოლოდ დადებითი რიცხვები მეორეში მხოლოდ უარყოფითი რიცხვები



numbers = [12, -7, 5, -3, -14, 9, -21, 30, -1, 6, -11]

positive_numbers = [num for num in numbers if num > 0]

negative_numbers = [num for num in numbers if num < 0]

print("დადებითი რიცხვები:", positive_numbers)
print("უარყოფითი რიცხვები:", negative_numbers)