# Before build RPM, install prerequsite RPMs:
yum install postgresql10-devel.x86_64 gcc openssl-devel

# Clone source and rpm package files
[root@vmxdb01 rpmbuild]# git clone git@github.com:luodonghua/pgaudit_10_rpmbuild.git

[root@vmxdb01 rpmbuild]# mv pgaudit_10_rpmbuild rpmbuild


# Refresh the pgaudit source code if needed (optional)
git clone -b REL_10_STABLE https://github.com/pgaudit/pgaudit.git

mv 1.2.0.tar.gz 1.2.0.tar.gz.orig

mv pgaudit_10-1.2.0 pgaudit_10-1.2.0.orig

mv pgaudit pgaudit_10-1.2.0

tar zcvf 1.2.0.tar.gz  pgaudit_10-1.2.0

# Build into RPM package:
rpmbuild -ba SPECS/pgaudit.spec

# Install RPM package:
rpm -ihv RPMS/x86_64/pgaudit_10-1.2.0-1.el7.centos.x86_64.rpm


# Appendix: RPM build log
[root@vmxdb01 rpmbuild]# rpmbuild -ba SPECS/pgaudit.spec

warning: bogus date in %changelog: Thu Nov 24 2017 - Luo Donghua <luodonghua@gmail.com> 1.2.0-1
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.xgcf34
+ umask 022
+ cd /root/rpmbuild/BUILD
+ cd /root/rpmbuild/BUILD
+ rm -rf pgaudit_10-1.2.0
+ /usr/bin/gzip -dc /root/rpmbuild/SOURCES/1.2.0.tar.gz
+ /usr/bin/tar -xf -
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd pgaudit_10-1.2.0
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ /usr/bin/cat /root/rpmbuild/SOURCES/pgaudit-makefile-pgxs.patch
+ /usr/bin/patch -s
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.oPqoai
+ umask 022
+ cd /root/rpmbuild/BUILD
+ cd pgaudit_10-1.2.0
+ /usr/bin/make USE_PGXS=1
gcc -Wall -Wmissing-prototypes -Wpointer-arith -Wdeclaration-after-statement -Wendif-labels -Wmissing-format-attribute -Wformat-security -fno-strict-aliasing -fwrapv -fexcess-precision=standard -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC -I. -I./ -I/usr/pgsql-10/include/server -I/usr/pgsql-10/include/internal  -D_GNU_SOURCE -I/usr/include/libxml2  -I/usr/include  -c -o pgaudit.o pgaudit.c
gcc -Wall -Wmissing-prototypes -Wpointer-arith -Wdeclaration-after-statement -Wendif-labels -Wmissing-format-attribute -Wformat-security -fno-strict-aliasing -fwrapv -fexcess-precision=standard -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC -shared -o pgaudit.so pgaudit.o  -L/usr/pgsql-10/lib -Wl,--as-needed  -L/usr/lib64 -Wl,--as-needed -Wl,-rpath,'/usr/pgsql-10/lib',--enable-new-dtags
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.KS3nmw
+ umask 022
+ cd /root/rpmbuild/BUILD
+ '[' /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64 '!=' / ']'
+ rm -rf /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64
++ dirname /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64
+ mkdir -p /root/rpmbuild/BUILDROOT
+ mkdir /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64
+ cd pgaudit_10-1.2.0
+ /usr/bin/rm -rf /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64
+ /usr/bin/make USE_PGXS=1 DESTDIR=/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64 install
/usr/bin/mkdir -p '/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/lib'
/usr/bin/mkdir -p '/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/share/extension'
/usr/bin/mkdir -p '/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/share/extension'
/usr/bin/install -c -m 755  pgaudit.so '/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/lib/pgaudit.so'
/usr/bin/install -c -m 644 .//pgaudit.control '/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/share/extension/'
/usr/bin/install -c -m 644 .//pgaudit--1.2.sql  '/root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/share/extension/'
+ install -d /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/doc/extension
+ install -m 644 README.md /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/doc/extension/README-pgaudit.md
+ /usr/bin/rm -f /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/doc/extension/README.md
+ /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /root/rpmbuild/BUILD/pgaudit_10-1.2.0
extracting debug info from /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64/usr/pgsql-10/lib/pgaudit.so
dwz: Too few files for multifile optimization
/usr/lib/rpm/sepdebugcrcfix: Updated 1 CRC32s, 0 CRC32s did match.
125 blocks
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-compress
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/redhat/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: pgaudit_10-1.2.0-1.el7.centos.x86_64
Provides: pgaudit_10 = 1.2.0-1.el7.centos pgaudit_10(x86-64) = 1.2.0-1.el7.centos
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: libc.so.6()(64bit) libc.so.6(GLIBC_2.2.5)(64bit) libc.so.6(GLIBC_2.4)(64bit) rtld(GNU_HASH)
Processing files: pgaudit_10-debuginfo-1.2.0-1.el7.centos.x86_64
Provides: pgaudit_10-debuginfo = 1.2.0-1.el7.centos pgaudit_10-debuginfo(x86-64) = 1.2.0-1.el7.centos
Requires(rpmlib): rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1 rpmlib(CompressedFileNames) <= 3.0.4-1
Checking for unpackaged file(s): /usr/lib/rpm/check-files /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64
Wrote: /root/rpmbuild/SRPMS/pgaudit_10-1.2.0-1.el7.centos.src.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/pgaudit_10-1.2.0-1.el7.centos.x86_64.rpm
Wrote: /root/rpmbuild/RPMS/x86_64/pgaudit_10-debuginfo-1.2.0-1.el7.centos.x86_64.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.h7nTTt
+ umask 022
+ cd /root/rpmbuild/BUILD
+ cd pgaudit_10-1.2.0
+ /usr/bin/rm -rf /root/rpmbuild/BUILDROOT/pgaudit_10-1.2.0-1.el7.centos.x86_64
+ exit 0
[root@vmxdb01 rpmbuild]#





