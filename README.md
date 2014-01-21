#**OpenStack Fencing Tool**#

Author: Rhys Oxenham <roxenham@redhat.com>

##**Overview**##

The 'openstack-fence' package is designed as a fencing agent wrapper for fencing instances running on-top of an OpenStack environment. This tool can be used as part of a HA cluster to help guarantee a fence success instead of relying on OpenStack to perform a power-down of an instance. Whilst it relies on fencing agents for libvirt, the tool facilitates the configuration and execution of the fence upon the target instance. It first queries the OpenStack Nova API to discover the instance's name and the hypervisor it resides on and then brokers the fence via _ssh_ (fence_virsh).

No modification of OpenStack or any of the sub-components are required to make use of this application. Note that his was written specifically for Red Hat based platforms although should work with other distributions - your mileage may vary! 

**Disclaimer**: I take _no_ responsibility for any losses incurred whilst using this code. This is **not** a supported or accredited package from Red Hat - usage is at your own risk! :-)

##**Building & Installation**##

The code provided within GitHub is source-code only, therefore to install as a deployable package, a build file is provided (build.xml). The steps below will help you build the package:

	# yum install rpm-build ant* git -y
	
Once these packages have been installed, clone the repository:

	# git clone https://github.com/rdoxenham/openstack-fence.git
	
Then, execute the build:

	# cd openstack-fence && ant
	
Once the build has finished, an RPM will be built for the system it was created on. A temporary 'build' directory is placed within the same directory and you'll be able to find the rpm in there, the code output from ant provides the location. For example:

	[rpm] Wrote: /root/openstack_fence/build/rpm/RPMS/x86_64/openstack-fence-1.0-1.el6.x86_64.rpm
	
The package has a number of dependencies, so it's recommended to use the yum package manager to solve them for you during the installation. To proceed with the installation follow these steps, although make sure to change the path to the rpm to represent your environment:

	# yum localinstall /root/openstack_fence/build/rpm/RPMS/x86_64/openstack-fence-1.0-1.el6.x86_64.rpm -y
	
##**Configuration**##

For unattended usage, the tool supports static configuration and is shipped with a sample configuration file found within _/usr/share/openstack-fence/fence_openstack.conf.sample_. If no configuration file is found by the tool, it will ask for the correct details interactively. The correct placement of the configuration file is _/etc/fence_openstack.conf_ and can be copied into place as follows-

	# cp /usr/share/openstack-fence/fence_openstack.conf.sample /etc/fence_openstack.conf
	
The sample configuration file details the configuration options applicable to the usage, however a summary is as follows:

**AUTH_URL**: The authentication URL used by Keystone, e.g. _http://10.0.0.1:35357/v2.0_

**KEYSTONE_USER**: The user (with the **admin** role) to query Nova with

**KEYSTONE_PASS**: The password for the **KEYSTONE_USER**

**KEYSTONE_TENANT**: The tenant/project for the **KEYSTONE_USER**

**FENCE_USER**: The user to connect to the hypervisor as (must match key below)

**FENCE_KEY**: The path to the users private identity/ssh key, e.g. **/root/.ssh/id_rsa**


##**Usage**##

At present, the tool expects that the configuration file is being used if running in unattended mode. It does support running without a configuration file but it will ask for the configuration interactively. Therefore, the remainder of this section assumes the configuration has been set as above.

Usage of the tool can be found using the following:

	# fence_openstack --help
	
To list all of the instances currently running (or the instances available to the currently authenticated user), simply pass the '_--list_' parameter. Examples are demonstrated below:

	# fence_openstack --list
	
	Instance Name: rhel6-rdo
	Instance ID: 7a5e1b68-9ee4-46bd-a2c6-276527b4cf6a
	VM Name: instance-0000000f
	Hypervisor: stack-node4.lab.london.redhat.com
	
The fencing is based directly on the 'Instance ID' as listed above. This can be found in a normal '_nova list_' command and is used for fencing due to it being unique; it's possible to have instances with the same "name". Fencing is carried out as follows:

	# fence_openstack --fence 7a5e1b68-9ee4-46bd-a2c6-276527b4cf6a
	Success: Power off.
	INFO: Successfully fenced instance: rhel6-rdo
	
The return code can then be checked (for exit status checking):

	# echo $?
	0

##**Feedback**##

I very much welcome feedback, comments, critique and merge requests :-)

Please get in contact with me, I'm '**rdo**' on Freenode or available at _roxenham@redhat.com_

##**TODO's**##

1. Enable configuration to be parameterised on the commandline
2. Tidy up (read: implement) error handling for incorrect usernames/passwords/endpoints
3. Test on other platforms