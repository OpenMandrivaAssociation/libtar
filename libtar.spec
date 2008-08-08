Summary:	C library for manipulating tar files
Name:		libtar
Version:	1.2.11
Release:	%mkrel 8
License:	BSD
Group:		System/Libraries
URL:		http://www.feep.net/libtar/
Source0:	ftp://ftp.feep.net/pub/software/libtar/%{name}-%{version}.tar.bz2
Patch0:		libtar-1.2.11-includes.patch
Patch1:		libtar-1.2.11-64bit-fixes.patch
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
libtar is a library for manipulating tar files from within C programs.
Here are some of its features:

  * Handles both POSIX tar file format and the GNU extensions.
  * API provides functions for easy use, such as tar_extract_all().
  * Also provides functions for more granular use, such as 
    tar_append_regfile().

%package devel
Summary:	Development files and headers for %{name}
Group:	Development/C
%description devel
This package contains the static library and the C headers needed to
build applications with libtar.

%prep
%setup -q
%patch0 -p1 -b .includes
%patch1 -p1 -b .64bit-fixes

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/libtar

%files devel
%defattr(-,root,root)
%doc README ChangeLog* COPYRIGHT TODO
%{_includedir}/libtar*.h
%{_libdir}/libtar.a
%{_mandir}/man3/*.3*
