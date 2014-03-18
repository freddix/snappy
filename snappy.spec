Summary:	Snappy - fast compression/decompression library
Name:		snappy
Version:	1.1.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://snappy.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8887e3b7253b22a31f5486bca3cbc1c2
URL:		http://code.google.com/p/snappy/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snappy is a compression/decompression library. It does not aim for
maximum compression, or compatibility with any other compression
library; instead, it aims for very high speeds and reasonable
compression.

%package devel
Summary:	Header files for Snappy library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for Snappy library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
    --disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/snappy

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libsnappy.so.1
%attr(755,root,root) %{_libdir}/libsnappy.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsnappy.so
%{_libdir}/libsnappy.la
%{_includedir}/snappy*.h

