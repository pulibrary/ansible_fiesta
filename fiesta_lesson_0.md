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
* Ansible
* asdf or rtx
* Docker
* Git
* Molecule
* Python (with virtual environments and pip configured)

## Setup Environment for macOS

* macOS ships with a terminal. (Consider using:
  [iTerm2](https://www.iterm2.com/index.html))
* Follow the instructions on the [Homebrew Page](https://brew.sh/) to install
  the package manager.
* Select a programmers Text Editor (For example VIm, VSCode)

```bash
brew install neovim
```

Download [VSCode](https://code.visualstudio.com/) and add the following

  * [YAML Language Support](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
  * [Ansible Language Support](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)

* Install Git using the Homebrew package manager with:

```bash
brew install git
```
* Install Python and virtual environment management software with:

Install and configure [ASDF](https://asdf-vm.com/)

```
asdf install
pip install --upgrade pipenv
```
* Install [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)

## Setup Environment for Ubuntu Jammy Jellyfish

* Select a programmers Text Editor (For example VIm, nano)
```bash
sudo apt -y install neovim
```
Download [VSCode](https://code.visualstudio.com/) and add the following

  * [YAML Language Support](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
  * [Ansible Language Support](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)

* We will use the `asdf` [ASDF](https://asdf-vm.com)

```bash
asdf install
pip install --upgrade pipenv
```

* Install Git using `apt` with:
```bash
sudo apt -y install git
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
```zsh
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

## Inventory

To manage a remote host Ansible will look for an inventory file of the hosts that will be managed. (by default `/etc/ansible/hosts`) In our case we will create a file called `inventory/sandbox-<yournetid>` (this file will be ignored based on [./.gitignore](/.gitignore) by git) which will look like [the example inventory file](./inventory/example-sandbox-yournetid).

Run the following commands (if you haven't already):

```zsh
pipenv sync
pipenv shell
```

This will install all the software defined in [Pipfile](./Pipfile) which includes Ansible and launch your virtual environment.

Then try to use the following Ansible:

## Ansible ad-hoc

With your keys added try the following ad-hoc commands

```zsh
ansible netid_sandbox -u pulsys -m ping -vvvv
```

We will see that the "ping" module has succeeded. The `"changed" : false` output
tells us that the executing module did not change the state of the server. The
`"ping": "pong"` text is output that is specific to the ping module. The `-m`
flag part of the command represents module and the `-vvvv` part is the verbosity
levels in the output.

Run the following now:

```zsh
ansible netid_sandbox -m command -a uptime -u pulsys
```

and

```zsh
ansible netid_sandbox -u pulsys -m command -b -a "tail /var/log/syslog" -u pulsys
```

Here we are using Ansible's
[`command`](https://docs.ansible.com/ansible/latest/modules/command_module.html) module (used by default) and because
`/var/log/syslog` requires sudo privileges we elevate our privileges using the
`-b` flag. (for become).

Finally let's run:

```zsh
ansible netid_sandbox -u pulsys -m apt -b -a "name=htop update_cache=yes state=present"
```

Here we are using Ansible's [`apt`](https://docs.ansible.com/ansible/latest/modules/apt_module.html?highlight=apt) module to run `apt -y update && apt -y install
htop`. It is important to state that you will rarely need to use this but most
ad-hoc commands are useful in quickly getting reports back from hosts under your
management.
