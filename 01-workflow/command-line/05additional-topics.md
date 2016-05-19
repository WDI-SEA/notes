# Additional Topics

## Tab Completion

Hitting `<TAB>` autocompletes what you're typing, based on the names of the files and directories in your current directory.  Hit `<TAB>` constantly to make yourself more productive.

## Filename Wildcards

Sometimes we want to refer to a bunch of similar files, to do this we can use wildcards. Think of wildcards as placeholders for any text. The most common wildcard to use is `*` usually along with a file extension.

```
ls -la *.txt
```

The above command lists all files that end in `.txt`, but begin with anything.

## History

Lastly, there are a few different commands for checking your terminal's history. What have we been up to? Use the up and down arrow keys, or the `history` command.

```
<UP ARROW>

<UP ARROW>

<DOWN ARROW>

<DOWN ARROW>

history
```

## Environment Variables

Your current terminal session has variables called **environment variables**. There are really useful for storing commonly used commands and settings. Try typing `env` to view all of your environment variables.

You can also set your own environment variables in your shell's configuration file `~/.zshrc`. Storing the variables in the configuration file will load them for every session.

If you want to create a temporary environment variable, here's an example:

```
export MY_SETTING='subl .'
```

To access the variable:

```
$MY_SETTING
```

## Getting Help
For any command we discuss here, the command `man`, short for **manual**, will give a (hopefully) detailed explanation of that command. Sometimes that explanation will be too detailed for you. When you get lost in a man page and you want to understand it, start again from the beginning of of the **man page** and keep repeating.  Hopefully you will get further into the page each time you read it.

Many third party commands also accept the --help option, but not all, but if you get stuck it can be worth a try. Most of the commands covered in this lesson overview do not support this feature. However, commands like `git` do!


## Useful Links

* [Terminal Cheat Sheet](https://github.com/0nn0/terminal-mac-cheatsheet)
  * You may want to start bookmarking this and other resources you find helpful
* [Different Flavors of Shells](http://www.tutorialspoint.com/unix/unix-shell.htm)
  * You can try entering these shells by typing their names
  * **Example:** `bash` opens the bash shell. Type `exit` to exit the shell
* [Command Line Crash Course](http://cli.learncodethehardway.org/book/)
  * A useful tutorial similar to ours, but with a few additional commands
* [File Permissions](http://en.flossmanuals.net/command-line/permissions/)
* [Shell Scripts](http://www.howtogeek.com/67469/the-beginners-guide-to-shell-scripting-the-basics/)
  * We won't cover this much, but there's a whole scripting language for running programs in the shell! Try going through this sometime to become a productivity mastermind.
