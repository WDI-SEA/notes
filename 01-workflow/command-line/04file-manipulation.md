# File Manipulation

## Common File Manipulation Commands

* `mkdir` - make a directory
* `touch` - make a file
* `mv` - move a file/directory
* `cp` - copy a file/directory
* `rm` - remove a file/directory
* `sort` - sort text files
* `grep` - search text files
* `echo` - write text to standard output
* `cat` - read and concatenate files
* `>` - redirect output to a file
* `>>` - redirect and append output to a file
* `|` - pipe output to another command

## `mkdir` - Make a directory

Make a directory using `mkdir`, which accepts the name of the new directory as an argument. Note that when naming directories, using hyphens or underscores is recommended when separating words (don't use spaces).

```sh
mkdir living_room
```

Let's `cd` into our new `living_room`  Look around with `ls`, and `ls -la`.  What do you see?

## `touch` - Create a file

Creating a file can be done by using the `touch` command. Then, the file can be opened in Sublime Text for editing.

```sh
touch books.txt
```

Now you can open that up in your editor of choice:

```sh
code books.txt
```
```sh
atom books.txt
```
```sh
subl books.txt
```

Add a few books, copy and paste the section below so we all have some books in common, and save the file.  Make sure the books you add are in the same format: `<author_given_name>, <author_last_name>:<title>`.

```
Carroll, Lewis:Through the Looking-Glass
Shakespeare, William:Hamlet
Bartlett, John:Familiar Quotations
Mill, John :On Nature
London, Jack:John Barleycorn
Bunyan, John:Pilgrim's Progress, The
Defoe, Daniel:Robinson Crusoe
Mill, John Stuart:System of Logic, A
Milton, John:Paradise Lost
Johnson, Samuel:Lives of the Poets
Shakespeare, William:Julius Caesar
Mill, John Stuart:On Liberty
Bunyan, John:Saved by Grace
```

Now try `ls -la` again.  Do you see the `books.txt` file?

## `cat` - Reading and concatenating files

A quick way to read files without opening your editor is by using `cat`.

```sh
cat books.txt
```

If we had another file, we could provide additional filenames as arguments in order to concatenate files together.

```sh
cat books.txt schedule.txt
```

## `echo` - Writing text to standard output

`echo` is a command that echoes (outputs) what we give to it as arguments.

```sh
echo "This bookshelf flexes under the weight of the books it holds."
```

At first glance, it seems too simple. Why would we need this command? Well every command that we run in the terminal has an input, an output, an error output, and arguments/options. Since `echo` produces output, we can *change* where this output will go!

## `>` and `>>` - File Redirection

Let's try redirecting the output from `echo` to a file.

```sh
echo "This bookshelf flexes under the weight of the books it holds" > bookshelf.txt
```

Using the closing angle bracket `>` in this way is called redirection. We are saying:

* Run `echo` with this string as an argument
* Take the output, and put it in a new file called `bookshelf.txt`.

Try running `ls` again, and `cat` our new file.

Two angle brackets `>>` works similarly, but it **appends** the string to the end of the file.

```sh
echo "It does not break, it does its job admirably" >> bookshelf.txt
```

Try `cat bookshelf.txt` to see the result

## `|` - Piping

Let's look back at `books.txt`. Look at the file contents. Notice that the list of books is unsorted. We need to organize this using the `sort` command.

We can use the `|` character to **pipe** output into another command, specifically the `sort` command. This is different from file redirection because we're directing output to the input of a command, not a file.

```sh
cat books.txt | sort
```

Note that if we look at `books.txt`, nothing changed. We read the contents of `books.txt` and piped the contents into sort, but the output was never saved. Luckily, we can combine piping with file redirection.

```sh
cat books.txt | sort > sorted_books.txt
```

Look around again to see how the room has changed.

## `grep` - Searching files

There are dozens of powerful tools we can leverage using pipes. One of the ones you'll be using the most is `grep`.

```sh
cat books.txt | grep Mil
```

See how we filtered out just the lines that contain Mil? Try grepping for something else. There are also additional options that can be passed to both `sort` and `grep`.

> Adapted from [http://en.flossmanuals.net/command-line/piping/](http://en.flossmanuals.net/command-line/piping/)

## `mv` - Moving files

Now that we have our books sorted, we really don't need our unsorted list of books. `mv` stands for move, and that's how we move files and folders from place to place.

```sh
mv sorted_books.txt books.txt
```

## `cp` - Copying files

To copy files, we use the `cp` command. Let's try adding a second bookshelf.

```sh
cp bookshelf.txt second_bookshelf.txt
```

Note that if we copy a folder, we'll need to use an additional option, `-r`.

## Removing

To remove files, we use the `rm` command. Let's go back and remove that second bookshelf.

```sh
rm second_bookshelf.txt
```

Note that if we remove a folder, we'll need to use an additional option, `-r` and sometimes `-f`.

**IMPORTANT NOTE:** This does not send files to the trash can or recycle bin. Your files are **gone forever**, so be careful when using this command!

## Learning More About Commands

Happily, the manual for every standard shell command is embedded in every Unix-derived system. It is as easy to access as typing `man name-of-command`. The word `man` is short for 'manual' and typing that will bring up the documentation for all the commands you will need to know.

Let's see if we can learn a bit more about the `grep` command. In your terminal, type the following:

```sh
man grep
```

This is a Unix manual page. You can exit it at any time by typing the letter 'q'. You can use the mouse pad to scroll or the arrow keys. Look in the section labeled 'SYNOPSIS' and you will see a listing of every command line option that you can use with grep. A bit further down in the 'DESCRIPTION' section you will find an explanation of every option.

Take 5 minutes and see if you can find the answers to the following questions:

1. How can I print the line number in the file where the match is found? (For example, if I grepped for `Jack` in the list of books, I want it to show that it is found on line 5.)

2. How can I also print the 3 lines *after* the line where the match is found?

3. What if I wanted to print the 2 lines before the match as well as the 3 lines after the match? (Hint: There are actually two ways to do this. What would be the cleanest way?)
