"""
Functions 
Functions are resuseable group of code

def nameofFunction():
    #body of the function
"""


def greet():
    print("Hello there!!")

def greet2(name):
    print("Hello ", name)


greet()

greet2("Henry")
greet2("Jane")

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    print ("Interest is = ", interest)

simple_interest(50000,5,3)

# p =  int ( input("Principal: ") )
# r = int( input("Rate: "))
# t = int( input("Time: "))

# simple_interest(p, r, t)


def b():
    a()
    print("b")

def a():
    print("a")

b()



