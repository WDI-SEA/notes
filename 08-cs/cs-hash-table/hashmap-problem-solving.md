# Problem Solving with Hash Tables

## Learning Objectives

* describe what language features are hash tables
* understand the use cases of hash tables
* implement hash tables in novel problem solving situations
* get experience working on hash table challenge problems

## Introduction

With only a few exceptions of very low-level programming languages, we can use built in hash tables for efficient problem solving. 

Due to their quick insertion and search, some problems which would take ages using nesting loops and arrays, such as the famous [two sum](https://leetcode.com/problems/two-sum/), can be solve with minimal computational power using a hash.

In Javascript, good ol' objects are hash tables, and in Python dictionaries are hash tables. We are of course familiar with using these data structures as containers for related data that needs to be grouped, but using them for problem solving means thinking about utilizing them in a different way.

## Using Hash Tables 

We are going to solve a programming problem first an inefficient way or the 'naive' way, and then we will refactor to use a hash table to reduce the algorithmic complexity.

Consider the following problem from [Leet code](https://leetcode.com/problems/contains-duplicate/):

```python
'''
Given an integer list nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

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
def contains_duplicate_loop(nums: list[str]) -> bool:
  # loop over the numbers
  for i in range(len(nums)):
    # what kind of comparison to do here?
```

Okay, we have a single loop in our algorithm, that's not too bad. Our solution has a worst case [Big O](https://www.bigocheatsheet.com/) of O(n) right now. This means the time complexity of our solution is 1:1 with how big our dataset is. 

But now here is another question: don't we need to compare every number to every other number? If each number has to be compared against all other numbers in the array, we will have to use another loop:

```python
def contains_duplicate_loop(nums: list[str]) -> bool:
  # loop over the numbers
  for i in range(len(nums)):
    # compare every number to every other number
    for j in range(len(nums)):
      # do comparison of numbers here
```

We are pretty close to the solve, lets finish whats referred to as the 'naive' solution and then consider how and why to refactor. We just need to compare to the numbers from each loop to each other and return the function appropriately. Recall that we need to return `True` if we find a match ans `False` if we don't.

```python
def contains_duplicate_loop(nums: list[str]) -> bool:
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
print('it should return true:', contains_duplicate_loop([1,2,3,1]))
print('it should return false:', contains_duplicate_loop([1,2,3,4]))
print('it should return true:', contains_duplicate_loop([1,1,1,3,3,4,3,2,4,2]))
```

But wait! there is a bug? It always returns `True`! This is because we need to have the loops skip when they try to compare the same number:

```python
def contains_duplicate_loop(nums: list[str]) -> bool:
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

Our solution works great! But there is a tiny problem: since we are we have a nested loop our worst case [Big O](https://www.bigocheatsheet.com/) is O(n^2)we might want to think about refactoring.

Now this isn't too bad as long as you know the size of your data. And this isn't to knock nested loops sometimes they are super useful and necessary. But in situation where you don't how large the input data will be, you need to make your algorithms as efficient as possible: An O(n^2) is the data size squared. So an array of 10 items will take 100 iterations to complete (not bad), but an array of 10,000 items will take 10,000,000 iterations! 

This particular can be refactored to use hash map in a clever way and achieve a complexity of O(n) or better. 

Here what we will need to do is use a hash table to store every number as we loop over them. Before adding a new number, we will first check to see if it is in the hash table. If we find it, we can immediately return `True` because we know that we have a duplicate.

```python
def contains_duplicate_hash(nums: list[str]) -> bool:
  # using a dictionary as a hash table
  hash_table = {}
  # loop over the numbers
  for num in nums:
    # if the number is in the hash table -- return immediately
    if num in hash_table:
      return True
    # otherwise add the number to the hash table so it can be found
    else:
      hash_table[num] = num

  # otherwise return False if no match is found
  return False
```

Essentially we are passing some processing power off of the cpu onto the memory since we need to have a hash table of all of the numbers. Our worst case computational complexity will be O(n) but we will also raise the memory complexity to O(n). In modern computer (_ie programming for desktop computers_) you will want to pass as much complexity as you can to the memory, since processing power on desktops and laptops is finite while memory is expansive. If we were programming microchips with little or no RAM, we would strive for the opposite. 

## Lab

Congratulations, you are now ready to take on some problems of your own! 🥳

You can head on over to [this lab](https://github.com/WDI-SEA/python-hash-table-challenges) to get started! 

## Addition resources

[Leet code's](https://leetcode.com/explore/learn/card/hash-table/) introduction to hash tables