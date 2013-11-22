%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

# There is no debug here, but can't build as noarch,
# since some 'twisted' modules are arch-dependent and all these modules
# should be located in the same place
%define debug_package %{nil}

Summary:	An NNTP protocol implementation together with clients and servers
Name:		python-twisted-news
Version:	13.0.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://twistedmatrix.com/trac/wiki/TwistedNews
Source0:	http://twistedmatrix.com/Releases/News/13.0/TwistedNews-%{version}.tar.bz2
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(python)
Requires:	python-twisted-core

%description
Twisted News provides a very basic NNTP server, as well as an NNTP client
protocol implementation. Two messages storage systems are supported:	the
DB-API 2.0 backend stores and indexes messages in any compatible SQL
database; the Twisted dirdbm backend uses serialized Python objects
stored directly on the filesystem for message storage. Twisted News
also has very rudamentary support for moderated groups.

%prep
%setup -qn TwistedNews-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --install-purelib=%{py_platsitedir}

%files
%defattr(0644,root,root,0755)
%doc  LICENSE README
%dir %{py_platsitedir}/twisted/news/
%{py_platsitedir}/twisted/news/*
%{py_platsitedir}/twisted/plugins/*
%{py_platsitedir}/*.egg-info

