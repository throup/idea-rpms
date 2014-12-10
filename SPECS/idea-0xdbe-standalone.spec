%define vendor    jetbrains
%define fullname  0xDBE
%define shortname 0xdbe

Name:          idea-%{shortname}-standalone
Version:       138.2222.2
Release:       3
Summary:       Develop with pleasure!

Group:         Development
License:       Commercial
URL:           http://confluence.jetbrains.com/display/DBE/0xDBE+1.0+EAP
Source0:       http://download.jetbrains.com/dbe/%{shortname}-%{version}.tar.gz

Requires:      java


%description
Integrated Development Environment for DBs.

%prep
%setup -qn "%{fullname}-%{version}"

%build
cat >%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%{fullname}
Icon=%{_datadir}/idea/bin/%{shortname}.png
#Exec="%{_bindir}/%{name}" %f
Exec="%{_datadir}/idea/bin/%{shortname}.sh" %f
Comment=%{summary}
Categories=Development;IDE;
Terminal=false
StartupWMClass=%{vendor}-%{shortname}
EOF

# Create the wrapper for /usr/bin
cat >%{name} <<EOF
#!/bin/sh
%{_datadir}/%{vendor}/%{shortname}/bin/%{shortname}.sh $@
EOF

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/%{vendor}/%{shortname}
install -p -m0755 %{name} \
                  %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop

cp -a bin lib %{buildroot}%{_datadir}/%{vendor}/%{shortname}/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc help/* license/*
%{_bindir}/%{name}
%{_datadir}/%{vendor}/%{shortname}/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Dec  4 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
