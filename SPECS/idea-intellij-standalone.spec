%define vendor    jetbrains
%define fullname  IntelliJ Idea
%define shortname idea
%define buildname intellij-community-%{shortname}

%global __python %{__python3}

Name:          idea-intellij-standalone
Version:       139.658
Release:       1
Summary:       IntelliJ Java IDE

Group:         Development
License:       Apache License
URL:           https://github.com/JetBrains/intellij-community/tree/%{shortname}/%{version}
Source0:       https://github.com/JetBrains/intellij-community/archive/%{shortname}/%{version}.tar.gz
%define suppl1 throup-idea-android-1625a52a183a
#Source1:         https://bitbucket.org/throup/idea-android/get/master.tar.gz#/%{suppl1}.tar.gz
Source1:       https://bitbucket.org/throup/idea-android/get/idea/%{version}.tar.gz#/%{suppl1}.tar.gz
%define suppl2 throup-idea-adt-tools-base-381a533c8845
#Source2:       https://bitbucket.org/throup/idea-adt-tools-base/get/master.tar.gz#/%{suppl2}.tar.gz
Source2:       https://bitbucket.org/throup/idea-adt-tools-base/get/idea/%{version}.tar.gz#/%{suppl2}.tar.gz

BuildRequires: ant

%description
IntelliJ Java IDE based upon the Jetbrains Idea platform.

%prep
%setup -qn "%{buildname}-%{version}"
echo %{version} > build.txt
%setup -T -D -a 1 -n "%{buildname}-%{version}"
mv %{suppl1} android
%setup -T -D -a 2 -n "%{buildname}-%{version}"
mv %{suppl2} android/tools-base

%build
ant
ant -f python/build.xml -Didea.path=`pwd`/out/artifacts/ -Didea.build.number=%{version} plugin

cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{fullname}
GenericName=%{fullname}
Comment=Starts %{fullname}
Exec="%{_datadir}/%{shortname}/bin/%{shortname}.sh" %f
Icon=%{_datadir}/%{shortname}/bin/%{shortname}.png
Terminal=false
Type=Application
Categories=GTK;GNOME;Development;
StartupWMClass=%{vendor}-%{shortname}-ce
EOF

# Create the wrapper for /usr/bin
cat >%{name} <<EOF
#!/bin/sh
%{_datadir}/%{shortname}/bin/%{shortname}.sh $@
EOF

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/%{shortname}

rm out/dist.unix.ce/bin/fsnotifier

cp -a out/dist.all.ce/* \
      %{buildroot}%{_datadir}/%{shortname}/
cp -a out/dist.unix.ce/* \
      %{buildroot}%{_datadir}/%{shortname}/

cp -a python/distCE/zip/python \
      %{buildroot}%{_datadir}/%{shortname}/plugins/


#install -p -m0755 out/dist.unix.ce/bin/fsnotifier \
#                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/dist.unix.ce/bin/fsnotifier64 \
                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/dist.unix.ce/bin/idea.sh \
                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/dist.unix.ce/bin/inspect.sh \
                  %{buildroot}%{_datadir}/%{shortname}/bin/


install -p -m0755 %{name} \
                  %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc %{_datadir}/%{shortname}/license
%doc %{_datadir}/%{shortname}/NOTICE.txt
%doc %{_datadir}/%{shortname}/build.txt
%doc %{_datadir}/%{shortname}/Install-Linux-tar.txt
%{_datadir}/%{shortname}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Dec  6 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
