# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "docker-test"
  config.vm.synced_folder ".", "/home/vagrant/linux-containers-from-scratch"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "docker-test"
    vb.memory = "1024"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    # upgrade to newest packages
    apt-get update
    apt-get upgrade -y

    # setup docker
    curl -fsSL https://get.docker.com | sh
    usermod -aG docker vagrant

    # cgroups
    apt-get install -y cgroup-tools
  SHELL
end
