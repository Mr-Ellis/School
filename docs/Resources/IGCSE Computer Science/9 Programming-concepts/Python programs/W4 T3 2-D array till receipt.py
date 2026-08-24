#2-D array till receipt

receipt = [[0.99, 2], [1.28, 3], [3.69, 1], [0.49, 4], [8.29,1]]
print(receipt)
grandTotal = 0

for i in range(0,len(receipt)):
    subtotal = receipt[i][0] * receipt[i][1]
    print(receipt[i][0], receipt[i][1], subtotal)
    grandTotal = grandTotal + subtotal

print(round(grandTotal,2))

input("\nPress ENTER to exit program ")
