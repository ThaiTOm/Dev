def findMedianSortedArrays(n1, n2):
    ar = n1+n2
    leg = len(ar)
    ar = sum(ar)
    return ar / leg


print(findMedianSortedArrays([1, 2], [3, 4]))
