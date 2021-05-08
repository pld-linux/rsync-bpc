# Conditional build:
%bcond_with	tests	# perform "make test"
#
Summary:	A customized version of rsync that is used as part of BackupPC
Name:		rsync-bpc
Version:	3.1.3.0
Release:	1
License:	GPL v3+
Group:		Networking/Utilities
Source0:	https://github.com/backuppc/rsync-bpc/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5c2ee55dc1683c9737982e51a404026
URL:		https://github.com/backuppc/rsync-bpc
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.318
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rsync-bpc is a customized version of rsync that is used as part of
BackupPC, an open source backup system.

The main change to rsync is adding a shim layer (in the subdirectory
backuppc, and in bpc_sysCalls.c) that emulates the system calls for
accessing the file system so that rsync can directly read/write files
in BackupPC's format.

Rsync-bpc is fully line-compatible with vanilla rsync, so it can talk
to rsync servers and clients.

Rsync-bpc serves no purpose outside of BackupPC.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure \
	LIBS="-lcrypto" \
	%{?with_rsh:--with-rsh=rsh} \
	--enable-ipv6 \
	--enable-acl-support \
	--enable-xattr-support \
	--disable-debug
%{__make} proto
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_bindir}/rsync_bpc

%changelog
