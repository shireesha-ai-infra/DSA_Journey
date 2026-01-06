def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i


# Edge cases considered:
# - Empty array (loop will not run)
# - No valid pair (problem guarantees one exists)
# - Duplicate values handled correctly by dictionary

if __name__ == "__main__":
    nums = [3, 14, 5, 15]
    target = 8

    result = two_sum(nums, target)
    print("Result:", result)
