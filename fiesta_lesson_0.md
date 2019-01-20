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
brew install python pipenv
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
* Setup Python and Pipenv software with:
```bash
sudo apt -y install python-pip
pip install --user pipenv
```

### Test your installation on both macOS and Ubuntu with:

* Install Ansible and Molecule with:
```bash
pipenv install ansible molecule
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

## Ansible ad-hoc

With your keys added try the following ad-hoc commands

```bash
ansible testservers -m ping -vvvv
```

We will see that the "ping" module has succeeded. The `"changed" : false` output
tells us that the executing module did not change the state of the server. The
`"ping": "pong"` text is output that is specific to the ping module. The `-m`
flag part of the command represents module and the `-vvvv` part is the verbosity
levels in the output.

Run the following now:

```bash
ansible testservers -m command -a uptime
```

and

```bash
ansible testservers -m command -a -b "tail /var/log/syslog"
```

Here we are using Ansible's `command` module (used by default) and because
`/var/log/syslog` requires sudo privileges we elevate our privileges using the
`-b` flag. (for become).

Finally let's run:

```bash
ansible testservers -m apt -b -a "name=nginx update_cache=yes state=present"
```

Here we are using Ansible's `apt` module to run `apt -y update && apt -y install
nginx`. It is important to state that you will rarely need to use this but most
ad-hoc commands are useful in quickly getting reports back from hosts under your
management.
