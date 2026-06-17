# The bane of my existence as of May 2026. Time to dig into it.

# [1,2,1,3,4,1] - 1-2-1-3-1 is the longest alternating sequence, write the tome that summons it.

# O(n^2) - length only
def AlternatingLIS(A):  # O(n^2) LIS-DP style
    n = len(A)

    UP, DOWN = [1]*n, [1]*n

    #for i in range(n):
    #    UP[i] = 1
    #    DOWN[i] = 1

    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                UP[i] = max(UP[i], DOWN[j] + 1)

            elif A[j] > A[i]:
                DOWN[i] = max(DOWN[i], UP[j] + 1)

    answer = 1
    for i in range(n):
        answer = max(answer, UP[i], DOWN[i])

    return answer


# O(n) - length only
def AlternatingLIS_Linear(A):
    if not A or len(A) == 0:
        return 0
    n = len(A)

    up = 1 # best length so far ending with an upward move
    down = 1 # best length so far ending with a downward move

    for i in range(1, n):
        if A[i] > A[i-1]:
            up = down + 1

        elif A[i] < A[i-1]:
            down = up + 1

    return max(up, down)


lst = [1, 2, 1, 2, 3, 4, 1]
print(AlternatingLIS(lst))
print(AlternatingLIS_Linear(lst))
