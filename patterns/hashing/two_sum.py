"""
Problem: Two Sum

Day 1 Status: Understanding and logic only.
"""

# What is given:
# - An array of integers called nums
# - An integer called target

# What is asked:
# - Find two different elements in nums
# - Their sum should be exactly equal to target
# - Return the indices of those two elements

# Brute-force idea:
# - Pick the first element
# - Pair it with every other element
# - Check if their sum equals the target
# - If yes, return their indices

# Why brute-force is slow:
# - For every element, we scan the rest of the array
# - As the array grows, the number of checks increases rapidly

# Example:
# nums = [2, 7, 11, 15]
# target = 9
#
# Checks:
# 2 + 7 = 9  -> valid pair found
