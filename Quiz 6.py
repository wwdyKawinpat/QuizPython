# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:12:28 2022

@author: Win11
"""

def morse_code(str): #Create function to generate morse code
    #Create Dictionary
    code = {"A":".-", "B":"-...","C": "-.-.","D":"-..","E": ".","F" :"..-.",
            "G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--",
            "N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
            "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"-..",
        
            "a":".-", "b":"-...","c": "-.-.","d":"-..","e": ".","f" :"..-.",
            "g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--",
            "n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
            "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"-.."}
    
    m_code = ""
    #Combine result
    for i in x:
        m_code += " "+code[i]
        
    return m_code #Send result
    
x = str(input("Enter your text :"))

print(morse_code(x))