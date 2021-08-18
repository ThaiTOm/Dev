def findClosestElements(arr, k, x):
    lo = 0
    hi = len(arr) - k - 1
    while(lo <= hi):
        mid = lo + (hi - lo) // 2
        st = arr[mid]
        end = arr[mid + k]
        if x < st:
            hi = mid - 1
        elif x >= end:
            lo = mid + 1
        else:
            if abs(x - st) <= abs(x - end):
                hi = mid - 1
            else:
                lo = mid + 1
    return arr[lo: lo + k]
