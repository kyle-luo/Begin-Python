# Example
#
# 1:
# Input: [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
# Example
#
# 2:
# Input: [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]
#
# Note:
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non - decreasing order.

def sortedSquar(A):
    result = []
    for a in A:
        result.append(a*a)
    result = sorted(result)
    return result

def sortedSquare(A):
    result = []
    for a in A:
        result.append(a * a)
    return sorted(result)

def sortedSquares(A):
    return sorted(a*a for a in A)

print(sortedSquares([-7, -3, 2, 3, 11]))