def fibonacci_multiply(arr1, arr2,arr3, n, m) : #n은 arr1의 길이, m은 arr2의 길이
    hold =0
    for k in range(0, n+m) :
        for i in range(0,n-1) :
            hold += arr1[i]*arr2[k-i]
            arr3 = hold %10
            hold /=10
    return arr3
    
    
    

arr1=[1,2,3]
arr2=[2,3,4]
arr3=[0]*10
arr4=fibonacci_multiply(arr1, arr2,arr3,3,3)
print(arr4)