# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:48:00 2022

@author: Win11
"""

x = str(input("Statement :"))
a = False
b = True

def f(a,b):
    return eval(x)

print(f)
print("----------------------")
print("------TruthTable------")

for a in [b, a]:
    for b in [b, a]:
        print(str(a),str(b), str(f(a,b)))
        a