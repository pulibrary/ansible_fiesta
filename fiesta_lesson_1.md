## Preliminaries

Make sure you have a Github account and your user is part of the [pulibrary
organization](https://github.com/pulibrary). The rest of the exercises will
require access to a VM in our datacenter.

Make sure you can VPN onto the princeton network. You will be unable to do any
of the exercises.

## Playbook One

We will configure the two test servers to use the
[Nginx](https://www.nginx.com/) webserver. This will not differ significantly
than installing `htop` in our first lesson. While the ad-hoc command ran a step
on the remote machine our playbook below will consist of a series of tasks to
set up and configure the webserver

Look at the contents of:
[playbooks/nginx-install.yml](playbooks/nginx-install.yml)

## Playbook Anatomy

A playbook contains one or more plays. A play connects a set of hosts with a
series of tasks. Each task is associated with one module.

* Playbooks are YAML files
* Playbooks are a list of dictionaries (consisting of a list of plays)
* Playbooks **MUST** contain a set of hosts to configure, a list of tasks to be
  executed on those hosts

At a minimum that is all that is required to make a playbook.

### Tasks

Our first playbook has six tasks and this is the first one

```yaml
- name: remove nginx webserver
      apt:
        name: nginx
        state: absent
        purge: true
      ignore_errors: true
```

The `name` is optional so it would be valid to have this task look like this
(please don't :sweat_smile:):

```yaml
  - apt:
      name: nginx
      state: absent
      purge: true
    ignore_errors: true
```

Names serve as good reminders for the intent of the task and can be useful for
those collaborating with you. (including yourself) Also important to note that
ansible has the `--start-at-task <task name>` flag which can be used by
`ansible-playbook` to start a playbook in the middle of the task and you will
need to point to that reference point.

Tasks have keys with the name of a module and a value with the arguments to that
module. In the one above `apt` is the module name and the arguments are
`name=nginx` and `purge=true`

These arguments tell the `apt` module to uninstall the package named `nginx` and
purge it. (the equivalent of doing `apt -y purge nginx`)

### Modules

Modules are generically packaged scripts that come with Ansible. The perform
actions on the host. Thus far we've seen.

* `apt` which installs and removes packages using the `apt` package manager
* `copy` which copies files from local machine to the hosts. If you read the
  documentation further it can also copy remote files. 
* `file` sets the attribute of a file, directory or symlink
* `service` starts stops or restarts a service
* `template` generates a new file to be copied to the hosts

## Run the playbooks

To run the playbooks described above run the following:

```bash
ansible-playbook -u playbooks/nginx-install.yml
```
