firstName = "Jane"

#converts string to lowercase
print (firstName.lower() )

#to uppercase
print( firstName.upper() )

country = "nigeria"
#makes the first character of a string uppercase
print( country.capitalize() )

message = "    Hi there!, I am Darth vader!!   "

#remove whitespace from the beginning and the end of a string
print( message.strip() )

#remove spaces from the begining of a string
print( message.lstrip() )

#remove spaces from the end of a string
print ( message.rstrip() )

#length of a string
print( len(message) )

print( message.startswith(" ") )

print( message.split("a") )

#splicing a string

favFood = "Indomie is my favourite foode"
#prints the first index in the string
print( favFood[0] )

#print the second index in the string
print( favFood[1] )

#print the last character in the string
print( favFood[6] )
print( favFood[-1] )

""""
I   n   d   o   m   i   e
0   1   2   3   4   5   6
"""
print( favFood[0:3] )

print( favFood[1:])

print( favFood[:3] )

print( favFood[:] )


#find a character in a string
print( favFood.find("e") )
print( favFood.index("e") )
print( favFood.rindex("e") )

print( favFood.replace("e", "*") )






