# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
 
# config.vm.network "public_network", auto_config: false
 config.vm.define "nginx" do  |web|
   web.vm.box = "hashicorp/precise32"
   web.vm.network "public_network", auto_config: false
   web.vm.network "forwarded_port", guest: 80, host: 8082
   
   web.vm.provider "virtualbox" do |vb|
     vb.name = "Server"
     vb.memory = "512"
     vb.cpus = "1"
    #: vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
   end
   web.vm.provision "shell",
     run: "always",
     inline: "ifconfig eth1 10.0.2.3 netmask 255.255.255.0 up"
 end

 config.vm.define "Python" do  |py|
   py.vm.box = "hashicorp/precise32"
   py.vm.network "public_network", auto_config: false 
 #  py.vm.network "forwarded_port", guest: 22, host: 10122, id: "ssh"

   py.vm.provider "virtualbox" do |vb|
     vb.name = "Application"
     vb.memory = "512"
     vb.cpus = "1"
   end

   py.vm.provision "shell",
     run: "always",
     inline: "ifconfig eth1 10.0.2.4 netmask 255.255.255.0 up"
  #  inline: "uwsgi --socket 10.0.2.4:3031 --wsgi-file /var/www/*py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191"
 end

 config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
        ansible.sudo = true
 end
end
