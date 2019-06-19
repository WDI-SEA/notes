# Introduction to Regular Expressions

### Objectives

- Explain the purpose of regular expressions
- Describe some situations using regular expressions might be useful
- Name and Use different methods available from the Regex object in JavaScript
- Demonstrate ability to utilize regular expressions in JavaScript to match, test, and replace

### What is a regular expression?

A regular expression, often referred to as "Regex", is the idea of pattern matching in a string. It is not a language-specific idea, so while we will today be using regex in context of JavaScript, you can transfer this knowledge to any language you want to learn.

Regular expressions as we know them today were invented in the 1950s by a mathematician named [Stephen Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene). He described them as "*notation for expressing the algebra of regular sets.*"

Regular expressions are used in many areas of computer science:

- Programming languages
- Word processors & text editors
- System utilities like Unix's `grep`

### What do programmers think about regular expressions?

Regular expressions can be powerful, elegant solutions. Or they can be headaches. Or both. Undoubtedly you've been solving a problem on Code Wars, HackerRank, CoderByte, etc. and noticed that someone else came up with a solution using regular expressions in just a line or two (compared to your miles and miles of loops to do the same thing).

As neat and elegant as regular expressions can be, for most of us, they are just one step up from being completely illegible. For example, the following regular expression:

```
/^\(*\d{3}\)*( |-)*\d{3}( |-)*\d{4}$/
```

This is just for validating a phone number. You can imagine things can get complicated pretty quickly. Thus, it is up to you to make the decision whether to invest time in making a nice regular expression. There are also specific situations in which you should NOT use a regular expression. For example, parsing a language, such as HTML, or when the regex code becomes more complicated than the problem it's solving.

>"Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’ Now they have two problems."

