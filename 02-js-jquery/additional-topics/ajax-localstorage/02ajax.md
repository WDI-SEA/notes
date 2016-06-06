#AJAX with JSON files

##Prereq: Setting up a server

To load local JSON files to our page, we'll need to run a HTTP server. If you're using BrowserSync, you won't need to worry about this. Nevertheless, it's very handy if you need a quick server, without having to install additional dependencies.

We'll be setting up a command line alias to start a Python server.

1.) edit your `zshrc`:

```
subl ~/.zshrc
```

2.) Insert this code near the bottom of the file:

###OSX

```
alias srv="_srv(){open \"http://localhost:\${1-8000}\" && python -m SimpleHTTPServer \$1}; _srv"
```

###Linux

```
alias srv="_srv(){xdg-open \"http://localhost:\${1-8000}\" && python -m SimpleHTTPServer \$1}; _srv"
```

3.) Close and restart your terminal, or run `source ~/.zshrc` to reload the file.

Now you should be able to navigate to the folder of your project (the folder containing index.html), type `srv`, and hit enter. This will start a HTTP server and open your browser to that URL.

You can go back to the site at anytime by going to `http://localhost:8000`. You can quit the server by typing `CTRL + C`

#### Aside: Wildcard Protocols and HTTP

You'll notice that Bootstrap and other CDN URLs may start with `//`. This is a wildcard protocol, which means it will use whatever protocol your site is using (`http://` or `https://`). When we're loading a file locally, our protocol is `file:///`, meaning we're accessing a file on our harddrive. Therefore, the default CDN will look for the file on our computer (instead of on the CDN) and won't find it. To fix this, we need to run a HTTP server.

##AJAX w/JSON

We can load local files, such as JSON files, using AJAX/jQuery. All we need to do is use the local file name. As a security precaution, modern browsers will only allow us to do this if we're running a HTTP server. This is to prevent sites from accessing files on our computer that we don't want them to have access to.

####Load data from local JSON file

**script.js**

```js
$.getJSON('data.json', function(data) {
  console.log(data);
});
```

**data.json**

```js
{
  "key": "value",
  "number": 5,
  "word": "taco",
  "other": [1, 2, 3, 4, 5]
}
```

The above code would load the data from `data.json` and console.log it. You can put whatever data you want in the data file. This can be useful if you have larger amounts of data that you don't want to hardcode in your js file.
