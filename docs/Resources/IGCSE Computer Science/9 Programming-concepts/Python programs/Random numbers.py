import random

numbers = [0,0,0,0,0,0]

for i in range(0,100):
    rand = int(round(random.random()*6+0.5,0))
    numbers[rand - 1] = numbers[rand - 1] + 1

print(numbers)


import statistics

print(max([5,2,8]))
print(min([5,2,8]))
print(sum([5,2,8]))
print(statistics.mean([5,2,8]))
animals = ['rabbit', 'cat', 'dog', 'hamster']
animals.sort()
print(animals)
print('hamster' in animals)

ages = [18,2,14,6]
a = min(ages)
b = max(ages)
c = sum(ages)
d = statistics.mean(ages)
print(ages.sort())
print(a,b,c,d)
if 14 in ages:
    print("14 present")
