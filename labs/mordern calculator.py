#1.add 
#2.substract
#3.multiply
#4.divide

print("Menu")
print("1. Add")
print("2. Substract")
print("3. Multiplication")
print("4. Division")
calculation=input()
if calculation == 1:
    num1=input("insert first value")
    num2=input("insert second value")
    print("The sum is"+ num1 + num2)
elif calculation == 2:
    num1=input("insert first value")
    num2=input("insert second value")
    print("The difference is"+ num1 - num2)
elif calculation == 3:
    num1=input("insert first value")    
    num2=input("insert secon value")
    print("The multiplied value is"+ num1 * num2)
elif calculation == 4:
    num1=input("insert first value")
    num2=input("insert second value")
    print("The exponential value is"+ num1 ** num2) 

      