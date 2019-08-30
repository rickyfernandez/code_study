def search_insert(nums, target):
    for i, a in enumerate(nums):
        if target == a:
            return i
        if a > target:
            return i
    return len(nums)

def _search_insert2(nums, target, lo, hi):
    mid = (lo + hi)//2
    if lo > hi:
        return mid + 1
    else:
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return _search_insert2(nums, target, lo, mid-1)
        else:
            return _search_insert2(nums, target, mid+1, hi)

def search_insert2(nums, target):
    return _search_insert2(nums, target, 0, len(nums)-1)

def search_insert3(nums, target):
    lo = 0
    hi = len(nums)

    while lo <= hi:
        mid = (lo + hi)//2
        if target < nums[mid]:
            hi = mid-1
        elif target > nums[mid]:
            lo = mid+1
        else:
            return mid
    return lo

if __name__ == "__main__":
    x = [1, 2, 6, 7]
    y = 3
    print(x, y, search_insert3(x, y))
