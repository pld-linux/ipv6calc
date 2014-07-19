#
# Conditional build:
%bcond_without	geoip		# GeoIP support
%bcond_with	ip2location	# IP2Location support
#
Summary:	IPv6 address format change and calculation utility
Summary(pl.UTF-8):	Narzędzie do zmiany formatu i przeliczania adresów IPv6
Name:		ipv6calc
Version:	0.97.3
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://ftp.bieringer.de/pub/linux/IPv6/ipv6calc/%{name}-%{version}.tar.gz
# Source0-md5:	1fc9c1a14802638f21e59408faa721a6
URL:		http://www.deepspace6.net/projects/ipv6calc.html
%{?with_geoip:BuildRequires:	GeoIP-devel >= 1.4.1}
%{?with_ip2location:BuildRequires:	ip2location-c-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipv6calc is a small utility which formats and calculates IPv6
addresses in different ways.

Install this package, if you want to extend the existing address
detection on IPv6 initscript setup or make life easier in adding
reverse IPv6 zones to DNS or using in DNS queries like nslookup -q=ANY
`ipv6calc -r 3ffe:400:100:f101::1/48` See also here for more details:
<http://www.bieringer.de/linux/IPv6/ipv6calc/>.

%description -l pl.UTF-8
ipv6calc to niewielkie narzędzie formatujące i przeliczające adresy
IPv6 na różne sposoby. Ułatwia życie przy dodawaniu stref odwrotnych
IPv6 do DNS lub odpytywaniu w rodzaju nslookup -q=ANY `ipv6calc -r
3ffe:400:100:f101::1/48`. Więcej szczegółów pod adresem
<http://www.bieringer.de/linux/IPv6/ipv6calc/>.

%prep
%setup -q

%build
%configure \
	%{?with_geoip:--enable-geoip} \
	%{?with_ip2location:--enable-ip2location --with-ip2location-dyn-lib=libIP2Location.so.1}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README CREDITS TODO doc/ipv6calc.html ipv6calcweb/ipv6calcweb.cgi
%attr(755,root,root) %{_bindir}/ipv6calc
%attr(755,root,root) %{_bindir}/ipv6loganon
%attr(755,root,root) %{_bindir}/ipv6logconv
%attr(755,root,root) %{_bindir}/ipv6logstats
%{_mandir}/man8/ipv6calc.8*
%{_mandir}/man8/ipv6loganon.8*
%{_mandir}/man8/ipv6logconv.8*
%{_mandir}/man8/ipv6logstats.8*
