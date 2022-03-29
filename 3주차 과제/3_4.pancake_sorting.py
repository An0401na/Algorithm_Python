

def pancake_sorting(arr, end) :
   
    if end==0 :
        return arr
    else :
        tmp = max(arr[:end+1])
        maxIndex = arr.index(tmp)
        if maxIndex != 0:
            slice_a, slice_b=arr[:maxIndex+1] , arr[maxIndex+1:]
            slice_a.reverse()
            arr=slice_a+slice_b
            print(arr)
        slice_a, slice_b=arr[:end+1] , arr[end+1:]
        slice_a.reverse()
        arr=slice_a+slice_b
        print(arr)
    
        return  pancake_sorting(arr, end-1)

arr = [1,3,4,5,2]
result=pancake_sorting(arr,arr.__len__()-1)
print("result : ", result)


