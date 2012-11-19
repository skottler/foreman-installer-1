%global foreman_root %{_datarootdir}/foreman-installer

Name:		foreman-installer
Version:	1.0.1
Release:	0%{?dist}
Summary:	Automated Foreman installation and configuration

Group:		Applications/System
License:	GPLv3
URL:		https://github.com/theforeman/foreman-installer
# TODO - put here documentation how tar.gz is created
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:	
#Requires:	

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
mkdir -p %{buildroot}/%{foreman_root}
for MODULE in apache concat dhcp dns foreman foreman_proxy git passenger puppet tftp xinetd; do
   mkdir -p %{buildroot}/%{foreman_root}/$MODULE
   cp -a $MODULE/* %{buildroot}/%{foreman_root}/$MODULE/
done
find %{buildroot}/%{foreman_root} -name .git | while read i; do rm -f $i; done

%files
%doc README.md
%{foreman_root}



%changelog

