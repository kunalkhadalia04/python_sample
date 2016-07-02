list1 = []
list1.append('1')
list1.insert(1,'2')
list1.append('3')
list1.append('4')
list1.insert(4,'5')
list1.append('5')
list1.append('6')
list1.append('7')
print(list1)
del list1[-3]
list2 = list1.pop()
print(list1)
print(list2)
list1.remove('2')
print(list1)
list1.remove('1')
print(list1)


