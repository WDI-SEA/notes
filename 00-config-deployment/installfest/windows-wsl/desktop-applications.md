# Desktop Applications 

## Table of Contents 
- Slack
- VS Code
    - Accessibility Extensions
    - Using Prettier and other auto-formatters.
    - Other helpful keyboard shortcuts.
- Chrome Browser
    - Chrome Developer Extensions
- Keyboard Shortcuts for Rearranging Windows
- Postman

## Slack

Download the [Slack Desktop Client](https://slack.com/downloads/windows). We recommend using the Desktop client over the website version of Slack because it is easier to get notifications, upload files, and do other actions. Slack is the primary communication tool for class. 

## VSCode Text Editor
Earlier, we installed VSCode. Open up Windows Terminal and type `code .` to create a shortcut in your terminal to open up VSCode. It's much faster than looking for a folder and then opening it in VSCode.

If the above doesn't work, open VScode and press `ctrl + shift + p` to open up a bar. type path and type 'shell command' to find `Shell Command: Install 'code' in PATH` click on that button to allow you to open up vscode in your terminal using `code .` to open up VScode with the current folder loaded in.

Once you have finished installing and VSCode has opened, close your command prompt and open a new one. At the new prompt, run `code .` to ensure that your shell is correctly linked with the app.

Here are some helpful extensions you might want to install:
- [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)
- [Community Material Theme](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-community-material-theme)
- [Dark Themes Pack](https://marketplace.visualstudio.com/items?itemName=thegeoffstevens.best-dark-themes-pack)
- [Django Support](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [EJS Syntax Support](https://marketplace.visualstudio.com/items?itemName=DigitalBrainstem.javascript-ejs-support)
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
- [Material Icons Pack](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
- [Prettier Code Formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Setting Up Auto-formatters

### Prettier

Prettier is an *opinionated* formatter for HTML, CSS, and JavaScript. It works similarly to the spell check feature in word processors like Microsoft Word or Google Docs, and it will be immensely helpful with formatting your code. 

To use Prettier, follow these steps:
- open HTML, CSS, or JavaScript file to format
- press `CTRL SHIFT P` to open up the "Command Palette" menu
- select "Format Document With..."
- another menu will pop up, and select Prettier as the default formatter.
- ...and just like magic, all lines will be automatically aligned and formatted properly!

### Black Python Formatter

You must have the Python VSCode extension installed!

Then, you can follow these steps:
- open a .py file
- press `CTRL SHIFT P` to open up the formatting menu and select "Format Document With..."
- an error message will pop-up and ask you to select an auto-formatter. Select the formatter named Black.
- open up the formatting menu with `CTRL SHIFT P`
  - type in Preferences: Open Settings (JSON)
  - if the first line of this snippet already exists in your settings.json, overwite it with this code block. otherwise, you can simply add it:
  ```
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "[python]": {
    "editor.defaultFormatter": null
  },
  "python.formatting.blackArgs": ["--line-length", "86"],
  "python.formatting.provider": "black",
  ```

## Other Helpful VSCode Shortcuts/Settings
- Toggle Word Wrap: `ALT Z`. Word Wrap should stay on by default.
- Zoom In/Zoom out: `CTRL +/-`. Always ask if code is too big/small to read. :)
- Open file: `CTRL P` and then type the path to file. E.g `controllers/data/resourceController.js`. 
  - Some projects may have dozens of folders, and it's much faster to access files this way then clicking through several menus.
- `CTRL K T` Change VSCode theme. Select your favorites from the theme packs above! My personal favorite is `PaleNight High Contrast` from the Community Material Themes Pack!
- To change the Icon Theme: Go to the top toolbar and click through File --> Preferences --> File Icon Theme
  - Material Icon Theme adds helpful labels and color coding to the folders of your projects.

## Chrome Browser
We like using Chrome as our preferred browser because we like its developer console best. If you don't already have it, please follow [the installation instructions for Chrome](https://support.google.com/chrome/answer/95346?hl=en).

We also recommend you install the JSON View Extension to make it easier to see data from APIs

* [JSON View](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc)

## Postman - API Testing

Download the Postman Desktop App from https://www.postman.com/downloads/. We will not be using the chrome extension.

## A word on *Keyboard Shortcuts*

By the way, developers LOVE shortcut key combinations. The more shortcuts you know, the faster you can code!

We've covered some heplful VSCode shortcuts above, but there are tons more [VSCode Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf). 

You also have a handy shortcut for resizing and moving windows built into Windows 10!

`Windows Key, Left Arrow / Right Arrow` to resize your window to half of the screen and move it to the left/right side. 

`Windows Key, Up Arrow, Up Arrow` to instantly make your current window or app full screen.

Every single application above has its own list of shortcuts too!

## Touch Typing
You will be at a serious disadvantage if you do not know how to touch type. To practice this skill we recommend [typingclub](http://typingclub.com), [speedcoder](http://www.speedcoder.net/) or [typeracer](http://play.typeracer.com/).

* [x] [Command Line](command-line-setup.md)
* [x] [Configuring Git](git-configuration.md)
* [ ] [Databases and Frameworks](dbs-languages-frameworks.md)
* [x] [Desktop Applications](desktop-applications.md)

## Instructors/Staff Notes
- Consider student's invidual needs for accesibility. 
- Bracket Colorizer and Prettier helps avoid wasting mental energy and time spent on fixing minor errors. 
- Make a class norm of auto-formatting code before presenting or debugging. Students can also use the `format document` menu using `CTRL+SHIFT+P` to quickly format longer blocks of code during lessons.
- Avoid themes that use cursive or substitute symbols for operators (for example `===` with a three lines vertically stacked) to avoid confusion about syntax meaning.

**Congratulations! You've made it through installfest! Now is a great time to take a cute photo of your work station! :)**
