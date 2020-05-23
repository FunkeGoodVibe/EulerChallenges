#!/bin/python3

import sys

getNumTestCase()
getUserInputNum()
getModulus()
getCurrentSum()

getNumTestCase():
    print("Number of test cases: ")
    t = int(input().strip()) #the number of test cases.
    return t

getUserInputNum():
    userValues = []

    for a0 in range(getNumTestCase()):
        print("What is your number: ")
        n = int(input().strip()) #the number to check multiples of 3, and 5. And to sum.
        userValues.append(n)
    return userValues

getModulus():
    answer =
    theList = getUserInputNum()
    for i in range(len(theList)):
        answer = getCurrentSum(theList[i])

getCurrentSum(currNum):
    total = 0
    for i in range(0,currNum):
        if(i%5==0) or (i%3==0):
            total = total+i
    return total