-[Jamie Zawinski](https://en.wikipedia.org/wiki/Jamie_Zawinski) (contributor to Mozilla among other things)


### Recognizing regular expressions

In JavaScript, most of the time, you will see regular expressions because they begin and end with a slash. For example:

```
/abc/
```

This is a regular expression that looks for exactly the string "abc", in that order to appear in whatever string you're searching in. There are never quotes around regular expressions when written in this form.

Other times you may see people use the built-in Regex object. In that case, you wouldn't specify the slashes.

```
Regex("abc")
```

### Regular Expression Patterns

To start, we're going to use the code playground, [codepen.io](http://codepen.io/pen/), to play with regex in HTML `<input>` elements.

Create a new pen, and hide the JS pane. In the HTML pane, let's add a simple form:

```html
<form>
  text: <input type="text" required pattern="Fred">
</form>
```

Put this in your pen's CSS pane:

```css
body {
  font: 14pt Helvetica;
}
form {
  padding: 50px;
  border: 4px solid lightgreen;
  border-radius: 20px;
}
form:invalid {
  border-color: yellow;
}
input {
  font: 14pt Helvetica;
  margin: 10px;
  padding: 4px;
}
input:invalid {
  border-color: red;
}
```

We won't need to change our CSS going forward, so go ahead and hide the CSS pane.

### Validating Text in an Input Element

HTML5 `<input>` elements have a `pattern` attribute just for regex patterns. If the text in the `<input>` does not **completely** match the regular expression:

	- The submit button will not submit the form to the server.

	- The `<form>` will have the `:invalid` CSS pseudo-class applied to it.

#### Literal Characters

The first type of characters within a regex pattern we can look for are **literal characters**. A **literal** is the most basic of the regex characters. They are _literally_ the character we want to match.

The first regex we have put in our `<input>`, `pattern="Fred"`, has a pattern, `Fred` that consists entirely of literal characters.

Type "Fred" and you will see the form's border turn green indicating a match!

#### Character Classes

Next up is a **character class**.  They tell the regex engine to match only one of several characters placed within square brackets.

Lets change our pattern to `gr[ae]y`. Check it out!

You can use a hyphen inside of a character class to specify a range of characters. For example, `[5-9]` will match a single digit of 5 to 9. You can use more than one range too. This pattern, `[0-9a-fA-F]`, would would match any single hexadecimal digit regardless of case.

Character classes are great for matching frequently misspelled words like `li[cs]en[cs]e`.

#### Question!

- **What regular expression could be used to match your name whether it is capitalized or not?**

#### Negated Character Class

Putting a `^` (caret) symbol after the opening `[`, means match any character **except** the character(s) in the brackets. So, `p[^ua]` will match the letter `p` followed by any single character except a `u` or `a`.

#### Shorthand Character Classes

Because character classes are used so often, there are several _shorthand character classes_ available. For example, instead of using `[0-9]` to match a digit, you can use `\d` instead.

Here are more shorthand character classes:

* **`\w`** will match any alphanumeric character, including digits and the underscore character.

* **`\s`** will match any "whitespace" character, including a space, tab, newline and carriage return.

* **`.`** (period) will match any character except line breaks.

Google will be your friend when working with regular expressions, unless you work with them frequently, there's no way to remember all this stuff!

#### Negating the Shorthand Classes

Interestingly, the uppercase versions of the previous shorthands match just the opposite of the lowercase versions:

* `\D` will match any character except a digit.

* `\W` will match anything but an alphanumeric character (and underscore).

* `\S` will match anything except a space, tab, newline or return.

- Note that there is no shortcut character class to match a letter from the alphabet only, so we must use: 
* `[a-z]` (lowercase)
* `[A-Z]` (uppercase)
* `[a-zA-Z]` (upper or lowercase)

#### Exercise (5 mins)

Based upon what you've learned already, work with a pair and write a regex pattern that will match the following:

The word "File", followed by a space and two uppercase letters from the alphabet, followed by a hyphen and three digits, except that the first of the three digits cannot be a zero.

For example, this text would be a match: `File XY-123`

#### Quantifiers

In the previous exercise/solution, we repeated the same character classes when we wanted to match more than one. Well, there's a better way using **quantifiers**.

There are four different quantifiers:

* **`{}`**
* **`*`**
* **`+`**
* **`?`**

Let's see how they work...

We use curly braces to specify a specific quantity, or range of quantities, to repeat a literal character, character class, etc. For example, `\d{3}` would match three digits.

We can also specify a range like `[A-Z]{1,5}`, which would match between 1 and 5 capital letters. A range from a number to infinity can be created by leaving off the second number such as this `{5,}`.

Note that regular expressions by default are "greedy", that is, they will match as many characters as possible (longest possible match).

#### Other Quantifiers

In addition to the `{min,max}` quantifier, there are repetition operators:

* **`*`** - the star symbol will match the preceding character class zero or more times.
* **`+`** - the plus symbol will match the preceding character class one or more times.
* **`?`** - the question mark will match the preceding character class zero or one time.

#### Escaping Special Characters

We've seen how certain characters such as these, `/*+?.[]{}`, have special meaning in regular expressions. That being the case, how do we match these special characters as a literal character? For example, what if you wanted a pattern to match a number that includes a decimal point?

To accomplish this, you have to _escape_ the special character by preceding it with a `\` (backslash), for example, `\+`, would match the plus symbol.

Note that we do not have to escape special characters within a _character class_ (square brackets).  So, if you wanted to match a plus or minus sign, you could use this pattern: `[+-]`.

#### Alternation

Alternation allows us to easily search for one of several characters or words. Let's say you want a single regex that will match any of these sentences:

_I have a dog._
_I have a cat._
_I have a bird._
_I have a fish._

This would do the trick:

```js
/I have a (dog|cat|bird|fish)\./
```

#### Anchors and Boundaries

Anchors and boundaries are unique in that they don't match a character, instead they match a _position_. They allow us to write patterns that match strings that contain only the characters we are interested in and only if they are isolated the way we want them to be.

The `^` symbol is used to match the start of the line. This is very useful for processing a file containing multiple lines.

The `$` symbol matches the end of the line.

For example, without boundaries, the regex `/dog/` will return _true_ when tested against any of these strings: "dog", "dogs" and "My dog is named Spot".  However, the regex `/^dog$/` will match only the string "dog" and when there is no other text in the line. The boundaries ensure that "dog" comes immediately after the start and immediately before the end of the string being tested.

Let's test the pattern, `cat`, with anchors (`/^cat$/`), and without (`/cat/`), against the strings "cat" and "catsup".

There is also `\b`, which matches a position called a _word boundary_. The `\b` will match any of the following:

* Before the first character in the string.
* After the last character in the string.
* Between two characters in the string where one character is a word character and the other is a non-word character such as a space, tab, or newline.

The `\b` easily allows us to search for whole words only.

This is how could use the string `match()` method to return the matches by passing in a regex:

```js
// try with no word boundary
var re = /cat/g;
var matches = "The catsup was eaten by the cat".match(re);
// ["cat", "cat"]

// try using word boundary
var re = /\bcat\b/g;
var matches = "The catsup was eaten by the cat".match(re);
// ["cat"]
```
The `g` at the end of the regex is the _global_ flag and it tells the regex to search for all matches, instead of just the first.

#### Parentheses - Grouping

Parentheses are used inside regular expressions to create groups that can then have a quantifier applied to the group as a whole. Whereas, the square brackets character class, `[]`, represents a **single** character to match, the parentheses, `()`, represent a **group** of characters to match.

Let's say we wanted to match a computer's IP Address. Ignoring the fact that we should limit the numbers to between 0 and 255, we could write something like this:

```js
/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/
```

But using grouping we can shorten this to:

```js
/(\d{1,3}\.){3}\d{1,3}/
```

#### Parentheses - Capturing

Parentheses can also be used to define **capture** groups. Capturing is when matched text is "captured" into numbered groups. These groups can then be reused with a process called backreferencing.

```js
// Match 2 sets of alphanumeric characters, separated by a space
var re = /(\w+)\s(\w+)/; 

var str = 'John Smith';
var newstr = str.replace(re, '$2, $1');

console.log(newstr); //Prints "Smith, John"
```

Capturing is beyond the scope of this lesson. Here's [one of several articles out there](http://techbrij.com/javascript-backreferences-string-replace-regex) should the mood strike you.

### Cheatsheet of Common Tokens

| Character | Meaning |
| ----- |--------------------------------------------------------------------------|
| \ | An escape character. If you mean a literal backslash, it must escape itself! |
| ^ | Match the beginning of a string |
| $ | Match the end of a string | 
| * | Match the preceeding expression 0 or more times |
| + | Match the preceeding expression 1 or more times |
| {n} | Match the preceeding expression exactly n times. |
| {n,m} | Match at least n times, but not more than m times. |
| . | Match any single character other than the newline character |
| ? | Match the preceeding expression 0 or 1 times. Also can be used as a modifier on * and + to make them match the fewest valid characters (non-greedy) as opposed to the most valid characters (greedy) |
| (...) | putting an expression in parenthesis causes the match to be remembered and saved for later use. |
| &#124; | this is the or operator - e.g., x &#124; y will match x or y. |
| [...] | A character set (match any character that is included) |
| [^...] | A negated character set (match any character NOT in the set) |
| \d | Matches any digit (equivalent to [0-9]) |
| \D | Matches any non-digit (equivalent to [^0-9]) |
| \w | Match anything alphanumeric plus underscore |
| \W | Matches anything else other than alphanumeric plus underscore |
| \s | Matches a whitespace character |
| \S | Matches anything other than whitespace |

### Regular Expressions in JavaScript

In JavaScript, regular expressions are special objects that can be created using a _regular expression literal_, or the _RegExp()_ constructor function. The literal syntax uses forward slashes to delimit the regex:

```js
var re = /cats?/;
```

The literal syntax is the best option if you know the pattern you want to use in advance.  However, using the constructor approach allows you to pass in a string variable to create a regex dynamically:

```js
var s = "cats?";
var re = new RegExp(s);
```

#### Test

A regex object has a `test()` method that returns `true` if there is at least one match:

```js
var re = /cats?/;
re.test('fatcat');   // returns true

var str1 = "hello there!";
/hello/.test(str1);   // returns true

var str2 = "hi there!";
/hello/.test(str2);   // returns false
```

#### Match

The match function is somewhat like test except that it returns you an array of the matches instead of just a true or a false. It returns null if you don't have any matches.

```js
var str = "hello, hello!";
str.match(/hello/g);   // returns ["hello", "hello"]
```

#### Replace

You're already familiar with the JavaScript String method `replace`. It replaces the first occurrence of the first parameter with the second parameter. For example:

```js
var str = "abcdefabc";
str = str.replace("abc", "123");
console.log(str);    // Outputs: 123defabc
```

Notice only the first occurrence of "abc" gets replaced. JavaScript doesn't have a built-in way to get around this, but we can do this easily with regular expressions.

```js
var str = "abcdefabc";
str = str.replace(/abc/g, "123");
console.log(str);    // Outputs: 123def123
```

#### Search

Search returns the starting index of the first match. Notice that the global modifier doesn't really mean anything here. Essentially works exactly like indexOf.

```js
var str = "defabcdefabc";
var result = str.search(/abc/);
console.log(result);
```

### Additional Exercises

Now you can have some fun practicing writing four more regular expressions. Solutions are listed at the very bottom of the page, so don't peek unless you need help.

#### Practice #1

Match an _American Express Credit Card Number_ which always begin with 34 or 37 and totals 15 digits.

#### Practice #2

Match a full U.S. Phone Number: **+1-(555)-555-5555**

#### Practice #3

A date in the format: YYYY-MM-DD. YYYY can start with either 19 or 20 only. DD can be anything from 01 to 31, regardless of the month.

#### Practice #4

An integer between 0 and 255<br>This is difficult, remember to use the "alternation" (|) operator.

### References
- [MDN - Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Eloquent JavaScript](http://eloquentjavascript.net/09_regexp.html)
- [Self-Paced Exercises](https://regexone.com/)
- [Very challenging regex puzzles](https://regexcrossword.com/)
- [Interactive Regex Checker - Regex101](https://regex101.com/)

#### Solution - 1 of 4

`/3[47]\d{13}/`

#### Solution - 2 of 4

`/\+1-\(\d{3}\)-\d{3}-\d{4}/`

#### Solution - 3 of 4

`/(19|20)\d\d-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])/`

#### Solution - 4 of 4

`/(2[0-4][0-9]|25[0-5]|[01]?[0-9]?[0-9])/`
