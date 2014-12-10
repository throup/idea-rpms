Name:          idea-rpms-release
Version:       0.0.2
Release:       1
Summary:       RPM packages for IDEs based upon Jetbrains Idea platform.
Source0:       RPM-GPG-KEY-idea-rpms

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
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-idea-rpms
enabled=1

[idea-rpms-sources]
name = Idea RPMS - sources
baseurl =https://raw.githubusercontent.com/throup/idea-rpms-repo/master/SRPMS
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-idea-rpms
enabled=1
EOF

%install
mkdir -p %{buildroot}/etc/yum.repos.d
cp idea-rpms.repo %{buildroot}/etc/yum.repos.d/

mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cp -p %SOURCE0 %{buildroot}/etc/pki/rpm-gpg/

%files
/etc/yum.repos.d/idea-rpms.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-idea-rpms

%changelog
* Wed Dec 10 2014 Chris Throup <chris@throup.org.uk>
- Add GPG key
* Thu Dec  4 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
