%define		source_name gmpc-coveramazon
Summary:	Amazon provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca dane z Amazona dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-amazon-provider
Version:	0.15.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/gmpc-0.15.5/%{source_name}-%{version}.tar.gz
# Source0-md5:	9471fe2ec7ae5ff04c855ef95c1744fc
Patch0:		%{name}-plugins_path.patch
URL:		http://www.sarine.nl/amazon-provider
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gmpc-devel >= 0.15.5.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin fetches cover art, and album information from Amazon.

%description -l pl.UTF-8
Ta wtyczka pobiera okładkę oraz informacje o albumie z Amazona.

%prep
%setup -q -n %{source_name}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gmpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gmpc/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/*.so
