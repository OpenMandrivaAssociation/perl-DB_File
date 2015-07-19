%define upstream_name	 DB_File
%define upstream_version 1.834

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl5 access to Berkeley DB version 1.x

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{upstream_name}-1.831-makefile.patch

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
perl Makefile.PL INSTALLDIRS=vendor
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
