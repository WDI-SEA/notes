# Visual and Usability Upgrades

## Zsh install, OhMyZsh, and P10k theme + font
`zsh` is an alternative shell program to the default linux shell program `bash`.

A shell is a text based Command Line Interface (CLI) with which we can interact with our computer to run programs and commands.

There are a number of advantages to using Zsh, primarily in the customizability and aesthetics department!

### Zsh Install
Open the Ubuntu terminal app
In the terminal run the following commands: (follow the prompts and press y to confirm yes when it prompts you to)

```
sudo apt install zsh
chsh -s $(which zsh)
```

Exit the ubuntu terminal and reopen it. It will prompt you with the Z Shell configuration menu - press 2 to populate zsh with the recommended defaults

### Oh my Zsh install
Oh My Zsh is a Zsh configuration framework that gives you way more customization options and a ton of visual themes to choose from .

* [OhMyZsh webpage](https://ohmyz.sh/#install)
* Run the following command in the Ubuntu terminal
```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### Font Install
We need to install a custom font to enable the use of various icons that our terminal will use.
Powerlevel10k recommends the MesloLGS NF font.

* [Powerlevel10k font install instructions](https://github.com/romkatv/powerlevel10k#manual-font-installation)
* Download and install the following font files
    - [MesloLGS NF Regular.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf)
    - [MesloLGS NF Bold.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold.ttf)
    - [MesloLGS NF Italic.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Italic.ttf)
    - [MesloLGS NF Bold Italic.ttf](
    https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Bold%20Italic.ttf)
* Right click the Ubuntu terminal header bar, click on 'Properties', click on the 'Font' tab, and change the font fo 'MesloLGS NF', or whichever other font you've installed!


### Powerlevel10k install
Powerlevel10k is a fantastic theme for OhMyZsh that includes all the bells and whistles and has a very powerful configuration tool that makes it super easy to use

* [Powerlevel10k webpage](https://github.com/romkatv/powerlevel10k#oh-my-zsh)

1. Run the following command in your terminal
```
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
```
2. Edit the `.zshrc` config file with our newly downloaded theme
```
code ~/.zshrc
```
3. Find the ZSH_THEME line and set it to be
```
ZSH_THEME="powerlevel10k/powerlevel10k"
```

### Windows Terminal (Optional)
Windows terminal is an application that gives you more flexibility and customization options with your terminal window than the regular terminal.

Nice features include tabs and color themes

1. Install from the Windows Store
2. Go to Settings -> Profiles -> Ubuntu -> Click on 'Open JSON file' in the bottom left
3. Open the JSON file with VS Code or notepad
4. Under "profiles" -> "list" find the one with `"name": "Ubuntu"`, and add:
```
"commandline": "wsl.exe ~",
"fontFace": "MesloLGS NF",
```

With this done you can now start using the Windows Terminal instead of the Ubuntu terminal!

<hr />

## Navigation
1. Read this intro
    * [✔️] [Alternative OS intro](./README.md)  
2. Prior to the first day of class: Enable WSL and Install Ubuntu from the Microsoft Store app
    * [✔️] [WSL Setup](./wsl-setup.md)
3. On the first day of class, your instructors will help you with **Installfest**
    * [✔️] [Installfest](./wsl-installfest.md)
4. Optional visual and usability upgrades for your terminal
    * [✔️] [Upgrades](./upgrades.md)
5. Unit 2-4 Installfest
    * [ ] [Unit 2, 3, 4 Installfest](./wsl-unit234.md)