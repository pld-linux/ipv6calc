Summary:	IPv6 address format change and calculation utility
Name:		ipv6calc
Version:	0.28
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz
URL:		ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipv6calc is a small utility which formats and calculates IPv6
addresses in different ways.

Install this package, if you want to extend the existing address
detection on IPv6 initscript setup or make life easier in adding
reverse IPv6 zones to DNS or using in DNS queries like nslookup -q=ANY
`ipv6calc -r 3ffe:400:100:f101::1/48` See also here for more details:
http://www.bieringer.de/linux/IPv6/

%prep
%setup -q
%build
%{__make} CFLAGS="%{rpmcflags}"
	
%install
rm -rf $RPM_BUILD_ROOT
install -d		$RPM_BUILD_ROOT%{_bindir}

install ipv6calc	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ipv6calc
