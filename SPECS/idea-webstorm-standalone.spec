%define fullname  WebStorm
%define vendor    jetbrains
%define shortname webstorm

Name:          idea-webstorm-standalone
Version:       139.773
Release:       2
Summary:       Develop with pleasure!

Group:         Development
License:       Commercial
URL:           http://confluence.jetbrains.com/display/%{fullname}/WebStorm+Early+Access+Program
#Source0:       http://download.jetbrains.com/webide/%{fullname}-%{version}.tar.gz
Source0:       http://download.jetbrains.com/webstorm/WebStorm-9.0.2.tar.gz
Nosource:      0

Requires:      java
Requires:      jre

%description
Integrated Development Environment for PHP.

%prep
%setup -qn "%{fullname}-%{version}"

%build
cat >%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=WebStorm
Icon=%{_datadir}/webstorm/bin/webide.png
Exec="%{_datadir}/webstorm/bin/%{shortname}.sh" %f
Comment=%{summary}
Categories=Development;IDE;
Terminal=false
StartupWMClass=%{vendor}-%{shortname}
EOF

# Create the wrapper for /usr/bin
cat >%{name} <<EOF
#!/bin/sh
%{_datadir}/webstorm/bin/%{shortname}.sh $@
EOF

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/webstorm

install -p -m0755 %{name} \
                  %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop


cp -a bin lib plugins %{buildroot}%{_datadir}/webstorm/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/webstorm/*
%{_datadir}/applications/%{name}.desktop



%changelog
* Fri Dec 12 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
