from typing import List
def search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1

        elif nums[mid] == target:
            return mid

        else:
            high = mid - 1

    return -1

list = [1,2,4,5,7,8,9]

search(list,3)
