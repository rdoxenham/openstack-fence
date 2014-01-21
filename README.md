#**OpenStack Fencing Tool**#

Author: Rhys Oxenham <roxenham@redhat.com>

##**Overview**##

The 'openstack-fence' package is designed as a fencing agent wrapper for fencing instances running on-top of an OpenStack environment. This tool can be used as part of a HA cluster to help guarantee a fence success instead of relying on OpenStack to perform a power-down of an instance. Whilst it relies on fencing agents for libvirt, the tool facilitates the configuration and execution of the fence upon the target instance.

##**Building**##

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

