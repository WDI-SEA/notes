# Environment Variables with Foreman

## Objectives

* Define what an environment variable is
* Explain why certain variables should not be committed to a codebase
* Use different methods to create environment variables.

## Environment Variables

Environment variables are values that exist in a computer's current environment. They can affect how a computer runs, or how certain commands are executed. If you open up the following file:

```bash
subl ~/.zshrc
```

You'll see some examples of environment variables. This is actually one way to create new environment variables. You can add them directly to `~/.zshrc` and they'll be loaded when your shell starts. Example:

```
TEST=testvalue
```

To avoid restarting the terminal, run the `~/.zshrc` file again.

```bash
source ~/.zshrc
```

## Why use Environment Variables?

Frequently, we'll have variables that are unique to a particular computer. An example is the `PORT` variable we looked for when deploying to Heroku. We also use variables to avoid committing values that are either sensitive or vary from machine to machine.

When we use API keys that are meant to be private/secret, this is a case where we **DO NOT WANT TO COMMIT THE VALUES**. These values can vary, but if a malicious user gets ahold of them, they can cause disastrous results, especially if the values access an account that costs money or resources.

## Using Foreman

An alternative to adding environment variables to `~/.zshrc` is to use `foreman`. Install it by running:

```bash
gem install foreman
```

Now, we can store environment variables for a particular project in a `.env` file, like so:

```
SECRET_KEY=asdfasdfasdf
OTHER_TOKEN=234lksdfasdf
```

Then, in order to `load` these variables into the environment, we can run `foreman run` before our application. So for a node app, we'd run:

```bash
foreman run nodemon
```

To access these variables in a Node app, we can use the following syntax:

```js
console.log(process.env.SECRET_KEY);
console.log(process.env.OTHER_TOKEN);
```

For a Ruby on Rails app, we'd run:

```bash
foreman run rails s
```

To access these variables in a Rails app, we can use the following syntax:

```rb
puts ENV['SECRET_KEY']
puts ENV['OTHER_TOKEN']
```

