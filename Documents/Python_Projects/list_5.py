list1 = ['1','2','3','4','5','6','7']
print("this is the unedited list 1 \t" + str(list1))
list2 = []
list2.append(list1.pop())
print("this is list 2 with a value of list1 which is " + str(list2[0]))
list1.insert(7,list2[0])
print("this is list one with the  last int returned back to the list" +  str(list1)) 
