cars = ["abc" , 'acb' , 'c' , 'd' , '1' , 'xzy' , 'xebra']
cars.reverse()
print(str(cars) + " this is the  unsorted list in reverse" )
print(str(sorted(cars)) + " is the temporarily sorted list" ) 
cars.sort()
cars1 = cars
cars1.reverse()
print(str(cars1) + " this is the sorted list in reverse with the reverse method" ) 
cars1.sort(reverse= True) 
print(str(cars1) + "is the list sorted in reverse order") 
a = len(cars1)
print(str(a) + " is the length of the list") 


