# Navigating the Filesystem

The file structure you see in the Terminal is the same as the one you see in the `Finder` application. Finder tends to hide some of the folders from you to keep things simple for most users, but everywhere that you go in Finder is accessible through the Terminal.

## Common Navigation Commands

* `pwd` - print working directory
* `open` - open a file/directory
* `ls` - list directory contents
* `cd` - change directory

## `pwd` - Where am I?

Wherever we are, `pwd` (short for **print working directory**) will show us what directory we are in.

```
pwd

/Users/brian
```

Typically the terminal will start in your `HOME` directory, each user has their own `HOME` directory, but on your computer it is common for you to be the only real user. At any given time a terminal shell process has one **current working directory**

## `open` - Open a file/directory

```
open .
```

Wherever we are, `open .` opens a Finder window in the current directory. This can be handy for going between the terminal and Finder interfaces.

Additionally, we can open a file using the default application for the file.

```
open index.html
```

## `ls` - Listing directory contents

We can also list the files and directories in the current working directory. Your list may vary from the files/directories below.

```
ls

  Applications   Pictures  gitshell.sh rorshell.sh
  Desktop   Library   Public    hashes  rorshellws.sh
  Documents Movies    bin   helloroom work
  Downloads Music   git_profile.sh  phpshell.sh
```

### Listing in the long format

To display this list in a cleaner format, we can pass **options** to the command. For example, the `l` option displays the list in a long format.

```
ls -l

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
```

Now we can clearly see what files are in the current working directory. Some of these items are files, some are directories.

The `ls` command can take a directory as an argument

```
ls -l Documents/

total 3
drwxr-xr-x   4 brian  staff      136 Feb 22 20:01 Rails
-rw-r--r--@  1 brian  staff  8154896 Feb 27 10:57 Profile.png
-rw-r--r--@  1 brian  staff  6258658 Feb 27 10:57 Profile2.png
```

### Listing hidden files

There's also a flag to list **hidden files**, which are files preceded with a period. These files are normally not visible in the command line unless we explicitly want them.

Using the `a` flag with `ls` will list hidden files. Note we can use flags in combination.

```
ls -la

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

Hidden Files are typically used by applications to store configurations and there will be many of them in your home directory. Most users don't want to be editing these files so they don't show up in `Finder`, but you as a software developer will be editing some these for yourself.

**Extra:** The columns from the output of `ls -la` represent (from left to right)

* type (`d` denotes a directory)
* file permissions
* number of links (contained files and folders)
* owner
* group
* file size
* last modified data
* file name

---

## `cd` - Changing directories

We can change directories by using the `cd` command, followed by the directory we want to change to. Let's try changing to the **root directory**.

```
cd /
```

We can verify that we are in the root directory by using `pwd`. Zsh also shows us the working directory.

### Root Directory

The files and directories on your computer are structured in a tree. The 'top' of the file system is know as the `root` directory (That may sound upside down, but in our case the root is at the top :)

![Filesystem image](http://www.qnx.com/developers/docs/qnx_4.25_docs/qnx4/user_guide/images/files.gif)

### Home Directory

When logged in as a user, there will also be a home directory that represents your user's files. By default, the terminal will usually open in the home directory. As a shortcut, the tilde (`~`) can be used to change to the home directory. Just run `cd ~`.

```
cd ~
```

---

## Absolute and Relative Paths

### Absolute Path

An **absolute path** is the *full path written out from the root*. For example, the full path of a file may look like this:

```
/Users/brian/Documents/profile.png
```

Navigating to this file would involve quite a lot of typing. Luckily, we can also use relative paths.

### Relative Path

A **relative path** is a *partial path relative to the current directory*. For example, if Brian was already in `/Users/brian`, a relative path for the file above would look like this:

```
Documents/profile.png
```

Note that `/Users/brian` was left off, because `Documents/profile.png` is relative to `/Users/brian`.

We can also use relative paths to go back one or more directories.

```
cd ..
cd ../..
cd .
```

Note that `..` represents a link to the previous directory. The first command goes back one directory, and the second command goes back two directories. These are relative paths!

The third command doesn't take us anywhere. We can also use `.` to represent the current directory. Try it out to get used to these links.
