%global foreman_root %{_datarootdir}/foreman-installer
%global foreman_hash .eb4cc43

Name:		foreman-installer
Version:	1.0.1
Release:	1%{foreman_hash}%{?dist}
Summary:	Automated Foreman installation and configuration

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/theforeman/foreman-installer
# TODO - put here documentation how tar.gz is created
Source0:	%{name}-%{version}.tar.gz

Requires:	foreman-installer-puppet-apache
Requires:   foreman-installer-puppet-foreman
Requires:   foreman-installer-puppet-foreman_proxy
Requires:   foreman-installer-puppet-passenger
Requires:   foreman-installer-puppet-puppet
Requires:   foreman-installer-puppet-tftp
Requires:   foreman-installer-puppet-xinetd
Requires:   puppet

%description
Installs Foreman as a standalone application or using apache passenger.

Installs Foreman Proxy

May install an example puppet master setup using passenger as well, including
the tweaks required for foreman.

%prep
%setup -q


%build
#nothing to do

%install
#nothing to do

%files
%doc README.md



%changelog
* Tue Nov 20 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-1.eb4cc43
- new package built with tito


