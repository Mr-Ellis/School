miles = -1
valid = False

while not valid:

    mph = float(input("Enter number of miles per hour: "))

    if mph >= 0 and mph <= 100:
        valid = True
        kmph = 1.609 * mph
        print(kmph, "km/h")
        
