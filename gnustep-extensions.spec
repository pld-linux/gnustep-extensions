Summary:	GNUstep Foundation Extensions Library
Summary(pl):	Biblioteka rozszerzeñ GNUstep Foundation
Name:		gnustep-extensions
Version:	0.8.6
Release:	1
License:	BSD-like
Vendor:		The GNUstep Project
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/extensions-%{version}.tar.gz
URL:		http://www.gnustep.org/
BuildRequires:	autoconf
BuildRequires:	gnustep-base-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/lib/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif

%description
This package contains some classes that extend the basic behavior of
Foundation classes by adding some features. The current extensions are
an extended exception handling mechanism, a garbage collector, some
classes that allow you to easily create methods that accept
printf-like arguments and two classes for portable archiving and
unarchiving Objective-C data.

%description -l pl
Ten pakiet zawiera trochê klas rozszerzaj±cych podstawowe mo¿liwo¶ci
klas poprzez. Te rozszerzenia to rozszerzona obs³uga wyj±tków, garbage
collector, klasy pozwalaj±ce ³atwo tworzyæ metody akceptuj±ce
argumenty w stylu printf i dwie klasy do przeno¶nego pakowania i
rozpakowywania danych Objective-C.

%package devel
Summary:	Header files for GNUstep Foundation Extensions library
Summary(pl):	Pliki nag³ówkowe dla biblioteki rozszerzeñ GNUstep Foundation
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gnustep-base-devel

%description devel
Header files for GNUstep Foundation Extensions library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki rozszerzeñ GNUstep Foundation.

%prep
%setup -q -n extensions-%{version}

%build
. %{_prefix}/System/Makefiles/GNUstep.sh
cp -f %{_prefix}/System/Makefiles/config.* .
%{__autoconf}
%configure

%{__make} \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_prefix}/System/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Headers/gnustep/extensions
%{_prefix}/System/Headers/gnustep/objc
%{_prefix}/System/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
%{_prefix}/System/Makefiles/extensions.make
