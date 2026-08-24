username = input("Enter your username: ")
PIN = input("Enter your PIN as a number: ")

print("Is username a string? ", isinstance(username, str))
print("Is PIN an integer? ", isinstance(PIN, int))

PINNum = int(PIN)

print("Is PINNum an integer? ", isinstance(PINNum, int))
