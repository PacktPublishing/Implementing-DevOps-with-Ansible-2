# This is an example Vagrantfile which can be used with 
# Vagrant 1.7 and greater to provision an Ubuntu Box 
# using Ansible

Vagrant.require_version ">= 1.7.0"
Vagrant.configure(2) do |config|

config.vm.box = "ubuntu/trusty64"
 config.vm.provision "ansible" do |ansible|
 ansible.verbose = "v"
 ansible.playbook = "playbook.yml"
 end
end