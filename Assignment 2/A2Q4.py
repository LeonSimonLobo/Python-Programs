def userindex(string1,string2):
    for i in range(len(string1)):
        if string2==string1[i:len(string2)+i]:
            return i
def userrindex(string1,string2):
    for i in range(len(string1)):
        if string2==string1[i:len(string2)+i]:
            location=i
    return location
def userrfind(string1,string2):
    for i in range(len(string1)):
        if string2==string1[i:len(string2)+i]:
            return i
    return -1
def userreplace(string1,string2,string3):
    stringnew=""
    i=0
    while i<len(string1):
        if string2==string1[i:len(string2)+i]:
            stringnew+=string3
            i+=len(string2)-1
        else:
            stringnew+=string1[i]
        i+=1
    return stringnew
def usercount(string1,string2):
    count=0
    for i in range(len(string1)):
        if string2==string1[i:len(string2)+i]:
            count+=1
    return count
s="abcdefghab"
print(s)
print(userindex(s,'ab'))
print(userrindex(s,'ab'))
print(userrfind(s,'hj'))
print(userreplace(s,'ef','kl'))
print(usercount(s,'ab'))
print(s)
