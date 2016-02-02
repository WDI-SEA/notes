#Sublime Setup

## Setting up Package Control in Sublime Text

* Open Sublime Text
* Bring up the console
  * Use CTRL + ` on OSX
  * or `View > Show Console`
* Go to https://packagecontrol.io/installation and paste the appropriate code into your Terminal
  * You should be using Sublime Text 3, so copy the Sublime Text 3 code.
* Restart Sublime

## Install Sublime Packages

* Type `COMMAND + SHIFT + P` to open the Command Palette
  * `CTRL + SHIFT + P` on Linux
* Type `Install Package` and select the first result (by pressing `ENTER`)
* Type the package you want to install, and press `ENTER` to begin installation.

### Useful Packages that you should install

* ColorPicker (pick colors by typing `COMMAND + SHIFT + c`, handy for CSS)
* Color Highlighter (visually displays colors for hex/rgb values)
* Terminal (launch a terminal window from a folder on the sidebar)
* BracketHighlighter (highlight brackets and tabs)
* Bootstrap 3 Snippets (tab snippets for Bootstrap 3 elements)
* CodeFormatter (format your HTML/CSS/JS like a boss)
* 1Self (tracks your coding activity)
* EJS (syntax definition, we'll use this when working with Node)
* Sass (syntax definition, we'll use this when working with Rails)

Feel free to install any others, and we'll install others throughout the course.

### Creating a Snippet

We'll use a lot of snippets when working with Bootstrap, and you can make your own as well.

* Go to `Tools > New Snippet`
* Include the content of your snippet inside `<![CDATA[ ]]>` within the `<content>` element.
* To define how to trigger the snippet, uncomment the `<tabTrigger>` line and type the keyword for your tab trigger.
* To trigger the snippet only on certain files (for example, only HTML, or only JavaScript), uncomment the `<scope>` tag and change the scope to the language you need.
* More details and advanced functionality can be found in [this handy blog post](http://www.hongkiat.com/blog/sublime-code-snippets/)