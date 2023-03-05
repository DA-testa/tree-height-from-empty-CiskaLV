# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0

    for i in range(n):
        height = 0
        current = i
        while current != -1:
            current = parents[current]
            height += 1
        max_height = max(max_height, height)
        
    print(max_height)

def main():
    text = input()

    if text[0] == "I":
        print("Enter number of nodes: ")
        number = int(input())
        parents = list(map(int, input().split()))
        print(parents)
        compute_height(number, parents)

    elif text[0] == "F":
        fileName = input()
        if "a" in fileName:
            print("Invalid file name")
            return
        else:
            if "test/" not in fileName:
                fileName = "test/" + fileName
            file = open(fileName, "r")
            number = int(file.readline())
            parents = list(map(int, file.readline().split()))
            compute_height(number, parents)

    else:
        print("Invalid input")
        return
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
