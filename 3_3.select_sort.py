#Selection Sort를 recursive algorithm 설계하기
    
from array import array


def select_sort(arr, start, end):
    if end-start ==1 :
        if arr[start]>arr[end] :
            print(start)
            var=arr[start]
            arr[start] = arr[end]
            arr[end]=var
        return arr
    else :
        for i in range(start,arr.__len__()) :
            if arr[start]>arr[i] :
                print(start)
                var=arr[start]
                arr[start] = arr[i]
                arr[i]=var
                print(arr)
        select_sort(arr,start+1,end)
        return arr
            
arr=[3,0,1,8,7,2,5,4,9,6]
result=select_sort(arr,0,arr.__len__()-1)
print("result : ", result)
                
                