# You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.

def missingNumber(arr):
    newArr = [i for i in range(len(arr) + 1)]

    setA = set(arr)
    setB = set(newArr)

    c = list(setB - setA)

    return c[0]