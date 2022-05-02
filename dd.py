def lis(arr):
    if not arr:
        return 0
    
    ret = 1
    for i in range(len(arr)):
        nxt = []
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret	


scores = [1,6,7,8,10,7,8,11,6,15]
a = lis(scores)

print(a)