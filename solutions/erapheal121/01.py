from tkinter import S


print ("ejike michael")
"""
a program to calculate S.I(simple interest) 
formula s.i=principal * rate * time / 100
"""
principal = int(input("principal"))
rate = int(input("rate"))
time = int(input("time"))
SI = (principal * rate * time) / 100
print("the S.I unit is",SI)