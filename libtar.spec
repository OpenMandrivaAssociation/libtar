%define debug_package	%nil

%define sdevname %mklibname tar -d -s

Summary:	C library for manipulating tar files
Name:		libtar
Version:	1.2.11
Release:	16
License:	BSD
Group:		System/Libraries
Url:		http://www.feep.net/libtar/
Source0:	ftp://ftp.feep.net/pub/software/libtar/%{name}-%{version}.tar.gz
Patch0:		libtar-1.2.11-includes.patch
BuildRequires:	pkgconfig(zlib)

%description
libtar is a library for manipulating tar files from within C programs.
Here are some of its features:

  * Handles both POSIX tar file format and the GNU extensions.
  * API provides functions for easy use, such as tar_extract_all().
  * Also provides functions for more granular use, such as 
    tar_append_regfile().

%files
%{_bindir}/libtar

#----------------------------------------------------------------------------

%package -n %{sdevname}
Summary:	Development files and headers for %{name}
Group:		Development/C
Obsoletes:	%{name}-devel < 1.2.11-16
Provides:	%{name}-devel = %{EVRD}

%description -n %{sdevname}
This package contains the static library and the C headers needed to
build applications with libtar.

%files -n %{sdevname}
%doc README ChangeLog* COPYRIGHT TODO
%{_includedir}/libtar*.h
%{_libdir}/libtar.a
%{_mandir}/man3/*.3*

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x
%make

%install
%makeinstall_std

