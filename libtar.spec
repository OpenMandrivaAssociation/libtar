%define major 1
%define libname %mklibname tar %{major}
%define develname %mklibname -d tar

%define sdevname %mklibname tar -d -s

Summary:	C library for manipulating tar files
Name:		libtar
Version:	1.2.20
Release:	7
License:	BSD
Group:		System/Libraries
Url:		http://www.feep.net/libtar/
Source0:	ftp://ftp.feep.net/pub/software/libtar/%{name}-%{version}.tar.gz
Patch1:         libtar-1.2.11-missing-protos.patch
Patch2:         libtar-macro.patch
Patch4:         libtar-1.2.11-mem-deref.patch
Patch5:         libtar-1.2.20-fix-memleak.patch
Patch6:         libtar-1.2.11-bz729009.patch
Patch7:         libtar-1.2.11-bz785760.patch
Patch8:		libtar-1.2.20-includes.patch
BuildRequires:	pkgconfig(zlib)
Obsoletes:	%{name} <= 1.2.11-16

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
Obsoletes:	%{name}-static-devel < 1.2.11-16
Provides:	%{name}-static-devel = %{EVRD}

%description -n %{sdevname}
This package contains the static library and the C headers needed to
build applications with libtar.

%files -n %{sdevname}
%doc README ChangeLog* COPYRIGHT TODO
%{_libdir}/libtar.a
#----------------------------------------------------------------------------
%package -n	%libname
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %libname
This package contains the shared library for %{name}.

%files -n %{libname}
%{_libdir}/libtar.so.%{major}
%{_libdir}/libtar.so.%{major}.*
#----------------------------------------------------------------------------
%package -n	%develname
Summary:	Development files and headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-devel < %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
This package contains the shared library and the C headers needed to
build applications with libtar.

%files -n %{develname}
%{_libdir}/libtar.so
%{_includedir}/libtar*.h
%{_mandir}/man3/*.3*

#----------------------------------------------------------------------------
%prep
%setup -qn %{name}
%apply_patches

%build
# set correct version for .so build
%define ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' \
  lib/Makefile.in

autoreconf -fiv

export CFLAGS="%{optflags} -fPIC"
%configure2_5x --enable-static
%make

%install
%makeinstall_std
