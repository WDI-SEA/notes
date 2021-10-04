# VS Code Tips & Tricks

## How to open it

Use the command line to open it within the project on which you are working:

```bash
code .
```

## Managing the windows

Toggle the sidebar \(with the file list\) open or closed:

```text
command + b
```

Toggle the built-in terminal open or closed:

```text
control + `
```

Split the editor window:

```text
command + \
```

## File management

Create a new file \(mind what location you are creating it in\):

```text
command + n
```

Open file \(shows the open file dialog box\):

```text
command + o
```

Save file \(do this a lot\):

```text
command + s
```

Close current tab \(or the whole editor if no files are open\):

```text
command + w
```

## Basic Text Editing

We all know about Cut, Copy, and Paste. We may have been using them from our Edit menus with a mouse but no longer! We are developers now and we live in the command prompt:

Copy:

```text
command + c
```

Cut:

```text
command + x
```

Paste:

```text
command + v
```

Normally, we need to highlight text to perform one of those actions but VS Code has some more advanced tweaks. Simply place your cursor on a line and try the following:

Copy an entire line:

```text
command + c
```

Cut an entire line:

```text
command + x
```

Command + v will still paste whatever is on the clipboard.

Move an entire line up or down:

```text
option + up/down arrow
```

Copy an entire line up or down:

```text
shift + option + up/down arrow
```

Indenting/unindenting blocks: \(with a block highlighted\)

```text
tab/shift + tab
```

Commenting lines or blocks: \(with the cursor on a line or a block selected\)

```text
command + /
```

## Multi-cursor editing

Want to edit multiple lines at once? Add cursors to adjacent lines upward or downward:

```text
command + option + up/down arrow
```

Want to select multiple occurances of the same word? Select it once and then use:

```text
command + d
```

## Extensions

* Bracket Pair Colorizer - CoenraadS: Colors matching opening and closing brackets with the same color for easy location.
* indent-rainbow - oderwat: Makes each indentation level a different color for easy reference.
* Material Icon Theme - Phillipp Kief: Gives attractive icons to VS Code.
* open in browser - TechER: Adds an "open in browser" context menu item. Handy for launching HTML files.
* Rainbow Brackets - 2gua: More bracket colorizing.

## Full VS Code Command Reference

This PDF shows all the Mac OS commands for VS Code:

[https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

