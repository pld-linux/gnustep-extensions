Summary:	GNUstep Foundation Extensions Library
Summary(pl):	Biblioteka rozszerzeñ GNUstep Foundation
Name:		gnustep-extensions
Version:	0.8.6
Release:	4
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/extensions-%{version}.tar.gz
# Source0-md5:	7cce1455ab9319c980c204d11c481874
Patch0:		%{name}-missing.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-fs.patch
URL:		http://www.gnustep.org/
BuildRequires:	autoconf
BuildRequires:	gnustep-base-devel >= 1.7.3
Requires:	gnustep-base >= 1.7.3
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
Requires:	gnustep-base-devel >= 1.7.3

%description devel
Header files for GNUstep Foundation Extensions library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki rozszerzeñ GNUstep Foundation.

%prep
%setup -q -n extensions-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
cp -f %{_prefix}/System/Library/Makefiles/config.* .
%{__autoconf}
%configure

%{__make} \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_prefix}/System/Library/Headers/%{libcombo}/gnustep/extensions
%{_prefix}/System/Library/Headers/%{libcombo}/gnustep/objc
%{_prefix}/System/Library/Libraries/%{gscpu}/%{gsos}/%{libcombo}/lib*.so
%{_prefix}/System/Library/Makefiles/extensions.make
