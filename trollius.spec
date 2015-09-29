#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : trollius
Version  : 2.0
Release  : 11
URL      : https://pypi.python.org/packages/source/t/trollius/trollius-2.0.tar.gz
Source0  : https://pypi.python.org/packages/source/t/trollius/trollius-2.0.tar.gz
Summary  : Port of the Tulip project (asyncio module, PEP 3156) on Python 2
Group    : Development/Tools
License  : Apache-2.0
Requires: trollius-python
BuildRequires : futures
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Trollius provides infrastructure for writing single-threaded concurrent
code using coroutines, multiplexing I/O access over sockets and other
resources, running network clients and servers, and other related primitives.
Here is a more detailed list of the package contents:

%package python
Summary: python components for the trollius package.
Group: Default

%description python
python components for the trollius package.


%prep
%setup -q -n trollius-2.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 runtests.py -v 1
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
