Summary:	GNUstep Foundation Extensions Library
Summary(pl):	Biblioteka rozszerzeñ GNUstep
Name:		gnustep-extensions
Version:	0.8.5
Release:	1
License:	BSD
Vendor:		The Seawood Project
Group:		Development
Group(de):	Entwicklung
Group(es):	Desarrollo
Group(pl):	Programowanie
Group(pt_BR):	Desenvolvimento
Group(ru):	òÁÚÒÁÂÏÔËÁ
Group(uk):	òÏÚÒÏÂËÁ
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/extensions-%{version}.tar.gz
URL:		http://www.gnustep.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gnustep-make gnustep-base

%description
This package contains some classes that extend the basic behavior of
Foundation classes by adding some features. The current extensions are
an extended exception handling mechanism, a garbage collector, some
classes that allow you to easily create methods that accept
printf-like arguments and two classes for portable archiving and
unarchiving Objective-C data.

This package is built with library-combo gnu-gnu-gnu-xraw.

%description -l pl
Ten pakiet zawiera trochê klas rozszerzaj±cych podstawowe mo¿liwo¶ci
klas poprzez. Te rozszerzenia to rozszerzona obs³uga wyj±tków, garbage
collector, klasy pozwalaj±ce ³atwo tworzyæ metody akceptuj±ce
argumenty w stylu printf i dwie klasy do przeno¶nego pakowania i
rozpakowywania danych Objective-C.

%prep
%setup -q -n extensions-%{ver}

%build
if [ -z "$GNUSTEP_SYSTEM_ROOT" ]; then
   . %{_prefix}/GNUstep/Makefiles/GNUstep.sh 
fi
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix}/GNUstep --with-library-combo=gnu-gnu-gnu-xraw
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
if [ -z "$GNUSTEP_SYSTEM_ROOT" ]; then
   . %{_prefix}/GNUstep/Makefiles/GNUstep.sh 
fi
rm -rf $RPM_BUILD_ROOT
%{__make} install GNUSTEP_INSTALLATION_DIR=${RPM_BUILD_ROOT}%{_prefix}/GNUstep

cat > filelist.rpm.in << EOF
%defattr (-, root, root)
%doc COPYING ChangeLog NEWS README Version
%{_prefix}/GNUstep/Libraries/GSARCH/GSOS/gnu-gnu-gnu-xraw/lib*.so*
%{_prefix}/GNUstep/Headers/gnustep/extensions
%{_prefix}/GNUstep/Makefiles/extensions.make
EOF

sed -e "s|GSARCH|${GNUSTEP_HOST_CPU}|" -e "s|GSOS|${GNUSTEP_HOST_OS}|" < filelist.rpm.in > filelist.rpm

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f filelist.rpm
%defattr(644,root,root,755)
