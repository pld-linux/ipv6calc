Summary:	IPv6 address format change and calculation utility
Summary(pl):	Narzêdzie do zmiany formatu i przeliczania adresów IPv6
Name:		ipv6calc
Version:	0.45
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.deepspace6.net/pub/ds6/sources/ipv6calc/%{name}-%{version}.tar.gz
# Source0-md5:	6ce6a797fe95a9480fb2e8b09171e7fb
URL:		http://www.deepspace6.net/projects/ipv6calc.html
Buildrequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipv6calc is a small utility which formats and calculates IPv6
addresses in different ways.

Install this package, if you want to extend the existing address
detection on IPv6 initscript setup or make life easier in adding
reverse IPv6 zones to DNS or using in DNS queries like nslookup -q=ANY
`ipv6calc -r 3ffe:400:100:f101::1/48` See also here for more details:
http://www.bieringer.de/linux/IPv6/ipv6calc/ .

%description -l pl
ipv6calc to niewielkie narzêdzie formatuj±ce i przeliczaj±ce adresy
IPv6 na ró¿ne sposoby. U³atwia ¿ycie przy dodawaniu stref odwrotnych
IPv6 do DNS lub odpytywaniu w rodzaju nslookup -q=ANY `ipv6calc -r
3ffe:400:100:f101::1/48`. Wiêcej szczegó³ów pod adresem
http://www.bieringer.de/linux/IPv6/ipv6calc/ .

%prep
%setup -q

%build
./configure
%{__make} CFLAGS="%{rpmcflags} -I../getopt/ -I../ -I../lib/"
cd ipv6calcweb
perl -pi -m: -e "s:../ipv6calc/ipv6calc:%{_bindir}/ipv6calc:" ipv6calcweb.cgi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ipv6calc/ipv6calc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README CREDITS TODO LICENSE ipv6calcweb/ipv6calcweb.cgi
%attr(755,root,root) %{_bindir}/ipv6calc
