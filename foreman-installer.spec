%{?scl:%scl_package foreman-installer}
%{!?scl:%global pkg_name %{name}}

%global foreman_root %{?!scl:%{_datadir}}%{?scl:%{_root_datadir}}/foreman-installer
%global foreman_hash .f5ae2cd

Name:		foreman-installer
Version:	1.0.1
Release:	6%{foreman_hash}%{?dist}
Summary:	Automated Foreman installation and configuration

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/theforeman/foreman-installer
# TODO - put here documentation how tar.gz is created
Source0:	%{pkg_name}-%{version}.tar.gz
BuildArch:  noarch
BuildRequires: sed

Requires:	foreman-installer-puppet-apache
Requires:   httpd

Requires:   foreman-installer-puppet-foreman
Requires:   foreman

Requires:   foreman-installer-puppet-foreman_proxy
Requires:   foreman-proxy

Requires:   foreman-installer-puppet-passenger
Requires:   mod_passenger

Requires:   foreman-installer-puppet-puppet
Requires:   %{?scl_prefix}puppet

Requires:   foreman-installer-puppet-tftp
Requires:   tftp-server

Requires:   foreman-installer-puppet-xinetd
Requires:   xinetd

Requires:   foreman-installer-puppet-dhcp
Requires:   dhcp

Requires:   foreman-installer-puppet-dns
Requires:   bind

%description
Installs Foreman as a standalone application or using apache passenger.

May install an example puppet master setup using passenger as well, including
the tweaks required for Foreman.


%package -n foreman-proxy-installer
Summary:    Automated Foreman Smart Proxy installation and configuration
Requires:   %{?scl_prefix}rubygem(ruby-progressbar)
Requires:   katello-configure
Requires:   foreman-installer-puppet-foreman
Requires:   %{?scl_prefix}ruby

Requires:   foreman-installer-puppet-foreman_proxy
Requires:   foreman-proxy

Requires:   foreman-installer-puppet-puppet
Requires:   %{?scl_prefix}puppet

Requires:   foreman-installer-puppet-tftp
Requires:   tftp-server

Requires:   foreman-installer-puppet-dhcp
Requires:   dhcp

Requires:   foreman-installer-puppet-dns
Requires:   bind

Requires:   foreman-installer-puppet-xinetd
Requires:   xinetd

%description -n foreman-proxy-installer
Installs Foreman Smart Proxy.



%prep
%setup -n %{pkg_name}-%{version} -q


%build
%if %{?scl:1}%{!?scl:0}
    sed -i '1sX/usr/bin/rubyX/usr/bin/ruby193-rubyX' bin/foreman-proxy-configure
    sed -i '1,$sX/usr/bin/puppetX/usr/bin/ruby193-puppetX' bin/foreman-proxy-configure
%endif

%install
install -d -m 755 %{buildroot}%{?!scl:%{_sbindir}}%{?scl:%{_root_sbindir}}
install -m 755 bin/foreman-proxy-configure %{buildroot}%{?!scl:%{_sbindir}}%{?scl:%{_root_sbindir}}

install -d -m 755 %{buildroot}%{foreman_root}
install -m 0644 default-answer-file %{buildroot}%{foreman_root}
install -m 0644 options-format-file %{buildroot}%{foreman_root}

%files
%doc README.md
%{foreman_root}

%files -n foreman-proxy-installer
%{?!scl:%{_sbindir}}%{?scl:%{_root_sbindir}}/foreman-proxy-configure
%{foreman_root}

%changelog
* Fri Apr 05 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-6.f5ae2cd
- Automatic rebase to latest nightly Foreman-installer
- Merge remote-tracking branch 'foreman-installer/master' by rel-eng/build.sh
- mark rel-eng/build.sh as executable
- remove Fedora 17 releasers
- Remove pp file: cli is there already
- Merge branch 'develop'
- Updated modules for 1.1-1 release
- Remove sudo requirement from generate_answers, only run Puppet if root
- Merge remote-tracking branch 'project/develop'
- Allow for modulepaths other than pwd
- Removed the develop branch from clone instructions
- Updated submodules to latest and added option to run puppet to the generator
- Use Puppet's own create_resources function if available
- Add create_resources from puppetlabs to make this work on 2.6
- Ensure the terminal global is always set
- Fix Puppet 2.6 compatibility, parse error with hash in function call
- Use git submodule foreach
- Add answers generator v0.1
- Version bump
- Bump foreman/foreman_proxy/puppet for 1.1RC repo support
- Update README.md
- Bump dhcp/dns/foreman/foreman_proxy/passenger/puppet
- Rename loadyaml to loadanyyaml to prevent stdlib conflict
- bump concat/dhcp/puppet/foreman/tftp
- Throw error when YAML type is unknown
- Change YAML path to /etc/foreman-proxy/answers.yaml for consistency
  Parameterise foreman_installer class for answers.yaml location
- Update foreman, foreman_proxy, and puppet module commits
- Reapply YAML in develop branch

* Mon Feb 11 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-5.eb4cc43
- disable dhcp by default and put dhcp option to default-answer-file
- disable ssl until it is prepared
- add script foreman-proxy-configure
- Update foreman_proxy_installer.pp
- Simple application of the foreman_proxy_insteller with custom values

* Fri Nov 23 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-4.eb4cc43
- rename foreman_proxy-installer to foreman-proxy-installer

* Fri Nov 23 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-3.eb4cc43
- create foreman_proxy-installer subpackage
- package is noarch
- add remaining subpackages and their deps

* Tue Nov 20 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2.eb4cc43
- change to release tagger
- downgrade foreman-installer

* Tue Nov 20 2012 Miroslav Suchý <msuchy@redhat.com> 1.0.3-1.eb4cc43
- new package built with tito


