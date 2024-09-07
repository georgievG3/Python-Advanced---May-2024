def bubble_sort(nums):
    is_sorted = False
    s = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - s):
            if nums[j - 1] > nums[j]:
                is_sorted = False
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

        s += 1

numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)