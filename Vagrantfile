BOX_IMAGE = "hashicorp/bionic64"
ANSIBLE_CONTROL_IP_ADDR = "192.168.56.220"
JENKINS_HOST_IP_ADDR = "192.168.56.221"
MONGO_HOST_IP_ADDR = "192.168.56.223"
NODE_RED_HOST_IP_ADDR = "192.168.56.224"


Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Starting provisioning"
  
  config.vm.define "jenkins_host" do |jenkins_host|
    jenkins_host.vm.box = BOX_IMAGE
    jenkins_host.vm.hostname = "jenkins-host"
    jenkins_host.vm.network "private_network", ip: JENKINS_HOST_IP_ADDR
  end

  config.vm.define "mongo_host" do |mongo_host|
    mongo_host.vm.box = BOX_IMAGE
    mongo_host.vm.hostname = "MONGO-host"
    mongo_host.vm.network "private_network", ip: MONGO_HOST_IP_ADDR
    mongo_host.vm.provision "shell", inline: <<-SHELL
      apt update -y 
      apt install -y mongodb
      sed -i 's/127.0.0.1/0.0.0.0/' /etc/mongodb.conf
      cat /etc/mongodb.conf
      systemctl restart mongodb
    SHELL
  end

  config.vm.define "node_red_host" do |node_red_host|
    node_red_host.vm.box = BOX_IMAGE
    node_red_host.vm.hostname = "node-red-host"
    node_red_host.vm.network "private_network", ip: NODE_RED_HOST_IP_ADDR
    node_red_host.vm.provision "shell", inline: <<-SHELL
      apt update
      apt install software-properties-common -y
      apt install nodejs -y
      apt install npm -y
      apt install mongodb -y
      npm install -g --unsafe-perm node-red node-red-admin
    SHELL
  end

  config.vm.define "ansible_control" do |ansible_control|
    ansible_control.vm.box = BOX_IMAGE
    ansible_control.vm.hostname = "ansible-control"
    ansible_control.vm.network "private_network", ip: ANSIBLE_CONTROL_IP_ADDR
    ansible_control.vm.synced_folder "ansible/", "/dunwoody/paved_road/ansible", create: true
    
    ansible_control.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install software-properties-common -y
      apt-add-repository --yes --update ppa:ansible/ansible
      apt-get install ansible -y
    SHELL

    ansible_control.vm.provision "shell", privileged: false, inline: <<-SHELL
        ssh-keyscan -H 192.168.56.21 >> ~/.ssh/known_hosts
    SHELL

    ansible_control.vm.provision "ansible_local" do |ansible_config|
      ansible_config.playbook = "/dunwoody/paved_road/ansible/plays/config-ansible.yml"
      ansible_config.limit = "ansible_control"
      ansible_config.inventory_path = "/dunwoody/paved_road/ansible/inventory/hosts.yml"
    end

    ansible_control.vm.provision "ansible_local" do |jenkins_config|
      jenkins_config.playbook = "/dunwoody/paved_road/ansible/plays/config-jenkins.yml"
      jenkins_config.limit = "jenkins_host"
      jenkins_config.inventory_path = "/dunwoody/paved_road/ansible/inventory/hosts.yml"
    end

    ansible_control.vm.provision "ansible_local" do |docker_config|
      docker_config.playbook = "/dunwoody/paved_road/ansible/plays/config-docker.yml"
      docker_config.limit = "jenkins_host"
      docker_config.inventory_path = "/dunwoody/paved_road/ansible/inventory/hosts.yml"
    end
  end
end
