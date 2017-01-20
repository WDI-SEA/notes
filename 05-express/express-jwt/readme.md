# API Authentication with Express - Tokens

### Objectives
- Describe why authentication tokens are commonly used when interacting with APIs
- Add a token strategy to an application
- Authenticate a user based on their token

## Tokens, The Basics

The technique we're going to use today for API authentication revolves around **tokens**. Tokens are, at their simplest, a unique string that is usually auto-generated. They provide information that authenticates a user with a server, based on a hashing algorithm and token signature.

If we trust that we've designed it that way, then we can use a string of characters to determine the identity of a user and whether the user is logged in.

### Kicking it up a notch

That's the overall gist of what tokens do, but today we're going to use a specific type of token. It's a fairly new type of token, that's becoming widely used and trusted in web applications, and it's called a **JSON Web Token** or JWT (pronounced `jot`).

It is the same idea – a single string of characters to authenticate – only it's a string of characters built by encrypting actual information.

You can play with encoding/decoding the data over at their site as an example. Head on over to [jwt.io](http://jwt.io/#debugger).

![JWTs](https://cloud.githubusercontent.com/assets/25366/9151601/2e3baf1a-3dbc-11e5-90f6-b22cda07a077.png)

#### Just like cookies, mmmm....

In the example above, you'll notice that there are 3 parts. The payload is the one we care the most about, and it holds whatever data we decide to put in there. It's very much like a cookie; we put as few things in there as possible – just the pieces we really need.

Applications can save a JWT somewhere on a user's computer, just like a cookie. Because JWTs can be encrypted into a single string, we can _also_ send it over HTTP easily. Which means it'll work in any server/client scenario you can imagine. Quite nice.
