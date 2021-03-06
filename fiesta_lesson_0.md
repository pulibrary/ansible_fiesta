# Lesson 0

## Prerequisites

Clone this repo. Run all of the command -unless specified- from the root of this
repo. Make sure you are running the tests at the end of the class whilst
connected to the princeton network.

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
* Docker

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
* Install Python and virtual environment management software with:
```
brew install python pipenv
```
* Install [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)

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

* Setup Python and Pipenv software with: (Ubuntu bionic doesn't have Python
  3.7.2)

```bash
sudo apt -y install python-pip make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
exec "$SHELL"
```

This will install [pyenv](https://github.com/pyenv/pyenv) and the instructions
above assume bash shell.

```bash
pyenv install 3.7.2
pip install -U pip
pip install --user pipenv
```

* Install Docker
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt install docker-ce
```

### Test your installation on both macOS and Ubuntu with:


You will need to run the following steps inside your cloned repository.

* Install Ansible and Molecule with:
```bash
pipenv sync
pipenv install
pipenv shell
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
key"` This accepts the default file location. Ping kayiwa@ to have your keys
appended to the pulsys user's `authorized_keys`

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
ansible testservers -u pulsys -m ping -vvvv
```

We will see that the "ping" module has succeeded. The `"changed" : false` output
tells us that the executing module did not change the state of the server. The
`"ping": "pong"` text is output that is specific to the ping module. The `-m`
flag part of the command represents module and the `-vvvv` part is the verbosity
levels in the output.

Run the following now:

```bash
ansible testservers -u pulsys -m command -a uptime
```

and

```bash
ansible testservers -u pulsys -m command -b -a "tail /var/log/syslog"
```

Here we are using Ansible's
[`command`](https://docs.ansible.com/ansible/latest/modules/command_module.html) module (used by default) and because
`/var/log/syslog` requires sudo privileges we elevate our privileges using the
`-b` flag. (for become).

Finally let's run:

```bash
ansible testservers -u pulsys -m apt -b -a "name=htop update_cache=yes state=present"
```

Here we are using Ansible's [`apt`](https://docs.ansible.com/ansible/latest/modules/apt_module.html?highlight=apt) module to run `apt -y update && apt -y install
htop`. It is important to state that you will rarely need to use this but most
ad-hoc commands are useful in quickly getting reports back from hosts under your
management.
