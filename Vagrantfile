# -*- mode: ruby -*-
# vi: set ft=ruby :

# you're doing.
Vagrant.configure(2) do |config|
  # https://docs.vagrantup.com.

  config.vm.box = "princeton_box"
  config.vm.network "forwarded_port", guest: 80, host: 18584 # apache web server in production mode
  config.vm.define "nginx"

  # Provider-specific configuration for VirtualBox:
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 4096 # if your system can afford it, definitely increase the memory allocation here
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  # Enable provisioning ansible project
  # # Enable provisioning ansible project
  config.vm.provision "ansible" do |ansible|
    ansible.groups = {
        "nginx" => ["nginx"],
    }
    # ansible.verbose = 'vvv'
    ansible.playbook = "playbooks/nginx-role.yml"
    config.ssh.private_key_path = "pulsys_rsa_key"
    config.ssh.username = "pulsys"
  end
end
