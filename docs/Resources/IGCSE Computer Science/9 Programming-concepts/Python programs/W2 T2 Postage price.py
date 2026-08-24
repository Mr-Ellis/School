classType = input("Enter class: ")
size = input("Enter size: ")
weight = float(input("Enter weight: "))


if classType == "first-class":
    if size == "letter" and weight <= 100:
        price = 1.65
    if size == "large letter":
        if weight <= 100:
            price = 1.95
        else:
            if weight <= 250:
                price = 2.37
            else:
                price = 2.81
               
        
print(price)
