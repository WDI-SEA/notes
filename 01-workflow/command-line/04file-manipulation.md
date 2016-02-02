#File Manipulation

##Making Directories

Now that we know how to move around, it's time to make some changes. We can make directories with the `mkdir` command. Look at `man mkdir`. What's the format of the command for making a directory?

    MKDIR(1)                  BSD General Commands Manual                 MKDIR(1)

    NAME
         mkdir -- make directories

    SYNOPSIS
         mkdir [-pv] [-m mode] directory_name ...

    DESCRIPTION
         The mkdir utility creates the directories named as operands, in the order specified, using
         mode rwxrwxrwx (0777) as modified by the current umask(2).

**Operands** (or arguments or parameters) are what comes after a command, so we write `mkdir living_room` to make a new room, where we will keep our couches. Keep your directory names lowercase in almost every case. Separating words with underscores is called snake_case.

**Try This**

    ~ cd ~

    ~ mkdir living_room

What command can you use to see the results of you handywork?

###Adding and Editing Files

Let's `cd` into our new `living_room`  Look around with `ls`, and `ls -la`.  What do you see?

**Exercise**
I want my living room to have a bookshelf full of books.  Let's make a file that lists all of our books. Open Sublime Text and make a new file called `books.txt`

`subl books.txt`

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

Now try `ls -la` again.  Do you see the `books.txt` file?  Look at the contents with `cat`.

###File Permissions
The column on the left e.g.: `-rwxr-xr-x` displays the files' permissions. That is whether or not you can read, write or execute the file. These permissions can be set for the owner, group, or all users. The display also includes the type of file `d` for directory, `l` for link, `-` for files

Here's a tutorial on file permissions, if you're interested in unpacking that column: [http://en.flossmanuals.net/command-line/permissions/](http://en.flossmanuals.net/command-line/permissions/)

###echo and Redirection
**Try This**

  `echo "This bookshelf flexes under the weight of the books it holds."`

`echo` is a command that just echoes (outputs) what we give to it as arguments (same as operands). Now we want to put that line in a file called `bookshelf.txt`.

**Try This**

  `echo "This bookshelf flexes under the weight of the books it holds" > bookshelf.txt`

Using the closing angle bracket `>` in this way is called redirection. Every command that we run in the shell has an input, an output, an error output, and arguments/operands. We are saying: "Run `echo` with this string as an operand, and take the output and put it in a new file called bookshelf." Try running `ls` again, and `cat` our new file.

Two angle brackets `>>` works similarly, but it appends the string to the end of the file:

**Try This**

  `echo "It does not break, it does its job admirably" >> bookshelf.txt`

Try `cat bookshelf.txt` to see the result

**Exercise:** What's the difference between `cat` and `echo`?


###Piping

Let's look back at our books. Read out the file. Notice that the list of books is unsorted! We need to organize this using the `sort` command.

Try `cat books.txt`, and `cat books.txt | sort`. The character `|` is called the pipe. We take the output from `cat books.txt` and send it through a pipe to `sort`. The output of `cat books.txt` becomes the input of `sort`. Now send the output of `sort` to a file:

**Try This**

  `cat books.txt | sort`

**Try This**

  `cat books.txt | sort > sorted_books.txt`

Look around again to see how the room has changed.

There are dozens of powerful tools we can leverage using pipes. One of the ones you'll be using the most is `grep`.

**Try This**

  `cat books.txt | grep Mil`

See how we filtered out just the lines that contain Mil? Try grepping for something else.

> Adapted from [http://en.flossmanuals.net/command-line/piping/](http://en.flossmanuals.net/command-line/piping/)


###Moving

Now that we have our books sorted, we really don't need our unsorted list of books. `mv` stands for move, and that's how we move files and folders from place to place.

**Try This**

  `mv sorted_books.txt books.txt`

Look around and see how the room has changed.

## Copying
To copy files, we use the `cp` command. Extrapolate from the way we used `mv` to copy the file `bookshelf.txt` to add a file `second_bookshelf.txt`.

**Try This**

  `cp bookshelf.txt second_bookshelf.txt`

## Removing
`rm` is short for remove.  Use `rm` to remove the `second_bookshelf.txt` file we just created with `cp`.

**Try This**

  `rm second_bookshelf.txt`

**Important Note:** This does not send files to the trash can or recycle bin. Your files are gone forever, so be careful when using this command!

**Bonus:** `cp` and `rm` do not work on directories. What flag would be needed to remove a directory?

###Filename Wildcards

Sometimes we want to refer to a bunch of similar files, to do this we can use wildcards. The most common wildcard to use is `*` usually along with a file extension:

**Try This**

  `ls -la *.txt`

For more ideas go here: [How to Use Wildcards](http://www.linfo.org/wildcard.html)

###Mini Review - File Maniuplation

* `mkdir`
* editing files
* echo
* redirection `>` and `>>`
* piping
* moving, copying and removing
