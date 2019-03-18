## Basic Role Structure

An ansible role with a name `apache2` will have the apache2 role typically go in
the `roles/apache2` directory. This will contain the following files and
directory typically.

```
roles/apache2/tasks/main.yml
```
Tasks
```
roles/apache2/templates/
```
Hold Jinja2 template files
```
roles/apache2/handlers/main.yml
```
Handlers
```
roles/apache2/vars/main.yml
```
Variables that shouldn't be overriden
```
roles/apache2/defaults/main.yml
```
Default variables that can be overriden
```
roles/apache2/meta/main.yml
```
Dependency information about the role

Each individual file is optional. Ansible will look for roles in the `roles`
directory alongside your playbooks. It will default to `/etc/ansible/roles`
unless this -as is our case- is overriden by the `ansible.cfg` file.

### Example Database and Drupal Roles

Lets create a role that sets up Drupal with a PostgreSQL database. One could
create this role and name it `libwww` but instead we are going to break out this
up into a separate role called `database`. This will eventually allow us for
example to have a separate database on a separate host from the drupal
application.

### Using roles in playbooks

Role assignment playbook is done like this.
[playbooks/drupal-install.yml](playbooks/drupal-install.yml)

```yaml
---
- name: deploy drupal
  hosts: web
  vars_files:
    - secrets.yml
  pre_tasks:
    - name: update the apt cache
      apt:
        update_cache: true

  roles:
    - role: database
      database_name: "{{ drupal_proj_name }}"
      database_user: "{{ drupal_proj_name }}"
    - role: libwww
      database_name: "{{ drupal_proj_name }}"
      database_user: "{{ drupal_proj_name }}"
```

When we use roles, we have a roles section in our playbook. The roles section
expects a list of roles and in our case we have a database and libwww role. We
are passing `database_name` and `database_user` variables which would override
anything in `vars/main.yml` or `defaults/main.yml`. Reading and maintaining this playbook is
much simpler than the incomplete example here [playbooks/drupal-playbook.yml](playbooks/drupal-playbook.yml)

### Pre and Post Tasks

There will be times where one may want to run `pre_tasks` prior to running the
roles. In our example here we have a simple one of making sure we've updated our
cache before you deploy `libwww` there's examples on
[https://github.com/pulibrary/princeton_ansible/blob/2107a37d60f21cd0c93e249a502438e96b6dba31/playbooks/awx.yml#L13](https://github.com/pulibrary/princeton_ansible/blob/2107a37d60f21cd0c93e249a502438e96b6dba31/playbooks/awx.yml#L13)
that post to slack after completion of the roles.

#### Database role

This role which will have the following files

* [roles/database/tasks/main.yml](roles/database/tasks/main.yml)
* [roles/database/defaults/main.yml](roles/database/defaults/main.yml)
* [roles/database/handlers/main.yml](roles/database/handlers/main.yml)
* [roles/database/files/pg_hba.conf](roles/database/files/pg_hba.conf)
* [roles/database/files/postgresql.conf](roles/database/files/postgresql.conf)

We have to customized configuration files (this is a simple example) that would
generally be better suited using Jinja templating but will do for now.

`postgresql.conf`: Allows postgresql to listen on any interface.
`pg_hba.conf`: simplifies connection for our example.

#### Libwww Role

The role which install drupal will have the following files

* [roles/libwww/tasks/main.yml](roles/libwww/tasks/main.yml)
* [roles/libwww/tasks/apache.yml](roles/libwww/tasks/apache.yml)
* [roles/libwww/tasks/drupal.yml](roles/libwww/tasks/drupal.yml)
* [roles/libwww/tasks/php.yml](roles/libwww/tasks/php.yml)
* [roles/libwww/tasks/php.yml](roles/libwww/tasks/php.yml)
* [roles/libwww/tasks/extras.yml](roles/libwww/tasks/extras.yml)
* [roles/libwww/tasks/postgresql.yml](roles/libwww/tasks/postgresql.yml)
* [roles/libwww/templates/apache/vhosts.conf](roles/libwww/templates/apache/vhosts.conf)
* [roles/libwww/defaults/main.yml](roles/libwww/defaults/main.yml)
* [roles/libwww/handlers/main.yml](roles/libwww/handlers/main.yml)
* [roles/libwww/vars/main.yml](roles/libwww/vars/main.yml)

In this role we do have defined variables that we will use in the role that
contain the Jinja templating. 
