import numpy as np

x = int(input("Enter size of column: "))
result = []

for i in range(1,x+1): #Check each i in x
    for j in range(1,x+1):
        #Conditions
        if i < j and j != i: 
            result.append(0)
        elif i == j or j == x:
            result.append(1)
        else:
            result.append(-1)

result = np.array(result).reshape(x,x)
print(result)