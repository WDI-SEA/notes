![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Command Line

##Objectives

* Define what a terminal window is
* Identify commands used for navigating directories
* Identify commands used for manipulating files (moving, copying, editing, removing)
* Distinguish between absolute and relative paths
* Apply commands towards everyday problems and workflows

##Living in the Command Line
Web programmers have to live on the command line. It gives us fast, reliable, and automatable control over computers. Web servers usually don't have graphical interfaces, so we need to interact with them through command line and programmatic interfaces.  Once you become comfortable using the command line, staying on the keyboard will also help you keep an uninterrupted flow of work going without the disruption of shifting to the mouse.

Pretty cool, huh? Let's get started! But first...

**Important Note:** You should not copy / paste scripts from web pages and run them in your terminal until you have read them and understand what they do, bad things can happen, particularly with sudo and su commands.

Regarding scripts which you may find on the web while searching for solutions, assume they are going to do something bad.

## Introduction
### What is the Terminal?

![Terminal Window](http://i.stack.imgur.com/DjFOZ.png)

Terminal is a modern version of an 'original' **User Interface** for Unix-based computers. At that time a [Text Terminal](http://en.wikipedia.org/wiki/Computer_terminal#Text_terminals) is all you would have seen, no windows, no mouse. Because of this history, it's very powerful but sometimes a little cryptic.

Don't worry though, with a bit of practice you'll be flying around like a pro!

Although they technically mean slightly different things, the following terms are types of Terminal Environment

*  Shell
*  bash ('Bourne-Again shell')
*  Command Line
*  Text Terminal
*  DOS Prompt (on windows machines)
*  SSH (on remote machines)
*  Bourne Shell
*  csh
*  ksh
*  sh
*  [UNIX Shell](http://en.wikipedia.org/wiki/Unix_shell)

###Opening the Terminal
**Follow Along:**

1. In the top right of the screen click the Magnifying Glass icon to bring up 'Spotlight' and type 'Terminal'
2. Once Terminal starts locate the icon in the doc and select `Options -> Keep In Dock` so that it's always handy

---

##Current Working Directory
The file structure you see in the Terminal is the same as the one you see in the `Finder` application. Finder tends to hide some of the folders from you to keep things simple for most users, but everywhere that you go in Finder is accessible through 'Terminal'.


###Where am I?
Typically the shell will start in your `HOME` directory, each user has their own `HOME` directory, but on your computer it is common for you to be the only real user. At any given time a terminal shell process has one **current working directory**

**Follow Along:**

    ~ pwd

    /Users/brian

For me this is `Users/brian` What is the **current working directory** of your shell process?

Wherever we are, `pwd` (short for **print working directory**) will show us what directory we are in.

**Follow Along:**

    ~ open .

Wherever we are, `open .` opens a Finder window in the current directory, this can be handy for going between the terminal and Finder interfaces.


## Looking Around
What can we find out about the  **current working directory** ?

One of the most useful commands is:

    ~ ls

Which lists the files and directories in the current working directory:


    ~ ls

    Applications   Pictures  gitshell.sh rorshell.sh
    Desktop   Library   Public    hashes  rorshellws.sh
    Documents Movies    bin   helloroom work
    Downloads Music   git_profile.sh  phpshell.sh

Personally I find this a little difficult to read so I use the long form (using a flag):

    ~ ls -l

    total 10
    drwxr-xr-x    2 brian  staff    68 Dec  4 15:13 Applications
    drwx------+   6 brian  staff   204 Mar 23 18:20 Desktop
    drwx------+  11 brian  staff   374 Feb 27 10:57 Documents
    drwx------+ 141 brian  staff  4794 Apr  5 08:04 Downloads
    drwx------@  56 brian  staff  1904 Apr  4 21:58 Library
    drwx------+   3 brian  staff   102 Nov  4 10:49 Movies
    drwx------+   8 brian  staff   272 Mar  5 15:48 Music
    drwx------+  20 brian  staff   680 Mar 23 12:53 Pictures
    drwxr-xr-x+   5 brian  staff   170 Nov  4 10:49 Public
    -rwxr-xr-x    1 brian  staff   184 Nov  8 16:41 git_profile.sh

Now I can see a lot more clearly what files are in my current working directory. Some of these items are files, some are directories.

The `ls` command can take a directory as an argument

    ~ ls -l Documents/

    total 3
    drwxr-xr-x   4 brian  staff      136 Feb 22 20:01 Rails
    -rw-r--r--@  1 brian  staff  8154896 Feb 27 10:57 Profile.png
    -rw-r--r--@  1 brian  staff  6258658 Feb 27 10:57 Profile2.png

The `ls` command can also take a wildcard as an argument (placeholder for any set of characters).

    ~ ls -l Documents/*.png

    -rw-r--r--@ 1 brian  staff  8154896 Feb 27 10:57 Documents/Profile.png
    -rw-r--r--@ 1 brian  staff  6258658 Feb 27 10:57 Documents/Profile2.png

## Hidden Files
Have you ever heard of hidden files? Well it's true, they are real! We can see them by using another flag:

```
  ~ ls -la

  total 17
    drwxr-xr-x+  76 brian  staff   2584 Apr  6 10:30 .
    drwxr-xr-x    6 brian  admin    204 Nov  4 10:47 ..
    -rw-r--r--@   1 brian  staff  15364 Apr  2 16:00 .DS_Store
    -rw-------    1 brian  staff   8949 Apr  1 17:21 .bash_history
    -rw-r--r--    1 brian  staff    285 Mar 17 14:50 .bash_profile
    -rw-r--r--    1 brian  staff     59 Feb  2 13:47 .bashrc
    drwxr-xr-x    5 brian  staff    170 Dec  5 13:21 .bundler
    -rw-r--r--    1 brian  staff    379 Mar  3 17:36 .gitconfig
    drwxr-xr-x   30 brian  staff   1020 Feb  2 13:47 .rvm
    drwxr-xr-x    2 brian  staff     68 Dec  4 15:13 Applications
    drwx------+   6 brian  staff    204 Mar 23 18:20 Desktop
    drwx------+  11 brian  staff    374 Feb 27 10:57 Documents
    drwx------+ 141 brian  staff   4794 Apr  5 08:04 Downloads
    drwx------@  56 brian  staff   1904 Apr  4 21:58 Library
    drwx------+   3 brian  staff    102 Nov  4 10:49 Movies
    drwx------+   8 brian  staff    272 Mar  5 15:48 Music
    drwx------+  20 brian  staff    680 Mar 23 12:53 Pictures
    drwxr-xr-x+   5 brian  staff    170 Nov  4 10:49 Public
    -rwxr-xr-x    1 brian  staff    184 Nov  8 16:41 git_profile.sh
```

Hidden Files are typically used by applications to store configurations and there will be a many of them in your home directory. Most users don't want to be editing these files so they don't show up in `Finder`, but you as a software developer will be editing some these for yourself later on in the course.

Hidden files are hidden because their names begin with `.`

**Extra:** The columns from the output of `ls -la` represent (from left to right)

* file permissions
* number of links
* owner
* group
* file size
* last modified data
* file name


### Mini Review - Current Working Directory

* pwd
* Home Directory
* open .
* ls -la

---

##Navigating Around

###Root Directory
Another important directory is the root directory `/`

    ~ cd /

    / pwd

As we discovered the files on your computer are structured in a tree. The 'top' of the file system is know as the `root` directory (That may sound upside down, but in our case the root is at the top :) )

We can move to the **root directory** with the command `cd /`.
We can move back to your **home directory** with the command `cd ~`.

    / cd ~

    ~ pwd

    /Users/brian

You might have noticed that the prompt changed from `/` to `~`. The default prompt includes the current directory and sometimes the current user.

    ~ cd /Users/brian/

    ~

The `~` always refers to the current user's home directory, this is handy for scripts and for you, but you can use the full path just as well if you know it, `pwd` will give you the full path

## Relative Paths
Try this

    cd ../
    pwd

What happened? Which directory are you in?

  `../` prefixes paths relative to the parent directory

  `../` is a **relative path** and you can use it anywhere you would use a path

    ~ ls -al ../Guest

    total 8
    drwxr-xr-x+ 11 Guest  _guest  374 Nov  4 10:47 .
    drwxr-xr-x   6 root   admin   204 Nov  4 10:47 ..
    drwx------+  3 Guest  _guest  102 Nov  4 10:47 Desktop
    drwx------+  3 Guest  _guest  102 Nov  4 10:47 Documents
    drwx------+  4 Guest  _guest  136 Nov  4 10:47 Downloads
    drwx------+ 26 Guest  _guest  884 Nov  4 10:47 Library
    drwx------+  3 Guest  _guest  102 Nov  4 10:47 Movies
    drwx------+  3 Guest  _guest  102 Nov  4 10:47 Music
    drwx------+  3 Guest  _guest  102 Nov  4 10:47 Pictures
    drwxr-xr-x+  4 Guest  _guest  136 Nov  4 10:47 Public

###Tab Completion
Hitting `<TAB>` autocompletes.  Hit `<TAB>` constantly.

It's important to remember that being in one room is much like being in another room.  The difference is in the contents and the relative position of other folders.

###Mini Review - Navigating Around
* root directory `/`
* `../`
* Absolute and Relative Paths
* Tab Completion

---

##File Manipulation

###Making Directories

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

---

##Review

###History
What have we been up to?

    ~ <UP ARROW>

    ~ <UP ARROW>

    ~ <DOWN ARROW>

    ~ <DOWN ARROW>

    ~ history

##Topics
  * Current Directory
  * Home Directory
  * `ls`,`pwd`, commands
  * Root Directory
  * `cd`
  * Relative Paths
  * Tab Completion
  * `mkdir`
  * echo, Redirection and Piping
  * Moving, Copying and Removing

##Getting Help
For any command we discuss here, the command `man`, short for **manual**, will give a (hopefully) detailed explanation of that command.  Sometimes that explanation will be too detailed for you.  When you get lost in a man page and you want to understand it, start again from the beginning of of the **man page** and keep repeating.  Hopefully you will get further into the page each time you read it.

Many advanced commands also accept the --help option, but not all, but if you get stuck it can be worth a try. Most of the commands covered in this simple overview do not support this feature

    $ git --help

    usage: git [--version] [--help] [-C <path>] [-c name=value]
             [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
             [-p|--paginate|--no-pager] [--no-replace-objects] [--bare]
             [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
             <command> [<args>]

**Note:** In documentation we often see a `#` or `$` or `~` prefix before code examples, these characters are used to indicate that the example is a something which is executed in the terminal (as opposed to being a code sample) and usually these are not supposed to be entered when you execute a command.


##Bonus Topics
* Terminal Cheat Sheet
* `cat ~/.bash_profile`
* `export EDITOR='subl -w'`
* Different Types of shell


### Terminal Cheat Sheet
Bookmark this:

* [http://bit.ly/terminalcheats](http://bit.ly/terminalcheats)


### Different Types of Shell
You'll mostly be using `zsh` as your shell, but there are other similiar programs which you may see at work

* [http://unixhelp.ed.ac.uk/shell/oview2.html](http://unixhelp.ed.ac.uk/shell/oview2.html)


## Further Reading
Linux is almost the same as OSX, and this is a great manual about the Linux command line:

[The GNU Guide to the Command Line](http://en.flossmanuals.net/command-line/)

Here's a starter book on using the command line:

[The Command Line Crash Course](http://cli.learncodethehardway.org/book/)

Here's an interesting anecdote about why Standard Output and Standard Error are separate:

[The Birth of Standard Error](http://spinellis.gr/blog/20131211/)
