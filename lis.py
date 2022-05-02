from bisect import bisect_left

def get_lis_improved(sequence):
  L = [sequence[0]]
  for i in range(1, len(sequence)):
    if L[-1] < sequence[i]:
      L.append(sequence[i])
    else:
      lower_bound = bisect_left(L, sequence[i])
      L[lower_bound] = sequence[i]
  # print(L)
  return len(L)

sequence = [1,3,2,8,10,7,7,11,12,7] # L = [1, 3, 4, 8, 9]
print(get_lis_improved(sequence)) # 5 출력