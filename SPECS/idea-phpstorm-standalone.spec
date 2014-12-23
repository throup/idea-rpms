%define fullname  PhpStorm
%define vendor    jetbrains
%define shortname phpstorm

Name:          idea-phpstorm-standalone
Version:       139.732
Release:       1
Summary:       Develop with pleasure!

Group:         Development
License:       Commercial
URL:           http://confluence.jetbrains.com/display/%{fullname}/PhpStorm+Early+Access+Program
#Source0:       http://download.jetbrains.com/webide/%{fullname}-EAP-%{version}.tar.gz
Source0:       http://download.jetbrains.com/webide/PhpStorm-8.0.2.tar.gz

%description
Integrated Development Environment for PHP.

%prep
%setup -qn "%{fullname}-%{version}"

%build
cat >%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=PhpStorm
Icon=%{_datadir}/phpstorm/bin/webide.png
Exec="%{_datadir}/phpstorm/bin/%{shortname}.sh" %f
Comment=%{summary}
Categories=Development;IDE;
Terminal=false
StartupWMClass=%{vendor}-%{shortname}
EOF

# Create the wrapper for /usr/bin
cat >%{name} <<EOF
#!/bin/sh
%{_datadir}/phpstorm/bin/%{shortname}.sh $@
EOF

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/phpstorm

install -p -m0755 %{name} \
                  %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop


cp -a bin lib plugins %{buildroot}%{_datadir}/phpstorm/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/phpstorm/*
%{_datadir}/applications/%{name}.desktop



%changelog
* Thu Dec  4 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
