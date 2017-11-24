%global pgmajorversion 10
%global pginstdir /usr/pgsql-10
%global sname   pgaudit

Summary:        PostgreSQL Audit Extension
Name:           %{sname}_%{pgmajorversion}
Version:        1.2.0
Release:        1%{?dist}
License:        BSD
Group:          Applications/Databases
Source0:        https://github.com/%{sname}/%{sname}/archive/%{version}.tar.gz
Patch0:         %{sname}-makefile-pgxs.patch
URL:            http://pgaudit.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.

%prep
%autosetup


%build
%{__make} USE_PGXS=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make}  USE_PGXS=1 %{?_smp_mflags} DESTDIR=%{buildroot} install
# Install README and howto file under PostgreSQL installation directory:
install -d %{buildroot}%{pginstdir}/doc/extension
install -m 644 README.md %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.md
%{__rm} -f %{buildroot}%{pginstdir}/doc/extension/README.md

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{pginstdir}/doc/extension/README-%{sname}.md
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}--1.2.sql
%{pginstdir}/share/extension/%{sname}.control

%changelog
* Thu Nov 24 2017 - Luo Donghua <luodonghua@gmail.com> 1.2.0-1
- Update to 1.2.0 to support postgresql 10

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository
