# OpenStack External Test Platform

!! THIS REPOSITORY IS VERY MUCH A WORK IN PROGRESS !!

PLEASE USE AT YOUR OWN RISK AND PROVIDE FEEDBACK IF YOU CAN!

This repository contains documentation and modules in a variety
of configuration management systems that demonstrates setting up
a real-world external testing platform that links with the upstream
OpenStack CI platform.

It installs Jenkins, Jenkins Job Builder (JJB), the Gerrit
Jenkins plugin, and a set of scripts that make running a variety
of OpenStack integration tests easy.

Currently only Puppet modules are complete and tested. Ansible scripts
will follow afterwards.

## Pre-requisites

The following are pre-requisite steps before you install anything:

1. Get a Gerrit account for your testing system registered

2. Ensure base packages installed on your target hosts/VMs

3. Set up your data repository

Below are detailed instructions for each step.

### Registering an Upstream Gerrit Account

You will need to register a Gerrit account with the upstream OpenStack
CI platform. You can read the instructions for doing
[that](http://ci.openstack.org/third_party.html#requesting-a-service-account)

### Ensure Basic Packages on Hosts/VMs

We will be installing a Jenkins master server and infrastructure on one
host or virtual machine and one or more Jenkins slave servers on hosts or VMs.

On each of these target nodes, you will want the base image to have the 
`wget`, `openssl`, `ssl-cert` and `ca-certificates` packages installed before
running anything in this repository.


## Usage

### Setting up the Jenkins Master

#### Installation

On the machine you will use as your Jenkins master, run the following:

```
wget https://raw.github.com/mellanox-openstack/os-ext-testing/mlnx/puppet/install_master.sh
bash install_master.sh
```

The script will install Puppet, create an SSH key for the Jenkins master, create
self-signed certificates for Apache, and then will ask you for the URL of the Git
repository you are using as your data repository (see Prerequisites #3 above). Enter
the URL of your data repository and hit Enter.

Puppet will proceed to set up the Jenkins master.

#### Load Jenkins Up with Your Jobs

Run the following at the command line:

    sudo jenkins-jobs --flush-cache --delete-old update /etc/jenkins_jobs/config


#### Configuration

After Puppet installs Jenkins and Zuul, you will need to do a couple manual configuration
steps in the Jenkins UI.

1. Go to the Jenkins web UI. By default, this will be `http://$IP_OF_MASTER:8080`

2. Click the `Manage Jenkins` link on the left

3. Click the `Configure System` link

4. Scroll down until you see "Gearman Plugin Config". Check the "Enable Gearman" checkbox.

5. Click the "Test Connection" button and verify Jenkins connects to Gearman.

6. Scroll down to the bottom of the page and click `Save`

7. At the command line, do this::

    sudo service zuul restart
