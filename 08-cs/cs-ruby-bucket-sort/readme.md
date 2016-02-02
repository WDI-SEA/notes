##Bucket Sort Challenge: Sorting Papers

We need to create an algorithm that can take a list of letter grades and determine how many items there are with each grade.


**Example Input:**

```ruby
grades = ['A','B','B','C','C','C','D','F']
```

**Expected Output:**

```
A - 1
B - 2
C - 3
D - 1
F - 1
```



You must solve this problem using **RUBY**.

Use the following array for testing:

```
grades = ["A", "C", "B", "F", "C", "B", "B", "B", "B", "F", "B", "C", "F", "A", "D", "C", "B", "B", "B", "A", "D", "B", "C", "F", "C", "C", "B", "D", "A", "F", "C", "C", "A", "D", "D", "A", "C", "F", "C", "F", "D", "A", "C", "D", "B", "A", "B", "C", "C", "D", "A", "A", "C", "D", "A", "A", "F", "D", "A", "C", "C", "D", "F", "A", "B", "A", "C", "C", "B", "A", "B", "F", "A", "C", "D", "F", "D", "B", "D", "C", "A", "B", "B", "F", "F", "F", "C", "A", "F", "F", "B", "D", "C", "A", "A", "B", "D", "F", "C", "B", "D", "B", "D", "B", "F", "C", "F", "B", "B", "F", "A", "C", "D", "A", "C", "D", "A", "B", "D", "C", "D", "B", "A", "F", "C", "C", "C", "D", "A", "F", "C", "A", "D", "C", "B", "A", "F", "B", "B", "A", "A", "A", "C", "C", "B", "C", "B", "C", "D", "B", "B", "A", "F", "A", "C", "D", "C", "B", "D", "F", "C", "C", "D", "C", "B", "A", "B", "B", "B", "B", "F", "A", "A", "F", "F", "F", "B", "F", "B", "F", "D", "C", "B", "F", "A", "D", "A", "A", "A", "C", "D", "A", "A", "C", "D", "C", "D", "D", "D", "A", "D", "C", "C", "B", "B", "C", "D", "F", "C", "D", "A", "F", "C", "C", "C", "F", "B", "D", "F", "C", "A", "B", "C", "F", "C", "C", "F", "F", "B", "B", "F", "F", "C", "A", "F", "B", "C", "F", "F", "A", "C", "F", "B", "B", "F", "B", "A", "C", "B", "D", "C", "A", "B", "F", "D", "A", "C", "A", "A", "F", "F", "B", "D", "D", "B", "F", "C", "F", "F", "D", "F", "F", "B", "A", "A", "A", "C", "B", "F", "A", "C", "C", "D", "B", "A", "A", "D", "B", "F", "D", "F", "F", "D", "C", "D", "B", "F", "D", "B", "D", "C", "D", "C", "B", "C", "B", "D", "D", "A", "A", "D", "D", "A", "D", "C", "C", "B", "C", "D", "A", "B", "C", "C", "B", "A", "C", "A", "C", "C", "D", "B", "F", "A", "C", "F", "D", "B", "D", "D", "C", "A", "A", "F", "F", "C", "F", "D", "B", "F", "A", "A", "A", "C", "C", "C", "B", "B", "C", "D", "A", "F", "D", "A", "B", "F", "F", "A", "D", "D", "A", "F", "F", "C", "A", "B", "F", "F", "A", "B", "C", "B", "A", "F", "B", "F", "D", "F", "A", "D", "B", "D", "D", "D", "D", "F", "D", "D", "F", "F", "A", "A", "A", "F", "F", "F", "A", "D", "B", "C", "C", "F", "F", "F", "C", "A", "A", "D", "D", "D", "B", "B", "C", "C", "A", "F", "F", "A", "D", "F", "D", "C", "C", "C", "D", "F", "F", "F", "B", "F", "F", "D", "C", "B", "D", "F", "F", "D", "C", "C", "A", "B", "D", "C", "F", "F", "D", "F", "F", "A", "B", "F", "A", "A", "F", "B", "B", "D", "F", "F", "A", "C", "A", "F", "F", "F", "C", "F", "C", "A", "D", "C", "C", "D", "A", "B", "B", "F", "C", "B", "B", "A", "D", "C", "A", "B", "B", "F", "D", "A", "F"]
```
