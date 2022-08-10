"""
for i in <Iterable>:
	#action to perform
"""

name =  "Johnny"

for n in name:
	print(n)


#list of subjects
subjects = ['Maths', 'Eng', 'Chem', 'Bio', 'CRK']

for subject in subjects:
	print(subject)

#print all even numbers from 1 to 100
for i in range(1,101):
	if i % 2 == 0:
		print(i)

numbers = [1,3,6,8,9,12,11,24]

numbersSquared = []

for n in numbers:
	nsquared = n * n
	numbersSquared.append(nsquared)

print(numbersSquared)

#sum of the first 10 -numbers
sum = 0
for i in range(1,11):
	sum = sum + i

#product of the first 10 numbers
sum = 1
for i in range(1,11):
    sum = sum * i
print(sum)
