Summary:	IPv6 address format change and calculation utility
Summary(pl):	Narz�dzie do zmiany formatu i przeliczania adres�w IPv6
Name:		ipv6calc
Version:	0.28
Release:	2
License:	GPL
Group:		Networking/Utilities
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
http://www.bieringer.de/linux/IPv6/ .

%description -l pl
ipv6calc to niewielkie narz�dzie formatuj�ce i przeliczaj�ce adresy
IPv6 na r�ne sposoby. U�atwia �ycie przy dodawaniu stref odwrotnych
IPv6 do DNS lub odpytywaniu w rodzaju nslookup -q=ANY `ipv6calc -r
3ffe:400:100:f101::1/48`. Wi�cej szczeg��w pod adresem
http://www.bieringer.de/linux/IPv6/ .

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install ipv6calc $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README TODO ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ipv6calc
