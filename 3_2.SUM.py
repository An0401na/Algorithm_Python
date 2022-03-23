#배열의 원소들의 총합을 계산하는 recursive algorithm 설계하기

def SUM(arr,start, end) :
    if end-start ==1:
        return arr[start]+arr[end]
    else :
        sum = SUM(arr, start,end-1)+arr[end]
        return sum
    
arr=[5,5,1,2,0,7]
sum = SUM(arr,0,arr.__len__()-1)
print(sum)
print(arr)


