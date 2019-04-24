## Ansible Variables, Inventory, Groups

The default way to describe your hosts is to list them in text files called
inventory files. By default ansible will try to locate your file in
`/etc/ansible/hosts` unless -as is our case- there is an `ansible.cfg` file
located in the directory. Ansible by default adds the localhost to the
inventory.

Our `ansible.cfg` file here points to a host file. Ansible supports multiple
transport mechanisms which can be modified with the `[connection] If we need to
override any of ansible's default behavior we would enter that under the
`[default]`

### Groups

When performing configuration tasks we typically want to perform actions on
groups of hosts, rather than an individual host. Ansible by default defines a
group called `all` which includes all of the hosts in the inventory. 

Run:

```bash
ansible all -u pulsys -a "date"
```

Take a look at the
[figgy](https://github.com/pulibrary/princeton_ansible/blob/master/hosts) list
of hosts involved.

That could be re-written like so:

```yaml
[figgy:children]
lib-proc4.princeton.edu
lib-proc5.princeton.edu
lib-proc6.princeton.edu
```

or

```yaml
[proc-machines]
lib-proc[1:7].princeton.edu
```

while our needs lean simple today this may not always be the case.

### Host and Group Variables

As your needs get more complex creating group or host variables becomes
increasingly important.
