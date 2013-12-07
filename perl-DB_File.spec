%define upstream_name	 DB_File
%define upstream_version 1.826

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl5 access to Berkeley DB version 1.x
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{upstream_name}-1.805-makefile.patch

BuildRequires:	db-devel
BuildRequires:	perl-devel

%description
DB_File is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 1. (DB_File can be built with
version 2 or 3 of Berkeley DB, but it will only support the 1.x
features).

If you want to make use of the new features available in Berkeley DB
2.x or 3.x, use the Perl module BerkeleyDB instead.

Berkeley DB is a C library which provides a consistent interface to a
number of database formats. DB_File provides an interface to all three
of the database types (hash, btree and recno) currently supported by
Berkeley DB.

For further details see the documentation included at the end of the
file DB_File.pm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
chmod 644 README DB_File.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

rm %{buildroot}%{_mandir}/man3/DB_File.3pm

%files
%doc README Changes
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/DB_File


%changelog
* Sun May 13 2012 Crispin Boylan <crisb@mandriva.org> 1.826.0-1
+ Revision: 798653
- New release

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.820.0-10
+ Revision: 765164
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.820.0-9
+ Revision: 763693
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.820.0-8
+ Revision: 667069
- mass rebuild

* Wed Mar 30 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.820.0-7
+ Revision: 649269
- clean out obsolete/deprecated/redundant stuff in relation to db 5.1.25 rebuild

* Wed Dec 29 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.820.0-6mdv2011.0
+ Revision: 625750
- fix conflicting man pages

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.820.0-5mdv2011.0
+ Revision: 564426
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.820.0-4mdv2011.0
+ Revision: 555230
- rebuild

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.820.0-3mdv2010.1
+ Revision: 505725
- rebuild using %%perl_convert_version

* Wed Dec 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1.820-2mdv2010.1
+ Revision: 483976
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.820-1mdv2010.0
+ Revision: 371602
- update to new version 1.820

* Thu Feb 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.819-1mdv2009.1
+ Revision: 342830
- update to new version 1.819

* Sun Feb 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.818-1mdv2009.1
+ Revision: 336236
- update to new version 1.818

* Mon Dec 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.817-3mdv2009.1
+ Revision: 314520
- rebuilt against db4.7

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.817-2mdv2009.0
+ Revision: 265355
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.817-1mdv2009.0
+ Revision: 193798
- update to new version 1.817

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.816-3mdv2008.1
+ Revision: 151327
- rebuild for perl-5.10.0

* Sun Dec 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.816-2mdv2008.1
+ Revision: 137309
- rebuilt against bdb 4.6.x

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.816-1mdv2008.1
+ Revision: 105481
- new version
- update to new version 1.816

