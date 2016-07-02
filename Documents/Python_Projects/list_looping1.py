list1 = ['1','2','3','4','5']
#list1.insert(0,'1') 
#list1.append('5')
print(list1)
list2 = []
x=[]
for list2 in list1:  
	x =(list1.pop())
	list2.insert(0,x)  
	
print(list2)
