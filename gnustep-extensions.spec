# This package is not relocatable
%define ver	0.8.5
%define prefix 	/usr
%define gsr 	%{prefix}/GNUstep
Name: 		gnustep-extensions
Version: 	%{ver}
Release: 	1
Source: 	ftp://ftp.gnustep.org/pub/gnustep/libs/extensions-%{ver}.tar.gz
Copyright: 	BSD
Group: 		Development
Summary: 	GNUstep Foundation Extensions Library
Packager:	Red Hat Contrib|Net <rhcn-bugs@redhat.com>
Distribution:	Red Hat Contrib|Net
Vendor:		The Seawood Project
URL:		http://www.gnustep.org/
BuildRoot: 	/var/tmp/build-%{name}
Requires:	gnustep-make gnustep-base

%description
This package contains some classes that extend the basic behavior of
Foundation classes by adding some features. The current extensions are an
extended exception handling mechanism, a garbage collector, some classes
that allow you to easily create methods that accept printf-like arguments and
two classes for portable archiving and unarchiving Objective-C data.

This package is built with library-combo gnu-gnu-gnu-xraw.

%prep
%setup -q -n extensions-%{ver}

%build
if [ -z "$GNUSTEP_SYSTEM_ROOT" ]; then
   . %{gsr}/Makefiles/GNUstep.sh 
fi
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{gsr} --with-library-combo=gnu-gnu-gnu-xraw
make

%install
if [ -z "$GNUSTEP_SYSTEM_ROOT" ]; then
   . %{gsr}/Makefiles/GNUstep.sh 
fi
rm -rf $RPM_BUILD_ROOT
make install GNUSTEP_INSTALLATION_DIR=${RPM_BUILD_ROOT}%{gsr}

cat > filelist.rpm.in << EOF
%defattr (-, root, root)
%doc COPYING ChangeLog NEWS README Version
%{gsr}/Libraries/GSARCH/GSOS/gnu-gnu-gnu-xraw/lib*.so*
%{gsr}/Headers/gnustep/extensions
%{gsr}/Makefiles/extensions.make
EOF

sed -e "s|GSARCH|${GNUSTEP_HOST_CPU}|" -e "s|GSOS|${GNUSTEP_HOST_OS}|" < filelist.rpm.in > filelist.rpm

%ifos Linux
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif

%files -f filelist.rpm

%changelog
* Sat Mar 13 1999 Christopher Seawood <cls@seawood.org>
- Version 0.8.5 released

* Tue Mar 02 1999 Christopher Seawood <cls@seawood.org>
- Updated from CVS

* Sat Feb 06 1999 Christopher Seawood <cls@seawood.org>
- Split into separate rpm from gnustep-core
