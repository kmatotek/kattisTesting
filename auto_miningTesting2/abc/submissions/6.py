def rearrange_nums(order, nums):
    nums.sort()
    result = []
    for x in order:
        if x == 'A':
            result.append(nums[0])
        elif x == 'B':
            result.append(nums[1])
        else:
            result.append(nums[2])
    return result


nums = list(map(int, input().strip().split()))
order = input().strip()
result = rearrange_nums(order, nums)
print(' '.join(map(str, result)))