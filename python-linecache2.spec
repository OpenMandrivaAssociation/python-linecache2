%global srcname linecache2

Name:           python-%{srcname}
Version:        1.0.0
Release:        3
Summary:        Backports of the linecache module

Group:          Development/Python
License:        Python Software Foundation License
URL:            https://github.com/testing-cabal/linecache2
Source0:        http://pypi.python.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pip)
%description
A backport of linecache to older supported Pythons.

%package -n     python2-%{srcname}
Summary:        Backports of the linecache module
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2dist(setuptools)

%description -n python2-%{srcname}
A backport of linecache to older supported Pythons.

%prep
%setup -q -n %{srcname}-%{version}

cp -a . %{py3dir}

%build
pushd %{py3dir}
%{__python3} setup.py build
popd

%{__python2} setup.py build

%install
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python3_sitelib}/%{srcname}/tests
popd

%{__python2} setup.py install --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python2_sitelib}/%{srcname}/tests

%files
%doc AUTHORS ChangeLog README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files -n python2-%{srcname}
%doc AUTHORS ChangeLog README.rst
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
