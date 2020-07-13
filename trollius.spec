#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : trollius
Version  : 2.2.post1
Release  : 38
URL      : https://files.pythonhosted.org/packages/0b/31/356ae13ad4df58f963e9954d55118f6cffdb3a903c1547973ad7bc347fb9/trollius-2.2.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/31/356ae13ad4df58f963e9954d55118f6cffdb3a903c1547973ad7bc347fb9/trollius-2.2.post1.tar.gz
Summary  : Deprecated, unmaintained port of the asyncio module (PEP 3156) on Python 2
Group    : Development/Tools
License  : Apache-2.0
Requires: trollius-license = %{version}-%{release}
Requires: trollius-python = %{version}-%{release}
Requires: trollius-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : python-mock
BuildRequires : six

%description
========
Trollius
========

.. image:: http://unmaintained.tech/badge.svg
   :target: http://unmaintained.tech/
   :alt: No Maintenance Intended

.. warning::
   The Trollius project is deprecated and unsupported. It is on PyPI
   to support existing dependencies only.

%package license
Summary: license components for the trollius package.
Group: Default

%description license
license components for the trollius package.


%package python
Summary: python components for the trollius package.
Group: Default
Requires: trollius-python3 = %{version}-%{release}

%description python
python components for the trollius package.


%package python3
Summary: python3 components for the trollius package.
Group: Default
Requires: python3-core
Provides: pypi(trollius)

%description python3
python3 components for the trollius package.


%prep
%setup -q -n trollius-2.2.post1
cd %{_builddir}/trollius-2.2.post1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582908263
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/trollius
cp %{_builddir}/trollius-2.2.post1/COPYING %{buildroot}/usr/share/package-licenses/trollius/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/trollius/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
