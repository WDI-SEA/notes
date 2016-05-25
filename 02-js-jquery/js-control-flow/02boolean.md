#Boolean Expressions

### Equality Operator

The equality operator aka double equal (`==`) is used to compare two values.

```js
3 == 3
//true

4 == 3
//false
```

The equality operator allows type cohersion which means that if you compare two values of different types you might get unexpected results.

```js
3 == "3"
//true

0 == false
//true

1 == true
//true
```

### Identity Operator (recommended)

The identity operator aka triple quotes (`===`) works exactly like the equality operator (`==`) except it is a strict comparison operator. It does not convert types so it is more predictable and therefore the prefered method for comparision.

```js
3 === 3
//true

4 === 3
//false

3 === "3"
//false

0 === false
//false

1 === true
//false
```

### Additional Boolean Operators

There are also ways to check if a value is greater than, less than, or not equal to another value.

```js
4 > 5
//false

4 < 5
//true

4 >= 5
//false

5 <= 5
//true

4 != 5
//true

5 !== "5"
//true
```

### Logical Operators

Lastly, we can combine different boolean expressions by using logic operators.

* `&&` - and
* `||` - or
* `!` - not

```js
(4 > 5) && (5 == 5)
//false, the "and" operator requires both statements to be true

(4 > 5) || (5 == 5)
//true, the "or" operator requires at least one of the statements to be true

!(4 > 5) && (5 == 5)
//true, the "not" operator negates the first expression (!false ends up being true)
```

We'll be using these expressions throughout the course.

####Exercise

What are the results of these statements?

```js
//1
!(5 === "5") && (6 > 5) && (1 >= 0)

//2
(5 < 4) || !(3 == 3) && true
```
