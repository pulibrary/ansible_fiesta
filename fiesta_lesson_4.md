# Testing environment

## Why test roles

* Things break (ansible roles can and do break things)
* Check installation of wanted packages
* Check files for content
* Run services


## Molecule Framework

Revisit [Lesson 0](fiesta_lesson_0.md) to make sure you have all the
pre-requisites needed for testing. Let's revisit what happened there. If we
`cat` the `Pipfile.lock` we will notice to relevant inclusions:

```bash
git pull
pipenv --rm
pipenv install
pipenv shell
```

The `Pipfile.lock` has more details but we have installed. For our purposes
however installing molecule added the following that we will use to test.

* [Molecule](https://molecule.readthedocs.io/en/latest/)
* [Testinfra](https://testinfra.readthedocs.io/en/latest/modules.html)
* [Docker Driver](https://docker-py.readthedocs.io/en/stable/)
* [Ansible-lint](https://github.com/ansible/ansible-lint)
* [Flake8](https://pypi.org/project/flake8/)

### Molecule

Molecule now a first class citizen and is managed by the Ansible project. (Fall
of 2018) It uses Ansible to not just create images and but to test the roles. In
our case we use Docker images. Can also use Vagrant + Virtual Box

### Docker

We use docker to package application source code, Containers will hold our
isolated roles. Thus far it seems less complicated than Vagrant and allows us to
use CI/CD with less overhead.

### Testinfra

A testing framework for infrastructure written in python. In our case we use it
and python test scenarios to validate the docker image state. Goss (is another
verifier written in Go)

### Ansible Lint

This will check our roles for ansible syntax and to ensure we use best practices
for Ansible Galaxy

### Flake8

Python style checker.

### Molecule use

Let's create an nginx role that will have tests in it. 

```bash
molecule init role -r roles/nginx
```

This will create a new directory under `roles` named "nginx" which will look
like and have the format discussed in our [Roles](fiesta_lesson_3.md) with one
additional new directory named `molecule`. As a refresher it will have an
Ansible best practices directory with

* default - default values to variables for the role
* handlers - specific handlers to notify based on actions in Ansible
* meta - Ansible-Galaxy info for the role and/or dependencies
* molecule - molecule specific information (configuration, instance information,
  playbooks to run with molecule
* README.md - Information about the role and really important reminder of the
  importance of documentation
* tasks - tasks for the role
* vars - other variables for the role (generally ones that change infrequently)

With our Testing Environment set up we can now [Write some
tests](fiesta_lesson_5.md)
