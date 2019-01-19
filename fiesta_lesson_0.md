# Lesson 0

## Prerequisites

Participants in this exercises will be expected to install the following to work
effectively in this for this tutorial. As a result this repository will be
highly opinionated. The participant is encouraged to work with the tools they
are most comfortable with but we will make the following assumptions. The
participant has the following installed on their networked computer.

* A Terminal Emulator
* A Package manager
* A Text Editor
* Git
* Vagrant
* Virtualbox
* Python (with virtual environments and pip configured)
* Ansible
* Molecule

## Setup Environment for macOS

* macOS ships with a terminal. (Consider using:
  [iTerm2](https://www.iterm2.com/index.html))
* Follow the instructions on the [Homebrew Page](https://brew.sh/) to install
  the package manager.
* Select a programmers Text Editor (For example VIm, Atom)
```bash
brew install vim
```
* Install Git using the Homebrew package manager with:
```bash
brew install git
```
* Install Vagrant using the Homebrew package manager with:
```bash
brew cask install vagrant
```
* Install Virtualbox with the Homebrew package manager with:
```bash
brew cask install virtualbox
```
* Install Python and virtual environment software with:
```
brew install python pyenv pyenvvirtualenv
```

## Setup Environment for Ubuntu Bionic

* We will us the `apt` package manager
```bash
sudo add-apt-repository multiverse && sudo apt -y update
```
* Select a programmers Text Editor (For example VIm, nano)
```bash
sudo apt -y install vim
```
* Install Git using `apt` with:
```bash
sudo apt -y install git
```
* Install Virtualbox using `apt` with:
```bash
sudo apt -y install virtualbox
```
* Install Vagrant using `apt` with:
```bash
sudo apt -y install vagrant
```
* Setup Python and virtual environment software with:
```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
 `echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile`
```

### Test your installation on both macOS and Ubuntu with:

* Configure your environment for this project with:
```bash
pyenv install 3.7.2
pyenv virtualenv 3.7.2 ansible_fiesta-3.7.2
```
* Install Ansible and Molecule in your newly created python environment with:
```bash
pyenv activate ansible_fiesta-3.7.2
pip install -U pip
pip install ansible molecule
ansible localhost -m ping
```

You will get a result close to this whose warnings we will disregard for now.

```bash
[WARNING]: Unable to parse /etc/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

localhost | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## Upload ssh-keys to Github

* Create a [Github Account](https://github.com)
* Generate your ssh keys with the following commands on your Terminal
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@princeton.edu"
```

This will generate a new ssh-key using your princeton email as the label. If you
created your Github account with a different email account please adjust the
command above accordingly. You will be prompted to `"Enter a file to save the
key"` This accepts the default file location.

```bash
Enter a file in which to save the key (/path/to/userhome/directory/.ssh/id_rsa): [Press enter]
```

Follow the [Github
Instructions](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
to add your keys to your account. These keys will be appended to the `pulsys`
user needed for future activities in these classes.
