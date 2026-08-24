marks = open("marks.txt","w")   #open the file in write mode

moreNames = True    #set the flag

while moreNames:        #loop if there are more names
    name = input("Enter student name: ")
    mark = input("Enter mark: ")
    record = name + "," + mark + "\n" #construct the record
    marks.write(record) #write the record

    choice = input("Enter another student (y/n)? ")
    if choice == "n": #if the user has no more students...
        moreNames = False #...set the flag to False

marks.close()
