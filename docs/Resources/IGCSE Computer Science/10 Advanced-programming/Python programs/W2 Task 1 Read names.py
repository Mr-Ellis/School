#part a - output each of the names in a file

names = open("names.txt","r")   #"r" opens the file for reading

EndOfFile = False

while not EndOfFile:
    name = names.readline().rstrip()     #reads the line
                                        #rstrip() removes the \n character at the end of the line
    print(name)
    if not name:                #if the line was the end of file, change the EndOfFile flag to False
        EndOfFile = True

names.close()


names = open("names.txt","r")   #"r" opens the file for reading

EndOfFile = False
nameCounter = 1

#part b - number the list of names

while not EndOfFile:
    name = names.readline().rstrip()     #reads the line
                                        #rstrip() removes the \n character at the end of the line
    if name:                        #check a name was found before printing
        print(nameCounter,name)
        
    nameCounter = nameCounter + 1 #increment nameCounter
    if not name:                #if the line was the end of file, change the EndOfFile flag to False
        EndOfFile = True

names.close()
