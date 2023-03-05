# python3

import sys
# import threading
import numpy

def compute_height(n, parents):
    max_height = 0
    heights = numpy.full((n,), -1)

    for i in range(n):
        if  heights[i] != -1:
            height = heights[i]
        else:
            height = 0
            current = i
            while current != -1:
                if heights[current] != -1:
                    height += heights[current]
                    break
                current = parents[current]
                height += 1
            heights[i] = height
        max_height = numpy.max([max_height, height])

    return max_height

def main():
    text = input()
    number = int
    parents = numpy.array
    if text[0] == "I":
        print("Enter number of nodes: ")
        number = int(input())
        parents = numpy.array(map(int, input().split()))

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
            parents = numpy.array(list(map(int, file.readline().split())))

    else:
        print("Invalid input")
        return
    
    print(compute_height(number, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
main()
