# Set Basics

```python
# you pass an array into set() and it gets converted to a set by removing duplicates
arr = [1, 2, 2, 3, 3, 3]
my_set = set(arr)
print(my_set)

fruits_arr = ["avocado", "tomato", "banana"]
veggies_arr = ["beets", "carrots", "tomato"]
fruits_set = set(fruits_arr)
veggies_set = set(veggies_arr)

# UNION (Things that are fruits OR veggies)
print(fruits_set | veggies_set)

# INTERSECTION (fruits AND veggies)
print(fruits_set & veggies_set)

# DIFFERENCE
print(fruits_set - veggies_set)
print(veggies_set - fruits_set)
```

If you're into this stuff, set theory goes _way_ further. Start by looking up _subsets_ and the _power set_!

_These examples are adapted from_ ***Grokking Algorithms*** _Aditya Y. Bhargava_