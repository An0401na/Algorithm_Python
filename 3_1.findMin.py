#배열에서 최소값을 찾는 recursive algorithm 설계하기

from re import A


def findMin(arr, start, end):
    if end-start ==1:
        if arr[start] < arr[end]:
            return arr[start]
        return arr[end]
    else :
        a = findMin(arr, start, end-1)
        if arr[end] < a :
            return arr[end]


        return a
    
arr = [4,6,7,3,4]
min =findMin(arr, 0, arr.__len__()-1)
print(min)
print(arr)

