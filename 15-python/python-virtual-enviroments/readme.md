# Python Virtual Environments and Flask Set Up

Step by step breakdown of setting up a virtual environment for python projects and spinning up a flask app.

### What is a Virtual Environment and Why Do we Need it?

If you install packages using `pip` ofr `pip3` in your project, they will by default be installed globally. You can think of a virtual environment as `npm` and a `package.json` for your python project. Using a virtual environment will lock all of the versions of the packages you use for development. This is especially important in python development package maintainers will frequently introduce breaking changes, much more so than node package maintainers, and would believe that it is up to the dev (you) to version lock the packages you are using.

## Steps to Set up a Virtual Environment with Git

Before installing or using any packages you must always activate a `virtualenv`, and you must `deactivate` it when you are finished. `pip3` relies on the globally install packages unless you have a virtual environment running.

all python projects that use pip packages should be set up to use a virtual environment to ensure version control and package compatibility

#### Basic Virtual Environment Setup

* Create a project directory and cd into it
* run `virtualenv venv` to make a virtual environment
* start the virtual environment before installing needed packages:
  * on mac/linux/WSL use `. venv/bin/activate`
  * (on **non-WSL** windows use `. venv/Scripts/activate`)
* make sure your virtual environment is active: `(venv)` can be seen in your terminal
* install the needed pip packages for the project
* once all your packages are installed, freeze the pip list in a requirements.text file
  * use the command `pip freeze > requirements.txt`
  * this needs to be done again if you add more pip packages to update the requirements.txt
  * if you clone a python project from github, you can use `pip install -r requirements.txt` to install the needed packages
* you can use the command `deactivate` to leave the virtual environment
* every time you want to work on a python project with a virtual environment, you will need to activate it first
* if you clone a repo from github with a virtual environment first install the needed packages with `pip install -r requirements.txt` and then run `. venv/bin/activate` (`. venv/Scripts/activate` on windows) to start the virtual environment

#### Virtual Environments with git

the `venv` folder is like `node_modules` with node.js. It needs to be git ignored. By default when you create a new `venv` folder it includes a `.gitignore` inside of it. If for some reason the venv is not git ignored in your setup (older version of virtualenv), you can do these steps to ensure it is git ignored:

* after you `git init` in your project, `touch .gitignore` and add `venv` and `__pycache__` to it, so they don't get sent up to github.
