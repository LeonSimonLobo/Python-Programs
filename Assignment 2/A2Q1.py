string=input("Enter word:")
newstring=''
for i in range(len(string)):
    if not i%2:
        newstring+=string[i]
    else:
        newstring+=string[i].upper()
print(newstring)