#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-userpath
Version  : 1.8.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/85/ee/820c8e5f0a5b4b27fdbf6f40d6c216b6919166780128b6714adf3c201644/userpath-1.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/85/ee/820c8e5f0a5b4b27fdbf6f40d6c216b6919166780128b6714adf3c201644/userpath-1.8.0.tar.gz
Summary  : Cross-platform tool for adding locations to the user PATH
Group    : Development/Tools
License  : MIT
Requires: pypi-userpath-bin = %{version}-%{release}
Requires: pypi-userpath-license = %{version}-%{release}
Requires: pypi-userpath-python = %{version}-%{release}
Requires: pypi-userpath-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# userpath
| | |
| --- | --- |
| CI/CD | [![CI - Test](https://github.com/ofek/userpath/actions/workflows/test.yml/badge.svg)](https://github.com/ofek/userpath/actions/workflows/test.yml) [![CD - Build](https://github.com/ofek/userpath/actions/workflows/build.yml/badge.svg)](https://github.com/ofek/userpath/actions/workflows/build.yml) |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/userpath.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/userpath/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/userpath.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/userpath/) |
| Meta | [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/) [![GitHub Sponsors](https://img.shields.io/github/sponsors/ofek?logo=GitHub%20Sponsors&style=social)](https://github.com/sponsors/ofek) |

%package bin
Summary: bin components for the pypi-userpath package.
Group: Binaries
Requires: pypi-userpath-license = %{version}-%{release}

%description bin
bin components for the pypi-userpath package.


%package license
Summary: license components for the pypi-userpath package.
Group: Default

%description license
license components for the pypi-userpath package.


%package python
Summary: python components for the pypi-userpath package.
Group: Default
Requires: pypi-userpath-python3 = %{version}-%{release}

%description python
python components for the pypi-userpath package.


%package python3
Summary: python3 components for the pypi-userpath package.
Group: Default
Requires: python3-core
Provides: pypi(userpath)
Requires: pypi(click)

%description python3
python3 components for the pypi-userpath package.


%prep
%setup -q -n userpath-1.8.0
cd %{_builddir}/userpath-1.8.0
pushd ..
cp -a userpath-1.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656363722
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-userpath
cp %{_builddir}/userpath-1.8.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-userpath/451d0db67fd4b3e4e5bfcea6e7dcee7a800a081f
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/userpath

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-userpath/451d0db67fd4b3e4e5bfcea6e7dcee7a800a081f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
