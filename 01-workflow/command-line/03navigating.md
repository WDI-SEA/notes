#Navigating the Filesystem

The file structure you see in the Terminal is the same as the one you see in the `Finder` application. Finder tends to hide some of the folders from you to keep things simple for most users, but everywhere that you go in Finder is accessible through 'Terminal'.


##Where am I?
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
