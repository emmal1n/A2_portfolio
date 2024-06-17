#Emma Lin
#17 June 2024
#
#linear search

#ARRAY[0:9] OF INTEGER
myList = [3,7,11,7,9,13,0,100,24,10]

upperBound = 9 #INTEGER
lowerBound = 0 #INTEGER
index = lowerBound #INTEGER
item = -1 #INTEGER
found = False #BOOLEAN

print("please enter the item to be found")
item = int(input())

while found == False and index <= upperBound:
    if item == myList[index]:
        found = True
    index = index+1

if found == True:
    print('item found')
else:
    print('item not found')
