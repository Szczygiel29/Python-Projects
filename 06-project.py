def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l,target, midpoint+1, high)

print(native_search([1, 2, 12, 34, 54, 123], 54))
print(binary_search([1, 2, 12, 34, 54, 123], 54))
