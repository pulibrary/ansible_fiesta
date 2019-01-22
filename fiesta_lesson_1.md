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

* Playbooks are YAML files
* Playbooks are a list of dictionaries (consisting of a list of plays)
* Playbooks **MUST** contain a set of hosts to configure, a list of tasks to be
  executed on those hosts

At a minimum that is all that is required to make a playbook.

### Tasks

Our first playbook has six tasks and this is the first one

```bash
- name: remove nginx webserver
      apt:
        name: nginx
        state: absent
        purge: true
      ignore_errors: true
```

The `name` is optional so it would be valid to have this task look like this
(please don't :sweat_smile:):

```bash
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
