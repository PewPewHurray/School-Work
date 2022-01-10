#1-Countdown
def countdown(countFrom):
    count = []
    for x in range(countFrom, -1, -1):
        count.append(x)
    return count
print(countdown(5))

#2-Print and Return
def printAndReturn(printNum, returnNum):
    print(printNum)
    return(returnNum)
print(printAndReturn(2,3))

#3-First Plus Length
def firstPlusLength(numList):
    return(numList[0]+len(numList))
print(firstPlusLength([1,2,3,4,5]))

#4-Values Greater than Second
def valuesGreaterThanSecond(numList):
    sum = 0
    newList=[]
    if len(numList)<=1:
        return False
    for x in range(0, len(numList)):
        if numList[x] > numList[1]:
            sum+=1
            newList.append(numList[x])
    print(sum)
    return(newList)
print(valuesGreaterThanSecond([5,2,3,2,1,4]))

#5-This Length, That Value
def lengthAndValue(length, value):
    newList=[]
    for x in range(0, length):
        newList.append(value)
    return(newList)
print(lengthAndValue(4,7))