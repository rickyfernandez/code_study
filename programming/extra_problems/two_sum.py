def two_sum(nums, target):
    store = {}
    for i in range(len(nums)):
        if target - nums[i] not in store:
            store[nums[i]] = i
        else:
            return [store[target-nums[i]], i]

if __name__ == "__main__":
    x = [2, 7, 11, 15]
    print("x", x)
    print("solution", two_sum(x, 9))
