Name:          idea-rpms-release
Version:       0.0.1
Release:       1
Summary:       RPM packages for IDEs based upon Jetbrains Idea platform.

Group:         Development
License:       Commercial
URL:           https://github.com/throup/idea-rpms-repo

%description
RPM packages for IDEs based upon Jetbrains Idea platform.

%prep
cd %{name}

%build
cat >idea-rpms.repo <<EOF
[idea-rpms]
name = Idea RPMS
baseurl =https://raw.githubusercontent.com/throup/idea-rpms-repo/master/RPMS

[idea-rpms-sources]
name = Idea RPMS - sources
baseurl =https://raw.githubusercontent.com/throup/idea-rpms-repo/master/SRPMS
EOF

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cp idea-rpms.repo %{buildroot}/etc/yum.repos.d/

%files
/etc/yum.repos.d/idea-rpms.repo

%changelog
* Thu Dec  4 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
