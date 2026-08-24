import random

number1 = random.random()
number2 = number1 * 6
number3 = round(number2,0)
print(number3)

#when rounding Python will still treat the number as a float
#it therefore needs to be converted to an int to have no decimal places
print(int(number3))
