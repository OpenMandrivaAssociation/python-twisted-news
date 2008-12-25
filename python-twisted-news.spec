%define version 8.1.0
%define rel 21

Summary:        An NNTP protocol implementation together with clients and servers
Name:           python-twisted-news
Version: %version
Release: %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/News/8.1/TwistedNews-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/trac/wiki/TwistedNews
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core

%description
Twisted News provides a very basic NNTP server, as well as an NNTP client 
protocol implementation. Two messages storage systems are supported: the 
DB-API 2.0 backend stores and indexes messages in any compatible SQL 
database; the Twisted dirdbm backend uses serialized Python objects 
stored directly on the filesystem for message storage. Twisted News 
also has very rudamentary support for moderated groups.

%prep
%setup -q -n TwistedNews-%version

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc  LICENSE README
%py_platsitedir/twisted/news/
%py_platsitedir/twisted/plugins/*
%py_platsitedir/*.egg-info
