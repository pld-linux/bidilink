# TODO
# - checking for lynx... yes
# - checking for xmltoman... no
# - configure: WARNING: *** Not rebuilding man pages as xmltoman is not found ***
Summary:	bidilink - Bidirectional stream linker
Name:		bidilink
Version:	0.1
Release:	0.1
License:	GPL v2+
Group:		Applications/File
URL:		http://0pointer.de/lennart/projects/bidilink/
Source0:	http://0pointer.de/lennart/projects/bidilink/%{name}-%{version}.tar.gz
# Source0-md5:	f7e077061323415f73eed53da0694c4a
BuildRequires:	lynx
#BuildRequires:	xmltoman
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bidilink is a general purpose Unix tool for linking two bidirectional
data streams together. It extends the standard Unix "filter" paradigma
to bidrectional streams.

It has the following stream drivers:
- std: - STDIN, STDOUT of the process
- exec:PROGRAM - fork() off a process and use its STDIN and STDOUT
- tty:TTYDEVICE - Open a TTY device (like a serial port) as client
- pty:[PTYNAME] - Allocate a pseudo TTY device as master
- tcp-client:HOSTNAME:PORT - Connect to another or the local host via
  TCP/IP
- tcp-server:[IPADDRESS:]PORT - Listen on a local port and wait for an
  incoming connection
- unix-client:SOCKNAME - Connect to a local Unix domain socket
- unix-server:SOCKNAME - Listen on a local Unix domain socket

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
%doc README
%attr(755,root,root) %{_bindir}/bidilink
%{_mandir}/man1/bidilink.1*
