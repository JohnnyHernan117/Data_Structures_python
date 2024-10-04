def count_rotation_binary(nums):
    lo = 0
    hi = len(nums) - 1

    if not nums:
        return 0
    if nums[lo] <= nums[hi]:
        return 0
    if len(nums) == 1:
        return 0

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]

        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] >= nums[lo]:
            lo = mid + 1
        else:
            hi = mid - 1
    return 0

