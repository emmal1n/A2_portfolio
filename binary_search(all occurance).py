# Emma Lin
# 18 June 2024
#
# binarySearch find all occurance

myList = [1,2,3,3,3,6,7,8,9,10]


print("please enter item to be found")
item = int(input()) #INTEGER

found = False #BOOLEAN
indexfound=[]

def binarySearch(myList,n):
    tempindex = -1
    upperBound = 9 #INTEGER
    lowerBound = 0 #INTEGER
    while lowerBound <= upperBound:
    
        index = int((upperBound + lowerBound)/2) #INTEGER
        if item == myList[index]:
            if n == 1:    #find the last index of the given item
                tempindex = index
                lowerBound = index + 1
            elif n == 2:    #find the first index of the given item
                tempindex = index
                upperBound = index - 1
                
        elif item > myList[index]:
            lowerBound = index + 1
        elif item < myList[index]:
            upperBound = index - 1
            
    return tempindex


maxindex = binarySearch(myList,1)
minindex = binarySearch(myList,2)

if maxindex != -1:
    for i in range(minindex,maxindex+1):
        indexfound.append(i)
    print(indexfound)
else:
    print("not found")
    
