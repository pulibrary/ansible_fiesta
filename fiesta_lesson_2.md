## Ansible Variables, Inventory, Groups

As mentioned in [Lesson 0](./fiesta_lesson_0.md) the default way to describe your hosts is to list them in text files called
inventory files. By default ansible will try to locate your file in
`/etc/ansible/hosts` unless -as is in our case- there is an `ansible.cfg` file
located in the directory. Ansible by default adds the localhost to the
inventory.

Our `ansible.cfg` file here points to a host directory. Ansible supports multiple
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
[figgy](https://github.com/pulibrary/princeton_ansible/blob/main/inventory/all_projects/figgy) list
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

Hosts could be present in multiple groups. In the INI [figgy example](https://github.com/pulibrary/princeton_ansible/blob/main/inventory/all_projects/figgy) hosts "figgy1.princeton.edu" and "figgy3.princeton.edu" are grouped as "figgy_production". "figgy1.princeton.edu" is present in "figgy_production_webservers" as well as "production" group. 


### Inventory Host and Group Variables

As your needs get more complex creating group or host variables becomes
increasingly important. In inventory you might like to store variable values that relate to a specific host or group. This [AWS example scenario](https://github.com/pulibrary/princeton_ansible/blob/main/inventory/by_cloud/aws) is common because it defines different connections with different hosts. We provide specific connection for the the AWS hosts and dns names, by default, for all the other hosts. For each host you could also customize the login user pulsys for "new-vm.princeton.edu" and "systems" for "legacy-vm.princeton.edu".


### Variables

In your Playbook it is good practice to use Variables to store all the dynamic values that you need. Editing variables you could reuse your code in the future only parameterized according to your playbook's tasks needs.

The following are not permitted in variable names:

  * no blank spaces							`my var`
  * no dots									`my.var`
  * do not start with number 				`1stvar`
  * do not contain special character		`myvar$1`

Otherwise Ansible allows all the combinations of letters and numbers in variable names.

Run the [variableprint.yml](./playbooks/variableprint.yml) playbook:

```zsh
ansible-playbook -u pulsys playbooks/variableprint.yml --limit netid_sandbox
```

Please note print of the message "Print the value of variable tiger" obtained combining the string with the value of the variable. Also this execution is successful as you could see in the play recap area and the green color. Two tasks are being executed.


You could override the playbook variables specify the value from the command line. Variables set on the command line are called extra variables. Run the following command

```zsh
ansible-playbook -u pulsys -e cat=puma playbooks/variableprint.yml --limit netid_sandbox
```


Please note print of the message "Print the value of variable puma" obtained combining the string with the value of the variable. The value passed from the command line override any playbook value.

#### Host and Group Variables

Host and group variables could be defined in your inventory file (we have already encountered this in the AWS Example. In the left column you could see an example of a host variable. The variable "ansible_host" is assigned the value of an IP address.

You can achieve the same result also using directories to [populate host](https://github.com/pulibrary/princeton_ansible/tree/main/host_vars) and [group variables](https://github.com/pulibrary/princeton_ansible/tree/main/group_vars). The [figgy1 host variables](https://github.com/pulibrary/princeton_ansible/blob/main/host_vars/figgy1.princeton.edu.yml) use a very useful data structure of the Array. You could organize the information in a hierarchical data structure. In the example it’s easy to read the list of datadog_checks: rabbitmq, redisdb, nginx, ruby, and nginx. Each element of the list has properties that datadog will check.

#### Registered variables

Ansible has another very useful data structure, [registered variables](https://github.com/pulibrary/princeton_ansible/blob/5c5b926fe0dc901ff903fc4ad20f94a5e3161bb6/roles/solrcloud/tasks/install.yml#L37). This [playbook](./playbooks/registeredvariables.yml) is an example of the use of registered variables. 

Run the playbook and focus on the output at the end

```zsh
ansible-playbook -u pulsys playbooks/registeredvariables.yml --limit netid_sandbox
```

#### Facts

Variables related to remote systems are called facts. With facts, you can use the behavior or state of one system as configuration on other systems. They provide a very comprehensive report of the (usually) remote host, the operating system, the distribution used, the ip address, the networking configuration, the storage configuration, etc.

List the details of your remote host with the following ad-hoc command:

```zsh
ansible -u pulsys -m setup netid_sandbox
```

The same command can be saved as this [playbook](./playbooks/facts.yml)

```zsh
ansible-playbook -u pulsys playbooks/facts.yml --limit netid_sandbox
```

#### Magic Variables

As we mentioned variables related to remote systems are called facts. With facts, you can use the behavior or state of one system as configuration on other systems. Magic variables are variables related to Ansible.

The most commonly used magic variables on [princeton_ansible](https://github.com/pulibrary/princeton_ansible) are 

  * [inventory_hostname](https://github.com/pulibrary/princeton_ansible/blob/8501dffa0b81d95d6258b85c05ae394388480dda/roles/omp/templates/omp.conf.j2#L16)
  * [omit](https://github.com/pulibrary/princeton_ansible/blob/48e0a98b4b2ce2b5b891a0d0a7adbd3bf60e5eb5/roles/mysql/tasks/main.yml)

which contains the name of the host configured in the inventory and allows one to omit an option in a task respectively. More on magic variables can be found in [Ansible's Documentation](https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html#special-variables)
