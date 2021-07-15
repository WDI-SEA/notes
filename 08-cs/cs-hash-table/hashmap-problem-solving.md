# Problem Solving with Hash Tables

With only a few exceptions of very low-level programming languages, we can use built in hash tables for efficient problem solving. 

Due to their quick insertion and search, some problems which would take ages using nesting loops and arrays, such as the famous [two sum](https://leetcode.com/problems/two-sum/), can be solve with minimal computational power using a hash.

In Javascript, good ol' objects are hash tables, and in Python dictionaries are hash tables. We are of course familiar with using these data structures as containers for related data that needs to be grouped, but using them for problem solving means thinking about utilizing them in a different way.

## Using Hash Tables 

Consider the following problem from [Leet code](https://leetcode.com/problems/contains-duplicate/):

```python
'''
Given an integer list nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
```

This is a situation that could reasonably pop up in real life: you need to make sure every element in an array is unique. This is also very similar to what might be asked in a technical interview, so how could you solve for this?

Well, you will have to loop over the entire array at least once so you can check each element in the array, right? 

Right. 

Lets get started and write that out:

```python
def contains_duplicate(nums):
  # loop over the numbers
  for i in range(len(nums)):
    # what kind of comparison to do here?
```

Okay, we have a single loop in our algorithm, that's not too bad. Our solution has a worst case [Big O](https://www.bigocheatsheet.com/) of O(n) right now. This means the time complexity of our solution is 1:1 with how big our dataset is. 

But now here is another question: don't we need to compare every number to every other number? If each number has to be compared against all other numbers in the array, we will have to use another loop:

```python
def contains_duplicate(nums):
  # loop over the numbers
  for i in range(len(nums)):
    # compare every number to every other number
    for j in range(len(nums)):
      # do comparison of numbers here
```

We are pretty close to the solve, lets finish whats referred to as the 'naive' solution and then consider how and why to refactor. We just need to compare to the numbers from each loop to each other and return the function appropriately. Recall that we need to return `True` if we find a match ans `False` if we don't.

```python
def contains_duplicate(nums):
  # loop over the numbers
  for i in range(len(nums)):
    # compare every number to every other number
    for j in range(len(nums)):
      # if two numbers match, return early
      if nums[i] == nums[j]: 
        return True
  
  # otherwise return False if no match is found
  return False
```

You can use the following to test your function:

```python
# test the solution with some lists of numbers
print('it should return true:', contains_duplicate([1,2,3,1]))
print('it should return false:', contains_duplicate([1,2,3,4]))
print('it should return true:', contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
```

But wait! there is a bug? It always returns `True`! This is because we need to have the loops skip when they try to compare the same number:

```python
def contains_duplicate(nums):
  # loop over the numbers
  for i in range(len(nums)):
    # compare every number to every other number
    for j in range(len(nums)):
      # avoid comparing the same number to itself
      if j == i: continue
      # if two numbers match, return early
      if nums[i] == nums[j]: 
        return True
  
  # otherwise return False if no match is found
  return False
```

Our solution works great! But there is a tiny problem: since we are we have a nested loop our worst case [Big O](https://www.bigocheatsheet.com/) is O()

## Addition resources

[Leet code's](https://leetcode.com/explore/learn/card/hash-table/) introduction to hash tables