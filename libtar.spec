Summary:	C library for manipulating tar files
Name:		libtar
Version:	1.2.11
Release:	%mkrel 14
License:	BSD
Group:		System/Libraries
URL:		http://www.feep.net/libtar/
Source0:	ftp://ftp.feep.net/pub/software/libtar/%{name}-%{version}.tar.bz2
Patch0:		libtar-1.2.11-includes.patch
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
Group:		Development/C
%description devel
This package contains the static library and the C headers needed to
build applications with libtar.

%prep
%setup -q
%patch0 -p1 -b .includes

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


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.11-11mdv2011.0
+ Revision: 660284
- mass rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.2.11-10mdv2011.0
+ Revision: 439474
- rebuild

* Thu Nov 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.11-9mdv2009.1
+ Revision: 300379
- drop 64bit-fixes.patch: this 'fix' is bogus as per the discussion at
  http://sourceforge.net/mailarchive/message.php?msg_id=20070803200729.GA7068%%40foursquare.net
  ** API CHANGE **: this 'fix' slightly changed libtar's API, so reverting it
  also 'changes' the API back to the original. Apps that build against libtar
  may be patched to match this API change and hence may not build any more.
  If you maintain such an app, please remove the patch

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.2.11-8mdv2009.0
+ Revision: 268034
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.11-7mdv2009.0
+ Revision: 196263
- rebuild for new era
- decompress patches
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2.11-6mdv2008.0
+ Revision: 58480
- Import libtar


* Wed Aug  2 2006 Götz Waschk <waschk@mandriva.org> 1.2.11-6mdv2007.0
- Rebuild

* Tue Jul 26 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.2.11-5mdk
- fix includes
- 64-bit fixes, this causes a slight API change

* Fri May 20 2005 Götz Waschk <waschk@mandriva.org> 1.2.11-4mdk
- build with -fPIC
- new URLs

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.11-3mdk
- rebuild

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.11-2mdk
- rebuild

* Mon Jun 30 2003 Götz Waschk <waschk@linux-mandrake.com> 1.2.11-1mdk
- initial package
