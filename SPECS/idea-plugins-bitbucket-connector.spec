%define fork      dmitry_cherkas
%define shortname bitbucket-connector
%define codename  jetbrains-%{shortname}
%define commit    9099a4aec49f
%define checkout  20141127hg%{commit}

Name:          idea-plugins-%{shortname}
Version:       1.2.3.SNAPSHOT+%{checkout}
Release:       1
Summary:       Develop with pleasure!

Group:         Development
License:       Commercial
URL:           https://bitbucket.org/%{fork}/%{codename}
Source0:       https://bitbucket.org/%{fork}/%{codename}/get/%{commit}.tar.bz2#/%{fork}-%{codename}-%{commit}.tar.bz2
Requires:      java
BuildRequires: ant
BuildArch:     noarch

%description
Bitbucket plugin for Jetbrains integrated development environments

%prep
%setup -qn "%{fork}-%{codename}-%{commit}"

%build
ant -Didea.dir=/usr/share/idea

%install
mkdir -p %{buildroot}%{_datadir}/idea/plugins/

cp -a build/Bitbucket \
      %{buildroot}%{_datadir}/idea/plugins/

%files
%{_datadir}/idea/plugins/Bitbucket/*

%changelog
* Sun Dec  7 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
