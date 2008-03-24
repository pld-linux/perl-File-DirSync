#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	DirSync
Summary:	File::DirSync - synchronize two directories rapidly
Summary(pl.UTF-8):	File::DirSync - szybka synchronizacja dwóch katalogów
Name:		perl-File-DirSync
Version:	1.22
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3f16a853a9fcc2b8c9e7bacc0f12709
URL:		http://search.cpan.org/dist/File-DirSync/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::DirSync will make two directories exactly the same. The goal is
to perform this syncronization process as quickly as possible with as
few stats and reads and writes as possible. It usually can perform the
syncronization process within a few milliseconds - even for gigabytes
or more of information.

%description -l pl.UTF-8
File::DirSync czyni dwa katalogi dokładnie takimi samymi. Celem jest
wykonanie tego procesu synchronizacji jak najszybciej, jak najmniejszą
liczbą operacji stat, odczytu i zapisu. Zwykle może wykonać proces
synchronizacji w ciągu kilku milisekund - nawet dla gigabajtów lub
większej ilości informacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/dirsync
%{perl_vendorlib}/File/DirSync.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
