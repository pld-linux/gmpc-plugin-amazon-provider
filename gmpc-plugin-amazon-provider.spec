%define		source_name gmpccaa
Summary:	Amazon provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):   Wtyczka udostępniająca dane z Amazona dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-amazon-provider
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	%{source_name}-%{version}.tar.gz
# Source0-md5:	f55ae657b4664d393d9058d4d06e1d2b
Patch0:		%{name}-plugins_path.patch
Patch1:		%{name}-curl.patch
URL:		http://sarine.nl/amazon-provider
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	gmpc-devel
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin fetches cover art, and album information from Amazon.

%description -l pl.UTF-8
Ta wtyczka pobiera okładkę oraz informacje o albumie z Amazona.

%prep
%setup -qn %{source_name}-%{version}
%patch0 -p1
%patch1 -p1

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
