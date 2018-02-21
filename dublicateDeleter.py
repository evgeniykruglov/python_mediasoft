#Написать программу, которая берет исходный список и формирует новый список.
#В новом списке должны содержаться все элементы из исходного, за исключением дублей.
#Пример: [1, 1, 2, 3, 5,  4,5, 5, 6] -> [1, 2, 3, 5, 4, 6]

# Решение взято отсюда https://ru.stackoverflow.com/questions/580198/Удалить-дубликаты-в-массиве-без-использования-коллекций-java и переписано на языке python


#Объявляем список
defaultList = [1, 1, 2, 3, 5,  4,5, 5, 6]  
print ('Before:',defaultList)

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

print ('After:',defaultList)
print ('After:',newList)





















	
