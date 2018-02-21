# Написать программу, которая выводит на экран числа от 1 до 100.
#    При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
#     а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5,
 #    то программа должна выводить слово «FizzBuzz».


defaultList = [x for x in range(101)]
i = 1
while i != len (defaultList):
    if (defaultList[i]%5 == 0 and defaultList[i]%3 == 0):
        print ('FizzBuzz')
    elif (defaultList[i]%5 != 0 and defaultList[i]%3 == 0):       
        print ('Fizz')
    elif (defaultList[i]%5 == 0 and defaultList[i]%3 != 0):    
        print ('Buzz')
    else:
        print (defaultList[i])
    i = i + 1
