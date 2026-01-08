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


# EXPLAINATION

# Pattern identified:
# - Hashing (using a dictionary for fast lookup)

# Why this approach works:
# - For each number, we calculate the value needed to reach the target
# - Instead of searching the rest of the array, we check if that value
#   was already seen earlier
# - The dictionary allows us to check this instantly

# Key insight:
# - We trade a small amount of extra memory for much faster execution
# - This avoids checking all possible pairs

# Where this pattern can be reused:
# - Finding pairs with a given sum
# - Checking if an element already exists
# - Frequency-based problems
# - Subarray / substring problems using complements
