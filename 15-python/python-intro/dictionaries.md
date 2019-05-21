# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Dictionaries in Python

### Learning Objectives
*After this lesson, you will be able to:*
- Perform common dictionary actions.
- Build more complex dictionaries.

## Dictionaries

Dictionaries hold key value pairs just like Javascript objects. They can hold different types of values, strings, integers, even functions, so they function almost the exact same as Objects in Javascript. The only difference is that dictionary keys have to be [hashable](https://www.quora.com/What-are-hashable-types-in-Python) so that the key is immutable. That means your key must be a string or a number.

### Adding to a Dictionary

Once you've made a dictionary, you can start adding values using bracket notation. The value inside the bracket will be the key, so it has to either be hashable, or representing a variable that is.

```python
# Making an empty dictionary
Dict = {} 
print(Dict)
# => {}
  
# Adding elements one at a time 
Dict[0] = 'Hello'
Dict[2] = 'World'
Dict[3] = 1
print(Dict) 
# => {0: 'Hello', 2: 'World', 3: 1}
  
# Adding set of values  
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print(Dict) 
# => {0: 'Hello', 2: 'World', 3: 1, 'Value_set': (2, 3, 4)}
```
The same bracket notation is used for reassigning values. 

```python
# Updating existing Key's Value 
Dict[2] = 'Nerd'
print(Dict)
# => {0: 'Hello', 2: 'Nerd', 3: 1, 'Value_set': (2, 3, 4)}
```
This is a dictionary, so if you want to nest dictionaries, you can!

```python
# Adding Nested Key value to Dictionary 
five = 5
Dict[five] = {'Nested': {'1' : 'Goodbye', '2' : 'Friends'}} 
print(Dict)
# => {
#   0: 'Hello', 
#   2: 'Nerd', 
#   3: 1, 
#   'Value_set': (2, 3, 4), 
#   5: {
#     'Nested': {
#       '1': 'Goodbye',
#       '2': 'Friends'
#       }
#     }
#   }
```

### Things to know
While it is bad form and useless, it is possible to have have a dictionary with two keys that are the same, your python code will still run. If this happens, the last value will be the one that’s kept  

Keys are case-sensitive, so if you are reassigning a value and capitialise your key, you'll just create a entry in your dictionary.

## Looping through a dictionary

You can iterate through a dictionary using the same for loops we use for lists and strings.

To print out every value in the dictionary we run the loop like so:

```python
for key in Dict:
    print(Dict[key])
```
