# Lesson 0

## Prerequisites

Participants in this exercises will be expected to install the following to work
effectively in this for this tutorial. As a result this repository will be
highly opinionated. The participant is encouraged to work with the tools they
are most comfortable with but we will make the following assumptions. The
participant has the following installed on their networked computer.

* A Package manager
* A Text Editor
* Git
* Vagrant
* Virtualbox
* Python (with virtual environments and pip configured)
* Ansible
* Molecule

## Setup Environment for macOS

* Follow the instructions on the [Homebrew Page](https://brew.sh/) to install
  the package manager.
* Select a programmers Text Editor (For example VIm, Atom)
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
```

Test your installation with:

```bash
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
