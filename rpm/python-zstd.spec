
%global zstd_version 1.4.5

Name:           python-zstd
Version:        1.5.0.2
Release:        0
Summary:        Zstd Bindings for Python

License:        BSD
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source:         python-zstd-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libzstd) >= %{zstd_version}

%description
Simple Python bindings for the Zstd compression library.

%package -n     python3-zstd
Summary:        %{summary}
%{?python_provide:%python_provide python3-zstd}
# The library does not do symbol versioning to fully match automatically on
Requires:       libzstd%{?_isa} >= %{zstd_version}

%description -n python3-zstd
Simple Python bindings for the Zstd compression library.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}
# Remove bundled egg-info
rm -rf python-zstd.egg-info
# Remove bundled zstd library
rm -rf zstd/

%build
%py3_build -- --legacy --external

%install
%py3_install

%files -n python3-zstd
%license LICENSE
%doc README.rst
%{python3_sitearch}/*
