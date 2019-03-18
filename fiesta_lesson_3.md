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

Lets create a role that sets up Drupal with a PostgreSQL database.
