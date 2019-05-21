# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Scripting

### Learning Objectives
*After this lesson, you will be able to:*
- Explain the uses of scripting.
- Write scripts that perform file I/O.
- Write scripts that take user input.

## What's a Scripting Language?

There are only two types of programming languages in the world: **scripting languages** or **compiled languages**.

A *scripting language* or interpreted language like Python executes statements in order. A *script* is typically a file with some Python code in it.

Imagine; you wrote an application with Java. Before  you can run it, you need to compile it - turn it  After compiling completed, you run your application. When running your application, you notice a bug. To fix it, you have to stop your application, go back to source code, fix the bug, wait for the code to recompile, and restart your application to confirm that it is fixed. And if you find another bug, you'll need to repeat that process again.

In a scripting language, you can fix the bug and just need to reload your application, no need to restart or recompile anymore. It's as simple as that.

All languages, like Python, are one of these two categories.

#### Scripting languages:

- One is Python!
- Write code, then immediate run it: `python my_file.py`
- Executes statements in order.
- Find a bug? Fix it, run it, repeat.


#### Compiled languages:

- Compile means "build".
- *We can't immediate run code - the computer can't just read the code and needs to translate it to something it understands first.*
- Write code, *then compile it (not quick!),* then run it.
- Find a bug? Fix it, *wait for the code to compile,* run it, repeat.

You don't need to memorize this - just know that there's a difference, and Python is scripting.

## What is a Script?

A script is just some code that does something. It's usually written in a scripting language and can be as simple or as complex as needed!

#### Try it out!
Let's write a script:

- Create a file called `my_script.py`
- Open the file in your code editor.
- Type the line

```python
print("hello world!")
```

**CONGRATS**: You now have a script!

Look familiar? You've been scripting since day 1!

### Scripting, Commonly

When people say scripts, though, they usually mean code that:

* Takes input.
* Gives output.
* Reads or writes to a file.
* Performs a task.

We have done all of this already, but let's look at at in the context of scripting

## File I/O

On your computer, you can:

- Create or open a file (text, jpg, Word doc...).
- Read it.
- Edit it.
- Close it.

These are pretty basic actions. Can we do it in Python?
Enter File I/O *(input/output)*

With files, there are three key points.

1. Tell Python to open the file: `my_file = open(<file name>)`
2. Do something with the file! (Read it, edit it, etc).
3. Close the file when you're done: `my_file.close()`

### Reading Files
First, let's check out **read**: 
View, but not change, the contents, with `read()`.

#### Try it out

Next to your `my_script.py`, create a file called "hello.txt" with the word "hi" in it.

1. Now, in `my_script.py`, Fill it with:
    ```python
    my_file = open("hello.txt")
    print(my_file.read())
    my_file.close()
    ```
2. Run it!

> Note: The file must exist already!

### Editing Files

In programming, "edit" is referred to as "write", short for "write to." How do we write a file?

`open(<file name>)` has optional parameters: `open(<file name>, <mode>)`
 
**Mode:** "What do you want to do with the file?" The default is "read." Use `w` for "write":


```python
# To read a file:
my_file = open("hello.txt")
print(my_file.read()) ## We want this to be write, not read!
my_file.close()

# To write a file:
my_file = open("hello.txt", "w")
## Write some stuff
my_file.close()
```

**Important:** Write *overwrites* the current file! Write is "replace what's there", not "add to the file"

#### Try it Out

Let's try this. Change your script. We're going to make it a little more complex - since we're programming, we can use variables!

```python
# Open the file hello.txt
my_file = open("hello.txt", "w")

# Write some content to my_file.txt
my_file.write("Hello world")
my_text = "Apple juice is delicious." # Use the variable!
my_file.write(my_text) # Writes "Apple juice is delicious."
my_file.write("Have a nice day!")

# Always close the file
my_file.close()
```

Run it!

Open the file to see what happened. How would you add new lines?

#### Complex Strings

What happens if we try to `write` multiple strings?

```python
my_file = open("a_file.txt", "w")
my_text = "Apple juice is delicious."
my_file.write(my_text, "Don't you think?") # Error! Write takes 1 argument (2 given).

my_file.close()
```

Error! `write` only takes one argument. We need to concat the strings. *Always just pass one argument to file.write()*.

```python
my_file = open("a_file.txt", "w")
my_text = "Apple juice is delicious."
string_to_write = my_text + "Don't you think?" # Make one string here!
my_file.write(string_to_write)
my_file.close()
```
### Creating Files

What if the file doesn't exist yet?

**Write** to the rescue!

* Write opens a file for writing...
* But it also creates it if need be!

#### Test it out

At the bottom of your script, add:

