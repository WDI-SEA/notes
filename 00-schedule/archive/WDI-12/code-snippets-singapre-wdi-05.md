# Code Snippets From Lecture

## Week 4

### Node Express EJS Templates

Here's a project all set up with basic static file serving,
some route configruations, and some advanced ejs templates.

https://github.com/ga-students/simple-node-express-ejs-template

### Redit API Search

Reddit allows you to search their own content. Here's their own description of
how the search endpoint of their API works: [Reddit Search API Documentation](https://www.reddit.com/dev/api/#GET_search)

Here's how you can make a request to search their API for kittens:

```
$.get('https://www.reddit.com/search.json', {
  q: 'kittens'
  }).done(function(data) {
    console.log(data);
  });
```

## Week 3

Detecting keyboard interactions, moving things: <https://repl.it/DBp4>

Sorting, Reverse Sorting, and Shuffling: <https://repl.it/CzDF/0>

## Week 2

### Array Equality

a function that returns true if two arrays are equal: <https://repl.it/Cqzr/1>

### JavaScript Clock

Look at the commits on the `sol` solution branch to see different
implementations:

<https://github.com/ga-students/js-clock-intervals/commits/sol>

### Intervals and Timeouts
- a simple interval, timeout counter: <https://repl.it/CqVJ>
- ding, and stop ding: <https://repl.it/CqV8/2>
- cat meowing, dog barking: <https://repl.it/CqV8/3>


### Scopes and Closures
- scope example: <https://repl.it/CqS4/4>
- bank account closure: <https://repl.it/CqTA/2>
- bad vs good scope/closure examples: <https://repl.it/CqVY/2>

### Iterators
- .reduce() example: <https://repl.it/CqZD>
- .filter() .map() .reduce() in one breath: <https://repl.it/CqZH/0>
