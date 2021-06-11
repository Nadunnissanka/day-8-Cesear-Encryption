import math

def pain_cal(height, width):
    coverage = 5
    number_of_cans = ( height * width ) / coverage
    exact_cans = math.ceil(number_of_cans)
    print(f"You need {exact_cans} cans to pain the wall")

wall_height = int(input("Enter your wall's Height:- "))
wall_width = int(input("Enter your wall's width:- "))

pain_cal(height = wall_height, width = wall_width)