# Introduction to Regular Expressions

### Objectives

- Explain the purpose of regular expressions
- Describe some situations using regular expressions might be useful
- Name and Use different methods available from the Regex object in JavaScript
- Demonstrate ability to utilize regular expressions in JavaScript to match, test, and replace

### What is a regular expression?

A regular expression, often referred to as "Regex", is the idea of pattern matching in 
a string. It is not a language-specific idea, so while we will today be using regex in 
context of JavaScript, you can transfer this knowledge to any language you want to learn.

Regular expressions as we know them today were invented in the 1950s by a mathematician 
named [Stephen Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene). He described them as "*notation for expressing the algebra of regular sets.*"

### What do programmers think about regular expressions?

Regular expressions can be powerful, elegant solutions. Or they can be headaches. Or both.
Undoubtedly you've been solving a problem on Code Wars, HackerRank, CoderByte, etc. and 
noticed that someone else came up with a solution using regular expressions in just a 
line or two (compared to your miles and miles of loops to do the same thing).

As neat and elegant as regular expressions can be, for most of us, they are just one 
step up from being completely illegible. For example, the following regular expression:

```
/^\(*\d{3}\)*( |-)*\d{3}( |-)*\d{4}$/
```

This is just for validating a phone number. You can imagine things can get complicated pretty quickly. Thus, it is up to you to make the decision whether to invest time in making a nice regular expression. There are also specific situations in which you should NOT use a regular expression. For example, parsing a language, such as HTML, or when the regex code becomes more complicated than the problem it's solving.

>"Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’ Now they have two problems."

-[Jamie Zawinski](https://en.wikipedia.org/wiki/Jamie_Zawinski) (contributor to Mozilla among other things)


### Recognizing regular expressions

In JavaScript, most of the time, you will see regular expressions because they begin 
and end with a slash. For example, if you write:

```
/abc/
```

Then presumably you are going to be looking for exactly the string "abc", in that order 
to appear in whatever string you're searching in. Other times you may see people use the 
built-in Regex object. In that case, you wouldn't specify the slashes.

```
Regex("abc")
```

### Built-in stuff

There are a few abbreviations that may come after a regular expression's closing slash. Most 
important to know are 'g' for 'global' and 'i' for 'case-insensitive'. Global means that your 
regular expression will match any number of valid occurrences as opposed to just the first occurrence. Case-insensitive means that you would like 'A' and 'a' to be treated as the same character.

There are some special shortcuts you may see written with backslashes.

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
| \| | this is the or operator - e.g., x\|y will match x or y. |
| [...] | A character set (match any character that is included) |
| [^...] | A negated character set (match any character NOT in the set) |
| \d | Matches any digit (equivalent to [0-9]) |
| \D | Matches any non-digit (equivalent to [^0-9]) |
| \w | Match anything alphanumeric plus underscore |
| \W | Matches anything else other than alphanumeric plus underscore |
| \s | Matches a whitespace character |
| \S | Matches anything other than whitespace |

### How are they used?

#### Test

The test function is for when you just want a simple 'yea' or 'nay'.

```
var str = "hello there!";
/hello/.test(str); //returns true
```

```
var str = "hi there!";
/hello/.test(str); //returns false
```

#### Match

The match function is somewhat like test except that it returns you an array of the matches instead of just a true or a false. It returns null if you don't have any matches.

```
var str = "hello, hello!";
str.match(/hello/g); //returns ["hello", "hello"]
```

#### Replace

You're already familiar with the JavaScript string method `replace`. It replaces the first 
occurrence of the first parameter with the second parameter. For example:

```
var str = "abcdefabc";
str = str.replace("abc", "123");
console.log(str); //Outputs: 123defabc
```

Notice only the first occurrence of "abc" gets replaced. JavaScript doesn't have a built-in way to 
get around this, but we can do this easily with regular expressions.

```
var str = "abcdefabc";
str = str.replace(/abc/g, "123");
console.log(str); //Outputs: 123def123
```

#### Using Parentheses

```
var re = /(\w+)\s(\w+)/; //Match 2 sets of alphanumeric characters, separated by a space
var str = 'John Smith';
var newstr = str.replace(re, '$2, $1'); 
console.log(newstr); //Prints "Smith, John"
```

#### Search

Search returns the starting index of the first match. Notice that the global modifier doesn't really mean anything here. Essentially works exactly like indexOf.

```
var str = "defabcdefabc";
var result = str.search(/abc/);
console.log(result);
```

### Me Time!

For the next 30 minutes, go through the self-directed exercises.

### Revisiting an old problem with new tools

Remember when we did that problem on code wars called [dashatize-it](https://www.codewars.com/kata/dashatize-it/)? You should have an existing solution using a loop. Without looking at the answers, try and solve this problem with no loops using your new regular expression skills.

### References
- [MDN - Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Eloquent JavaScript](http://eloquentjavascript.net/09_regexp.html)
- [Self-Paced Exercises](https://regexone.com/)
- [Very challenging regex puzzles](https://regexcrossword.com/)
- [Interactive Regex Checker - Regex101](https://regex101.com/)
