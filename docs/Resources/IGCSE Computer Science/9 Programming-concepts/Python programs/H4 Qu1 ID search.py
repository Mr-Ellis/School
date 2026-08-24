#AQA Unit 2A Homework 4 Qu1 ID search v1.py
ID = [45, 33, 27, 88, 103, 66, 71]
numberSought = int(input ("Please enter ID number to find: "))
found = False
n = len(ID)
k = 0
while found == False and k < n:
    print("number sought", numberSought, "k", k, "ID[k]", ID[k])
    if numberSought == ID[k]:
        found = True
    #ENDIF
    k = k + 1
# endwhile
if found == True:
    print ("ID is in the list at index ", k - 1)
else:
    print("ID is not in the list")
    
input("\nPress ENTER to exit program ")
