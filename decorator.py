from time import time

lists = [1, 1, 2, 3, 5,  4,5, 5, 6]  

def decorator(func):
    def wrapper(arg):
        print ("Before:", arg)
        timestampStart = float(time())
        print ("After:", func (arg))
        timestampEnd = float(time())
        timeOfProcess = timestampEnd - timestampStart
        print ("Duration of computing:", timeOfProcess)
    return wrapper

#@decorator
def dublicateDeleter (defaultList):
    # Удаляем дубликаты
    lengthOfList = len(defaultList) 
    m = 0
    i = 0
    while i != lengthOfList:
        j = m = i + 1
        while j != lengthOfList:
            if defaultList[j] != defaultList[i]:
                if m != j :
                    defaultList[m] = defaultList[j]
                m = m + 1
            j = j + 1
        i = i + 1
        lengthOfList = m
    # Создаем новый список 
    if lengthOfList != len(defaultList):
        newList = []
        i = 0
        while i < lengthOfList:
            newList.insert (i, defaultList[i])
            i = i + 1
    return (newList)

dublicateDeleter(lists)
