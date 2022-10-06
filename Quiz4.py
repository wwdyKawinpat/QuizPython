
#Retrieved Logic Statement from use
statement = str(input("Logic Statement :"))
statement = statement.lower()                       # Convert x into lower case form.
# Create Table Header
print ('|-----------Truth Table----------|')

def f(a,b):                         # Create function to evaluate 'AND' 'OR' 'NOT'
    return eval(statement)
                                    # Manually create other opertions function
def NAND (a,b):                     # like 'NAND' 'NOR' 'XOR' 'NXOR'
    if a == True and b == True :
        return(False)
    else :
        return(True)

def NOR (a,b):
    if a == False and b == False :
        return(True)
    else :
        return(False)

def XOR (a,b):
    if a == True and b == True :
        return(False)
    elif a == False and b == False :
        return(False)
    else :
        return(True)
        
def NXOR (a,b):
    if a == True and b == True :
        return(True)
    elif a == False and b == False :
        return(True)
    else :
        return(False)         
                                    # Showing Truth Table.
for a in [True, False]:
    for b in [True, False]:
        if ' nand' in statement: # Checking conditions by word.
            print('|--{:^6}--|--{:^6}--|--{:^6}--|'.format(str(a),str(b), str(NAND (a,b)))) 
        elif 'nor' in statement:
            print('|--{:^6}--|--{:^6}--|--{:^6}--|'.format(str(a),str(b),str(NOR(a,b))))
        elif 'xor' in statement:
            print('|--{:^6}--|--{:^6}--|--{:^6}--|'.format(str(a),str(b),str(XOR(a,b))))
        elif 'nxor' in statement:
            print('|--{:^6}--|--{:^6}--|--{:^6}--|'.format(str(a),str(b),str(NXOR(a,b))))
        else:
            print('|--{:^6}--|--{:^6}--|--{:^6}--|'.format(str(a),str(b),str(f(a,b)))) 