```python
# Open OR create file totally_new_file.txt
my_new_file = open("totally_new_file.txt", "w")

# Write some content to totally_new_file.txt
my_new_file.write("Content goes here")

# Always close the file
my_new_file.close()
```

Check your folder after running it!

Now, try it yourself. Write a new script:

- Make a new file called `a_file.txt`.
- `open()`, in read mode, your existing `a_file.txt`.
- `.read()` the file and save the contents into a variable, `file_contents`.
- Using `.write()`, create a new file called `b_file.txt`.
- Write `file_contents` to `b_file.txt`.

<details><summary>Answers</summary>
<p>

```python
my_file = open("a_file.txt", "r")
file_contents = my_file.read()
my_file.close()

my_file_script = open("b_file.txt", "w")
my_file_script.write(file_contents)
my_file_script.close()
```

OR you can open multiple files at the top—you don't have to go sequentially 

```python
file_to_read = open("a_file.txt")
file_to_write = open("b_file.txt", "w")


file_contents = file_to_read.read()
file_to_write.write(file_contents)

file_to_read.close()
file_to_write.close()
```

</p>
</details>


### Notes on `file.close()`

According to this [stackoverflow question](https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python) not closing files is a bad idea, for the following reasons:

- It puts your program in the garbage collector's hands - though the file in theory will be auto closed, it may not be closed. If you don't close them yourself, Python will eventually close them for you. In some versions of Python, that might be the instant they are no longer being used; in others, it might not happen for a long time. Under some circumstances, it might not happen at all.

- It can slow down your program. Too many things open, and thus more used space in the RAM, will impact performance.

- When writing to a file, the data may not be written to disk until the file is closed. When you say `output.write(...)`, the data is often cached in memory and doesn't hit the hard drive until the file is closed. The longer you keep the file open, the greater the chance that you will lose data.

- You could, theoretically, run in to limits of how many files you can have open.

- Also, some operating systems (Windows, in particular) treat open files as locked and private. While you have a file open, no other program can also open it, even just to read the data. This spoils backup programs, anti-virus scanners, etc.

- It is good programming practice.

Always remembering to close a file can be hard.  There's another way to open files so Python closes it for us!

```python
# Instead of:
file_object = open("my_file.txt", "w")
file_object.write("Hello World!")
file_object.close()

# This line replaces the open and close above
with open("my_file.txt", "w") as file_object:
  file_object.write("Hello World!") # Note the indent!
````

## Other File Modes

What if we want to read AND write a file? Or write to the end of a file instead of overwriting what's there?

`open` has a few other modes.

| Value | Mode | Purpose |
| ----- | ------------ | -------------- |
| `r` | Reading | Read only. The default! |
| `w` | Write | Use to change (and create) file contents |
| `a` | Append | Use to write to the end of a file |
| `r+` | Read Plus | Can do both read and write |


> You don't need to memorize this; just know it's there. A lot of programming is understanding your options and then Googling the syntax! The biggest thing for you to learn is the concepts that Python can do.

### What Else is in File?

These are just for reference - we won't be using them!

- Do you have a list that you want to write on multiple lines? Use `my_file.writelines([<your list>])`

- Does your file have things on multiple lines you want to read into a list variable? Use `list_contents = my_file.readlines()`

- Separating some written lines? Add `\n` to the `write()`


## User Input?

We've just done a lot with file I/O (in/out).

We can prompt users for information, too.

```python
# Prompts with "input"
# Saves result in user_name
user_name = input("Please type your name: ")
```

#### Try it Out

1. Create a file called `about_script.py`.
2. In it, prompt the user for their name. Then, prompt them for their favorite food.
3. Using write, create a file called `about_me.txt`.
3. In `about_me.txt`, write out the name and favorite food in a sentence.

<details>
<summary>Answer</summary>
<p>

```python
user_name = input("Please type your name: ")
user_food = input("Please type your favorite food: ")

file = open("about_me.txt", "w")
file.write("My name is " + user_name +  " and my favorite food is " +  user_food)
```
</p>

</details>

## Summary and Q&A

Scripting language vs compiled language.

- Scripting languages: Write -> Run.
- Compiled languages: Write -> Build -> Run.

Script:

- Just some code!

File I/O:

- `my_file = open("a_file.txt", "w")`
- `my_file.write("Some content")`
- `my_file.write(my_text)`
- `my_file.close()`

User input

- `user_name = input("Please type your name:")`

## Additional Resources

* [Socratica Video: Text Files](https://www.youtube.com/watch?v=H_R5yRtFtuc)
* [Executing a Python Script](https://www.python-course.eu/python3_execute_script.php)
* [Reading and Writing Files](http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python)
* [File Object Documentation](https://www.tutorialspoint.com/python3/python_files_io.htm)
* [Binary vs Text Files](https://www.nayuki.io/page/what-are-binary-and-text-files)
