#ascii password generator
#using python andaconda
#TO EXECUTE -> $pythonw ctfPass.py
#by joe hollon

import random
import time
                       
#method 2 random number way(ascii) 
#set up a random number generator that took the ascii values 65-122 randomly picked the range
count = 0  
sum = 83  
sumList = []
word = []
#this loop automates me running the program a billion times    
while True: 
    
    #reset result
    result = 0 
    #always append 83 to the begening of the list
    sumList.append(83)
    word.append("S")
    
    #if sum is 1000 or count is less then 9
    #append the random number to the list
    #TODO take out the sum meaningless right now
    while count < 9:
        #change teh first random value for bigger range 
        r = random.randint(60, 122)
        sumList.append(r)
        word.append(chr(r))
        count +=1

    for sym in sumList:
        result += sym

    #swap index 0 with index 1    
    first, second = word[0], word[1]
    word[0] = second
    word[1] = first

    if result == 1000:
        print("\n===========================================================")
        print(sumList)
        print("Ascii Sum = " + str(result))
        toWord = ''.join(map(str, word))
        toWord = ''.join(map(str, word))
        print("===========================================================")
        print("\t\t  password = " + toWord)
        print("===========================================================")
        print("\n")
        break
    else: 
        #sum up all values in list
        print("\n") 
        print(sumList)
        for sym in sumList:
            result += sym
        print("Ascii Sum = " + str(result))
        toWord = ''.join(map(str, word))
        print("===========================================================")
        print("\t\t\t" + toWord)
        print("===========================================================")
        #clear list for next increment
        sumList.clear()
        word.clear()
        #set counter to 0 so second loop to execute took me forever to figure out  
        count = 0
        #tell me when at the bottom of outerLoop 
        print("Loading the next combination.........")
            