# Unit 4  OSX installfest

We are going to need to:
1. install `python3` and `pip3` with homebrew
1. alias the `python` an `pip` commands in our `.zshrc` (zshell config file) to point to python3 instead of python2.

#### Installing `python3` and `pip3`

We will be using homebrew to install and manage python3.

___

Tell homebrew to install python with the following command: 

```bash
brew install python
```

Afterwards, run the following command:

```bash
python3 --version
```

If this command returns a version lower than `Python 3.9.2`, tell homebrew to update python with this command:

```bash
brew upgrade python
```

Python uses `pip` as the package manager, similar to how node.js uses `npm`

Double check that `pip3` has been installed on your system with the following command:

```bash
pip3 --version
```

If zshell tells you `pip3` is a command not found, reach out to a dev to troubleshoot this bug. I am putting [this stack overflow](https://stackoverflow.com/questions/47255517/brew-install-python3-didnt-install-pip3) here in case it is helpful to debug this issue for anyone.

### Additional Setup

Everyone needs to install the following things, regardless of thier operating system.

1. install a couple global python packages with `pip3`
1. install a vscode extension for python

#### Installing Global Packages 

We are going to make sure we have `virtualenv` installed, which is how `pip` manages package versioning in python projects.

We also are going to install `ipython`, which is a tricked out version of the python shell.

___


check to make sure you have virtualenv installed with the following command:

```bash
virtualenv --version
```

if nothing is found, use `pip install virtualenv` ot install virtualenv

run the following command to install ipython, which is a tricked out python shell:

```bash
pip3 install ipython
```

#### Vscode python Extension

everyone should install [this python vscode extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) 