integers=[]
squares=[]
alphabets=[]
for i in range(50):
    integers.append(i)
print(integers)
for i in range(1,51):
    squares.append(i*i)
print(squares)
for i in range(97,123):
    alphabet=''
    for j in range(96,i):
        alphabet+=chr(i)
    alphabets.append(alphabet)
print(alphabets)