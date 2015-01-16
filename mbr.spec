Summary:	Master Boot Record for IBM-PC compatible computers
Name:		mbr
Version:	1.1.11
Release:	1
License:	GPL
Group:		Base
Source0:	http://www.chiark.greenend.org.uk/~neilt/mbr/%{name}-%{version}.tar.gz
# Source0-md5:	4e406ded185f94c2d2bf5fc793ac1842
URL:		http://www.chiark.greenend.org.uk/~neilt/mbr/
BuildRequires:	bin86
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Master Boot Record for IBM-PC compatible computers.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/install-mbr
%{_mandir}/man8/install-mbr.8*
