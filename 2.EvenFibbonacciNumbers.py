#!/bin/python3

import sys

def recurse(prev, curr, next):
    prev = curr
    curr = next
    next = prev + curr

    return (prev, curr, next)

def main():

    print("Input number of test cases")
    t = int(input().strip())

    for a0 in range(t):
        print("Input the number of fib series")
        n = int(input().strip())

        prev = 1
        curr = prev + 1
        next = curr + prev

        for x in range(0, n):
            answer = recurse(prev, curr, next)

    print(answer[2])

main()
