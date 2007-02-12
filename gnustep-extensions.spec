Summary:	GNUstep Foundation Extensions Library
Summary(pl.UTF-8):   Biblioteka rozszerzeń GNUstep Foundation
Name:		gnustep-extensions
Version:	0.8.6
Release:	7
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.gnustep.org/pub/gnustep/libs/extensions-%{version}.tar.gz
# Source0-md5:	7cce1455ab9319c980c204d11c481874
Patch0:		%{name}-missing.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-fs.patch
URL:		http://www.gnustep.org/
BuildRequires:	autoconf
BuildRequires:	gnustep-base-devel >= 1.9.0
Requires:	gnustep-base >= 1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
This package contains some classes that extend the basic behavior of
Foundation classes by adding some features. The current extensions are
an extended exception handling mechanism, a garbage collector, some
classes that allow you to easily create methods that accept
printf-like arguments and two classes for portable archiving and
unarchiving Objective-C data.

%description -l pl.UTF-8
Ten pakiet zawiera trochę klas rozszerzających podstawowe możliwości
klas poprzez. Te rozszerzenia to rozszerzona obsługa wyjątków, garbage
collector, klasy pozwalające łatwo tworzyć metody akceptujące
argumenty w stylu printf i dwie klasy do przenośnego pakowania i
rozpakowywania danych Objective-C.

%package devel
Summary:	Header files for GNUstep Foundation Extensions library
Summary(pl.UTF-8):   Pliki nagłówkowe dla biblioteki rozszerzeń GNUstep Foundation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnustep-base-devel >= 1.7.3

%description devel
Header files for GNUstep Foundation Extensions library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki rozszerzeń GNUstep Foundation.

%prep
%setup -q -n extensions-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
cp -f %{_prefix}/System/Library/Makefiles/config.* .
%{__autoconf}
# test for broken __builtin_apply hangs on amd64
%configure \
	ac_cv_broken_builtin_apply=no

%{__make} -j1 \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} -j1 install \
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
