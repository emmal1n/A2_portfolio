# Emma Lin
# 18 June 2024
#
# binarySearch

myList = [1,2,3,4,5,6,7,8,9,10]
upperBound = 9 #INTEGER
lowerBound = 0 #INTEGER

print("please enter item to be found")
item = int(input()) #INTEGER

found = False #BOOLEAN

while found == False and lowerBound <= upperBound:
    index = int((upperBound + lowerBound)/2) #INTEGER
    if item == myList[index]:
        found = True
    if item > myList[index]:
        lowerBound = index + 1
    if item < myList[index]:
        upperBound = index - 1
        
if found:
    print("found")
else:
    print("not found")
    
