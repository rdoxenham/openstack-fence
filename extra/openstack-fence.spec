Name:		openstack-fence
Version:	1.0
Release:	1%{?dist}
Summary:	openstack-fence is a direct to hypervisor fencing wrapper for OpenStack Nova
Packager:	Rhys Oxenham <roxenham@redhat.com>

Group:		Applications/System
License:	GPLv2+
URL:		http://www.github.com/rdoxenham/openstack-fence

Requires:	fence-agents
Requires:	python-novaclient

%description

openstack-fence is a fencing agent wrapper for OpenStack Nova. Its purpose is to discover the instance name and the hypervisor via the OpenStack instance-id and carry out the fencing via fence_virsh.

%prep

%build

%install

%clean

%files
%defattr(-,root,root,-)
/usr/share/openstack-fence/fence_openstack.conf.sample
%attr(4755, root, root) /usr/bin/fence_openstack

%changelog
* Tue Jan 21 2014 Rhys Oxenham <roxenham@redhat.com> 0.1-1
- Initial release for alpha testing
