Summary:	Voltaire Infiniband Fabric Simulator
Summary(pl.UTF-8):	Symulator materiału Infiniband Voltaire
Name:		ibsim
Version:	0.7
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
# Source0-md5:	7ff8756f222799d042f7309777cc711d
URL:		http://www.openfabrics.org/
BuildRequires:	libibmad-devel
BuildRequires:	libibumad-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ibsim emulates the fabric behavior by using MAD communication with the
SM/SA and the PerfMgr. This simple tool is ideally suitable for
various research, development, debug and testing tasks where IB subnet
management is involved.

%description -l pl.UTF-8
ibsim emuluje zachowanie materiału poprzez wykorzystanie komunikacji
MAD wraz z SM/SA oraz PerfMgr. To proste narzędzie nadaje się idealnie
do różnych badań, rozwijania oprogramowania, zadań diagnostycznych i
testowych związanych z zarządzaniem podsieciami IB.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}" \
	prefix=%{_prefix} \
	libpath=%{_libdir} \
	binpath=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT

# NOTE: flags are needed here to avoid recompilation
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libpath=%{_libdir} \
	binpath=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/ibsim
%dir %{_libdir}/umad2sim
%attr(755,root,root) %{_libdir}/umad2sim/libumad2sim.so
