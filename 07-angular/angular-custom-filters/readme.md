#Custom Angular Filters

##Objectives

* Review the concept of filters in Angular
* Create a custom filter and utilize it in an app

##Review of Filters

Angular uses the concept of filters to easily process data before output. Filters can work on any type of data (strings, numbers, arrays, etc). There are a bunch of built-in filters and we can easily create our own.

**Basic Filter Example**

```js
{{myVar | lowercase}}
```

Outputs the value of `myVar` in to the `lowercase` filter which outputs the string as lowercase.

####Filter options

Some filters also take in optional parameters. Angular uses colons (`:`) to separate arguments for filters.

**Filter Arguments Example**

```js
//in controller
$scope.someNumber = 12345;


//in view
{{someNumber | currency}}
// Outputs: '$12,345.00'

{{someNumber | currency : '£'}}
// Outputs: '£12,345.00'

{{someNumber | currency : '£' : 4}}
// Outputs: '£12,345.0000'
```

Each filter has it's own set of options. See the [full list of built-in filters](https://docs.angularjs.org/api/ng/filter) for more details.

###Chaining filters

Filters can be chained together just like terminal commands. The output of each filter will feed into the next filter.

In this example we'll use a filter called `limitTo` which limits the length of a string or array.

**Example**

```js
//in controller
$scope.myWords = 'My String With Caps';


//in view
{{myWords | lowercase}}
//outputs: 'my string with caps'

{{myWords | limitTo : 5}}
//outputs: 'My St'

{{myWords | lowercase | limitTo : 5}}
//outputs: 'my st'
```


##Custom Filters

Creating a custom filter is fairly simple, but the syntax is a little foreign at first. Let's create a filter called `reverse` that takes a word and prints it in reverse.

**Example**

```js
myApp.filter('reverse', function() {
  return function(input, preserveWords) {
    //format word and return here
  }
});
```

A filter is created by using the `filter` method, and like the other angular methods, the first parameter is the name of the filter we want to create. The second parameter is a function that returns another function.

This inner function is the actual filter that is triggered using the same syntax as the built-in filters.

The first parameter of the inner function is the actual data that was piped in to the filter. Every subsequent parameter come from things separated by colons (again like in the built-in filters).


**Usage Example**

```js
{{someVar | reverse : true}}
```

This would trigger the inner function and set `input` to the value of `someVar` and `preserveWords` to `true`. Additional, parameters can be added in the same fashion.


###Complete filter example

The below filter will take in a word and output it reversed. If `preserveWords` is set to true, it will keep the words intact.

**Custom Filter**

```js
myApp.filter('reverse', function() {
  var reverseWord = function(word) {
    return word.split('').reverse().join('');
  }

  return function(input, preserveWords) {
    if(!input) return input;
    if(preserveWords) {
      return input.split(' ').map(function(word){
        return reverseWord(word);
      }).join(' ');
    } else {
      return reverseWord(input);
    }
  }
});
```

**Usage Example**

```js
//in controller
$scope.someText = 'This is some text';


//in view
{{someText | reverse}}
//output: 'txet emos si sihT'

{{someText | reverse : true}}
//output: 'sihT si emos txet'
```

More info: [Angular Docs - Filters](https://docs.angularjs.org/guide/filter)

### Exercises

Create a filter called 'pluralize' that accepts accepts a list length
as an input and accepts two other parameters:

* **length** - a number representing a quantity
* **singular** - a string to show if the length is 1
* **plural** - a string to show if the length is not 1

The filter should return the **singular** string if the input length
is exactly equal to one. Otherwise, it should return the plural string.

The **plural** string is an optional parameter. Detect if it is passed to the
filter. If **plural** is not passed to the filter then append the letter `"s"`
to the **singular** string.

```html
<div class="inbox">
  {{planes.length}} new {{ planes.length | pluralize: "message"}}
</div>

<div class="zoo">
  {{octopus.length}} {{ planes.length | pluralize: "octupus":"octopi"}} spotted today.
</div>
```

The filter should output the following text to the page for different input:

```
0 new messages
1 new message
12 new messages
```

```
0 octopi spotted today.
1 octopus spotted today.
23 octopi spotted today.
```

### filesize

Create a filter called `filesize` that accepts a number representing the number
of kilobytes in a file and returns a string with a human-readable size description in
the following units:

* bytes
* KB - kilobytes (1024 bytes)
* MB - megabytes (1024 kilobytes)
* GB - gigabytes (1024 megabytes)

The filter should accept an optional parameter **precision** that defaults to
2 that represents how many digits to show after the decimal place if the filesize
if larger than one megabyte. Refer to
[MDN toFixed() documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)
for details.

```
<ul ng-repeat="bytes in [123, 1024, 1536, 1048576, 1310720]">
  {{ bytes | filesize: 2}}
</ul>
```

The filter should output the following list on the page:

```
123 KB
1.00 MB
1.50 MB
1.00 GB
1.25 GB
```

### primes

Create filter called `primes` that accepts a list of numbers and returns a new
list containing only prime numbers:

```html
<ul ng-repeat="num in [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] | primes">
  <li>{{num}}</li>
</ul>
```

The filter should output the following list on the page:

```
2
3
5
7
11
13
17
```

### ago

Create a filter called `ago` that accepts a timestamp string and returns a string
representing how long ago the timestamp occurred.

The filter should support time units of years, months, days, hours, seconds
and anything occuring less than 3 seconds ago should just say 'moments ago.'

Notice the sample output properly pluralizes "1 year ago" and "2 years ago."
It's possible to use filters outside of views!
Search the internet to find out how to call one filter from inside another filter.

Use the Date object to perform date calculations. MDN has great documentation
about what methods are available on instances of the Date object. (Note: be sure
to notice that the getYear() method was deprecated because of the Y2K bug!)

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getYear

```js
var then = new Date("2010-12-05T08:03:22Z");
var now = new Date("2010-01-11T08:01:57Z");

var years = now.getFullYear() - then.getFullYear()
// ... and so on
```

Here's some sample input:

```
{{ 'May 27 2014 00:17:00 GMT-0700' | ago}}
{{ 'Sep 27 2015 00:17:00 GMT-0700' | ago}}
{{ 'Feb 27 2016 00:17:00 GMT-0700' | ago}}
{{ 'May 22 2016 00:17:00 GMT-0700' | ago}}
{{ 'May 26 2016 18:17:00 GMT-0700' | ago}}
{{ 'May 27 2016 08:17:00 GMT-0700' | ago}}
{{ 'May 27 2016 09:30:00 GMT-0700' | ago}}
{{ (new Date().toString()) | ago}}
```

Here's some sample output. Beware, time is fickle and your actual results may vary:

```
2 years ago
1 year ago
5 days ago
23 hours ago
17 minutes ago
3 seconds ago
moments ago
```
