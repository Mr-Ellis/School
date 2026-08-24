#iGCSE Unit 1 ASCII and Unicode Worksheet 3
#program to demonstrate ASCII used in arithmetic

x = input("Please input an integer x: ")
y = input("Please input a second integer y: ")
z = x + y

print ("x + y = " + z)
#s = x - y
#print("x - y = " + s)

firstname = input("Please input your first name: ")
secondname = input("Please input your second name: ")
fullname = firstname + " " + secondname
print("Your full name is " + fullname)

x = ord('C')
y = x + 3
z = chr(y)
print("\n ord('C') = " + str(x) + "      ord('C') + 3 = " + str(y) + "     chr(70) = " + z)


input("\nPress Enter to exit.")




