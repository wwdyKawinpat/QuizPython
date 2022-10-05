def fibonanci(n): #Create function fibonanci
    x = 0
    y = 1
    count = 0
    fibo = [0,] #Set a first number in fibonanci
    
    while count < n-1: #Set number of iterations
        z = x+y
        x = y
        y = z
        count += 1
        fibo.append(z) #Keep a number in fibo
          
    return fibo #Send a result
       
print(fibonanci(100)) #Print result
