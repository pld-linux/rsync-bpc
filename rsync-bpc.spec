Summary:	A customized version of rsync that is used as part of BackupPC
Name:		rsync-bpc
Version:	3.0.9.12
Release:	1
License:	GPL v3+
Group:		Networking/Utilities
Source0:	https://github.com/backuppc/rsync-bpc/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9a95c7a1b9c35c4f0da221d22efd01e3
URL:		https://github.com/backuppc/rsync-bpc
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	popt-devel
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
%doc COPYING NEWS README
%attr(755,root,root) %{_bindir}/rsync_bpc

%changelog
