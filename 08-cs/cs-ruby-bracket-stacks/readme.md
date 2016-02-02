#Challenge: Bracket Matching

Create a method in ruby called `test_brackets` that takes a `string` and determines if all brackets are correctly matching / nested (returns `true` or `false`). This is code could be used as part of a system to detect syntax errors in code.

It should check for the following: `[ ]`,`{ }`,`( )`

###Usage Examples

```rb
test_brackets('abc(123)')
#returns true

test_brackets('abc(123')
#returns false -- missing closing bracket

test_brackets('a[bc(123)]')
#returns true

test_brackets('a[bc(12]3)')
#returns false -- inproperly nested

test_brackets('a{b}{c(1[2]3)}')
#returns true

test_brackets('a{b}{c(1}[2]3)')
#returns false -- inproperly nested

test_brackets('()')
#returns true

test_brackets('abc123yay')
#returns true -- no brackets = correctly matched
```
