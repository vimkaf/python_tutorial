"""
Parameters and Arguments in Functions
"""

def calculate(a,b,c,d):
    print(a,b,c,d)



calculate(10,20,30,40)

#default parameters
def calculate(a, b = 1):
    return a + b

def areaOfCircle(radius, pi = 3.142):
    return pi * radius ** 2


print( areaOfCircle(20,3.1415) )

#Keyword Arguements

def almighty_formula(a,b =1,c=1):
    print(a,b,c)

almighty_formula(1, c= 5)

def sum(*numbers):
    sum  = 0
    for num in numbers:
        # sum += num 
        sum =  sum + num

    return sum

print ( sum(1,2,3,4,5,6,7,8,9,10) )

def test(**person):
    person['age'] = 22
    print(person)

test(name="Jola",age=20,address="Lagos")

