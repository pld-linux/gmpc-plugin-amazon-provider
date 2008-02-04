%define		source_name gmpc-coveramazon
Summary:	Amazon provider plugin for Gnome Music Player Client
Summary(pl.UTF-8):	Wtyczka udostępniająca dane z Amazona dla odtwarzacza Gnome Music Player Client
Name:		gmpc-plugin-amazon-provider
Version:	0.15.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
# http://sarine.nl/gmpc-plugins-downloads
Source0:	%{source_name}-%{version}.tar.gz
# Source0-md5:	9471fe2ec7ae5ff04c855ef95c1744fc
Patch0:		%{name}-plugins_path.patch
URL:		http://www.sarine.nl//amazon-provider
BuildRequires:	gmpc-devel >= 0.15.5.0
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	libglade2-devel
BuildRequires:	libmpd >= 0.15.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin fetches cover art, and album information from Amazon.

%description -l pl.UTF-8
Ta wtyczka pobiera okładkę oraz informacje o albumie z Amazona.

%prep
%setup -qn %{source_name}-%{version}
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
