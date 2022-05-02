# 2.1_(b)
# “정렬후 회전된 배열”이란 (5, 8, 9, 2, 3, 4)와 같은 배열을 말한다.
# 즉, 정렬이 된 후에 회전 연산이 0회 이상 적용된 배열이다.
# 회전 연산이란 배열의 마지막 원소가 처음으로 이동하고 나머지 원소들이 오른쪽으로 한 칸씩 이동하는 것을 말한다.
# 예를들어, (2, 3, 4, 5, 8, 9)는 정렬된 배열이고 여기에 회전 연산을 1회 적용하면 (9, 2, 3, 4, 5, 8)이 되고
# 여기에 회전 연산을 추가로 2회 적용하면 (5, 8, 9, 2, 3, 4)가 된다.
# 따라서 (5, 8, 9, 2, 3, 4)는 정렬후 회전된 배열이다.
# (b) 정렬후 회전된 배열A [0..n-1]가 회전연산을 몇번 적용한 것인지 알아내는 알고리즘을 설계하고 분석하시오.

A = [4,5,6,8,1,2,3]         # 해당하는 배열
F = 0                       # 배열의 처음 원소의 인덱스 번호
L = len(A)                  # 배열의 총 길이

def NumRotAccount(A, F, L):
    M = (F+L)//2            # 배열의 중간 원소의 인덱스 번호
    # 회전함의 따라 최대 값의 인덱스가 0부터 +1씩 증가하므로, 최대값의 인덱스 번호의 +1이 회전연산의 횟수이다.
    # 하지만, 회전을 안했을 때의 경우에는 0회전인지, 배열의 길이만큼 회전한건지 알수가 없기 떄문에, 생각하지 않았다.
    if L-F == 1:            # 재귀를 반복하면서 나누어진 배열의 길이 - 배열의 처음 원소의 인덱스 번호를 뺀 결과가 인접한 배열의 길이가 2이라는 것을 의미하며,
        if A[F] >= A[L]:    # 배열의 재귀를 반복하면서, 나누어진 배열의 길이가 2가 되었으므로,
            return F+1      # 두 개의 원소 중, 더 큰 원소의 인덱스 번호의 +1의 값을 return한다. 
        else:
            return L+1
    if A[F] >= A[M]:        # 배열의 길이가 2만큼 나누어지지 않았기 때문에 배열의 길이가 2가 될 때까지 재귀를 반복한다.
        return NumRotAccount(A, F, M)   # 배열의 처음 원소가 마지막 원소보다 크다면, M을 기준으로 나누어진 배열의 앞 부분의 배열이 재귀로 넘어간다.
    else:
        return NumRotAccount(A, M, L)   # 위와 반대의 경우, 뒷 부분의 배열이 재귀로 넘어간다.

print(NumRotAccount(A, F, L))

# 시간복잡도 : T(n) = T(n/2) + O(1) = O(logn)이다.
# 정확도 : 배열이 정렬만 되어있을 경우에는, 0회전인지 배열의 길이만큼 회전한 것인지 알 수 없으므로, 해당 케이스를 제외하고는
# 정렬후 회전된 배열의 회전연산의 횟수를 모두 찾아낼 수 있으므로, 정확도는 100%이다.