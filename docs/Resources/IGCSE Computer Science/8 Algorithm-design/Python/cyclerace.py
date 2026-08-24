fastestTime = 0
firstInput = True
moreTimes = True

while moreTimes:
    time = int(input("Enter time in seconds - enter -1 to exit: "))

    if time == -1:
        moreTimes = False
    else:
        if firstInput:
            fastestTime = time
            firstInput = False
        else:
            if time < fastestTime:
                fastestTime = time
    print(fastestTime)

print(fastestTime)
