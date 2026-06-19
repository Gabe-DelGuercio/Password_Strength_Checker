points = 0
Password = input("What would you like your password to be?")
print({Password})
contNumb = any(char.isdigit() for char in Password)
if (contNumb == True):
    points += 1
contUpper = any(char.isupper() for char in Password)
if (contUpper == True):
    points += 1
contLwer = any(char.islower() for char in Password)
if (contLwer == True):
    points += 1
hasSpecial = not Password.isalnum()
if (hasSpecial == True):
    points += 1
if (points == 0 or points == 1):
    print("Weak Password")
if (points == 2):
    print("Medium Password")
if (points == 3 or points == 4):
    print("Strong Password")