def binary_search(lo, hi,  condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1

    return -1

def first_position(num, target):
    def condition(mid):
        if num[mid] == target:
            if mid > 0 and num[mid - 1] == target:
                return "left";
            return "found"
        elif num[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(num) - 1, condition)

def last_position(num, target):
    def condition(mid):
        if num[mid] == target:
            if mid < len(num) - 1 and num[mid + 1] == target:
                return "right"
            return "found"
        elif num[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(num) - 1, condition)

def first_and_last_position(num, target):
    return first_position(num, target), last_position(num, target)

nums = [5, 7, 7, 8, 8, 10]
target = 8
result = first_and_last_position(nums, target)
print(f"The starting and ending positions of {target} are: {result}")