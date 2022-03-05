#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Functional library for data processing
Summary(pl.UTF-8):	Biblioteka funkcyjna do przetwarzania danych
Name:		python-railroad
Version:	0.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/railroad/
Source0:	https://files.pythonhosted.org/packages/source/r/railroad/railroad-%{version}.tar.gz
# Source0-md5:	861f7b6c59eb087a5f3fbfd1fee2c805
Patch0:		%{name}-py3-requires.patch
URL:		https://pypi.org/project/railroad/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-boltons >= 16.5.0
BuildRequires:	python-funcsigs >= 1.0.2
BuildRequires:	python-mock
BuildRequires:	python-pytest
BuildRequires:	python-six >= 1.7.3
BuildRequires:	python-toolz >= 0.7.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-boltons >= 16.5.0
BuildRequires:	python3-pytest
BuildRequires:	python3-six >= 1.7.3
BuildRequires:	python3-toolz >= 0.7.4
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functional library for data processing.

%description -l pl.UTF-8
Biblioteka funkcyjna do przetwarzania danych.

%package -n python3-railroad
Summary:	Functional library for data processing
Summary(pl.UTF-8):	Biblioteka funkcyjna do przetwarzania danych
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-railroad
Functional library for data processing.

%description -n python3-railroad -l pl.UTF-8
Biblioteka funkcyjna do przetwarzania danych.

%prep
%setup -q -n railroad-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/railroad
%{py_sitescriptdir}/railroad-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-railroad
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/railroad
%{py3_sitescriptdir}/railroad-%{version}-py*.egg-info
%endif
