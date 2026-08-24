#part a - output each of the names in a file

names = open("names.txt","r")   #"r" opens the file for reading

for name in names:
    print(name.rstrip())

names.close()


#part b - output each of the names with a counter at the start


names = open("names.txt","r")   #"r" opens the file for reading

nameCounter = 1

for name in names:
    print(nameCounter, name.rstrip())
    nameCounter = nameCounter + 1

names.close()
