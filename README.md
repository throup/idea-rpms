idea-rpms
=========

RPM packages for IDEs based upon Jetbrains Idea platform.

Fedora
------

I do not want to host the packaged RPMs at this time; partly due to the size, but mainly due to the legal implications of redistributing Jetbrains' copyrighted material.

However, I have created a Yum repository which features delta RPMs for all of the packages which may be generated from the specfiles in this Git repository. To make use of the Yum repo, follow these steps:

1) Build the RPM packages of your choosing based upon the specfiles:

```sh
$ spectool -g -R /path/to/specfile.spec
$ rpmbuild -ba /path/to/specfile.spec
```

2) Install your RPM package(s):

```sh
$ sudo yum install /path/to/package.rpm
```

3) Install the release package for the Yum repository:

```sh
$ sudo rpm -Uvh https://github.com/throup/idea-rpms-repo/blob/master/RPMS/idea-rpms-release-0.0.1-1.x86_64.rpm?raw=true
```

That should do the job. You should now receive package updates in the form of delta RPMS whenever I release an update. These deltas only contain the changes between software releases, so (a) they cannot be used without obtaining the original software from Jetbrains; and (b) they're much, much smaller!
