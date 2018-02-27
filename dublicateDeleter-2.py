#Написать программу, которая берет исходный список и формирует новый список.
#В новом списке должны содержаться все элементы из исходного, за исключением дублей.
#Пример: [1, 1, 2, 3, 5,  4,5, 5, 6] -> [1, 2, 3, 5, 4, 6]

# Решение взято отсюда https://ru.stackoverflow.com/questions/580198/Удалить-дубликаты-в-массиве-без-использования-коллекций-java и переписано на языке python

from time import time


def dublicateDeleter (defaultList):
    # Удаляем дубликаты
    timestampStart = float(time())
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
    timestampEnd = float(time())
    timeOfProcess = timestampEnd - timestampStart
    return (newList,timeOfProcess)

lists = [1, 1, 2, 3, 5,  4,5, 5, 6]  
print ('Before:',lists)
changedLists = dublicateDeleter(lists)
print ('After:',changedLists[0])
print ('Duration of computing:',changedLists[1])























	