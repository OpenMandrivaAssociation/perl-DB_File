%define module	DB_File
%define name	perl-%{module}
%define version	1.818
%define release	%mkrel 1

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	Perl5 access to Berkeley DB version 1.x
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{module}-%{version}.tar.bz2
Patch:		%{module}-1.805-makefile.patch
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	db-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}
%patch -p1
chmod 644 README DB_File.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/DB_File
%_mandir/man3*/DB_File.*


