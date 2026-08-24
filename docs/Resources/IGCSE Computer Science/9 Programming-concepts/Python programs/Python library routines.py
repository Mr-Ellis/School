import statistics

ages = [18,2,14,6]
a = min(ages)
b = max(ages)
c = sum(ages)
d = statistics.mean(ages)
ages.sort()
print(ages)
print(a,b,c,d)
if 14 in ages:
    print("14 present")
