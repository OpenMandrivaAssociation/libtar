%define name libtar
%define version 1.2.11
%define release %mkrel 6

Summary:  C library for manipulating tar files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.feep.net/pub/software/libtar/%{name}-%{version}.tar.bz2
Patch0: libtar-1.2.11-includes.patch.bz2
Patch1: libtar-1.2.11-64bit-fixes.patch.bz2
License: BSD
Group: System/Libraries
URL: http://www.feep.net/libtar/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: zlib-devel

%description
libtar is a library for manipulating tar files from within C programs.
Here are some of its features:

  * Handles both POSIX tar file format and the GNU extensions.
  * API provides functions for easy use, such as tar_extract_all().
  * Also provides functions for more granular use, such as 
    tar_append_regfile().

%package devel
Group: Development/C
Summary: C library for manipulating tar files - headers and static library 

%description devel
libtar is a library for manipulating tar files from within C programs.
Here are some of its features:

  * Handles both POSIX tar file format and the GNU extensions.
  * API provides functions for easy use, such as tar_extract_all().
  * Also provides functions for more granular use, such as 
    tar_append_regfile().

This package contains the static library and the C headers needed to
build applications with libtar.

%prep
%setup -q
%patch0 -p1 -b .includes
%patch1 -p1 -b .64bit-fixes

%build
export CFLAGS="%optflags -fPIC"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYRIGHT
%_bindir/libtar

%files devel
%defattr(-,root,root)
%doc README ChangeLog* COPYRIGHT TODO
%_includedir/libtar*.h
%_libdir/libtar.a
%_mandir/man3/*.3*
