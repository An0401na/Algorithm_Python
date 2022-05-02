def partial_sum(arr):
    arr = [0] + arr
    partial_sum = [0] * len(arr)
    
    for i in range(1, len(arr)):
        partial_sum[i] = partial_sum[i-1] + arr[i]
        
    partial_sum = partial_sum[1:]
    print("partial_sum", partial_sum)
    
    max_partial_sum = partial_sum[0]
    
    for b in range(0, len(arr)-1):
        for a in range(0, b):
            print(a, b, partial_sum[b] - partial_sum[a-1])
            max_partial_sum = max(max_partial_sum, partial_sum[b] - partial_sum[a-1])
            
    print("max partial sum", max_partial_sum)


scores = [31,-41,57,-26,-53,58,95,-93,-23,84]
print("list", scores)
partial_sum(scores)
