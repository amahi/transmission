Name:           amahi-transmission
Version: 0.3
Release:        1
Summary:        amahi-transmission is a package of support files for the Transmission Amahi app
Group:          System Environment/Daemons
Source:		amahi-transmission-%{version}.tar.gz
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:	transmission-daemon >= 2.80

%define debug_package %{nil}

%description
amahi-transmission is a package of support files for the Transmission Amahi app at https://www.amahi.org/apps/transmission

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/var/hda/files/torrents

install -m 0755 -D -p amahi-transmission.initscript ${RPM_BUILD_ROOT}%{_initrddir}/amahi-transmission
install -m 0644 -D -p amahi-transmission-watch.cron ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.d/amahi-transmission-watch

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
%systemd_post amahi-transmission.service

%preun
%systemd_preun_with_restart amahi-transmission.service

%files
%defattr(-,root,root,-)
%{_initrddir}/amahi-transmission
%attr(0775,transmission,users) /var/hda/files/torrents
%{_sysconfdir}/cron.d/amahi-transmission-watch

%changelog
* Sun Mar 22 2009 cpg
- add monit wtching, pid, increate requirement version
* Sun Mar 22 2009 nesl247
- add crontab file to watch for torrents
* Sun Mar 21 2009 carlos puchol
- started
