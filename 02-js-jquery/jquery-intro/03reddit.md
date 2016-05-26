# Reddit - Independent Practice

Following the directions below to practice using jQuery:

- Go to http://www.reddit.com

- Reddit uses jQuery, so we can use our Chrome developer console to manipulate the site in real time using jQuery. Note that not everyone webpage uses jQuery, so this won't work on every webpage.

- To do this, once Reddit.com has loaded, go to your view menu in Chrome. Select View > Developer > JavaScript Console

- Once that's loaded, try entering the following command into the Chrome REPL:
```js
$('img').hide();
```

- Hit enter. All the images should have dissappeared from the Reddit.com home page. Make sure you understand why before moving on.

- Now try this:
```js
$('img').show();
```

- That should have brought all the images back. Make sense so far?

- Now with the chrome inspector, try to match the title of the first reddit post and replace the text using `.text()` or `.html()`.

- Try to replace the blue background in the header by another color using the function `.css()`.

- Now try some of the other examples we've gone over in the Chrome REPL and see what happens to the Reddit.com website. Remember, this is your laboratory --- your chance to experiment and learn. Make use of it.
