#output initial and surname
firstName = input("Enter your first name: ")
surname = input("Enter your surname: ")
initial = firstName[0]
initialUpper = initial.upper()
surnameStart = surname[0]
surnameStart = surnameStart.upper()
length = len(surname)
remain = surname[1:]
lowerRemain = remain.lower()
surname = str(surnameStart) + str(lowerRemain)
fullName = initialUpper + " " + surname
print(fullName)
input("\nPress ENTER to exit program ")
