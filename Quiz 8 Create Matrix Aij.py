import numpy as np
# Retrieved size of matrix from user
x = int(input("Enter size of columns: "))
result = [] # Create empty list for accept value.

for i in range(1,x+1): #Check each i in x.
    for j in range(1,x+1):
        # Setting Conditions
        if i < j and j != i: 
            result.append(0)        # Adding value to list.
        elif i == j or j == x:
            result.append(1)
        else:
            result.append(-1)

result = np.array(result).reshape(x,x)  # using array to create matrix x,x
print(result) # print matrix
