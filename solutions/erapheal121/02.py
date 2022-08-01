#question 1
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#question2
list1 = ["P", "y", "t", "h"]
list2 = ["o", "n"," ", "R", "ocks"]
print(list1+list2)

#question3
list1 = [10, 20, [300, 400, [2000, 3000], 500], 30, 40]
list1[2][2].append(4000)
print(list1)

#question4
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)

print(list1)
#question5
list1 = [5, 10, 15, 20, 25, 50, 10]
list1[1]= 100
list1[5]= 100
print(list1)


#question6
list1 = [5, 20, 15, 20, 25, 50, 20]
list1.remove(20)
list1.remove(20)
list1.remove(20)
print(list1)