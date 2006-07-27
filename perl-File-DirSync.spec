#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	DirSync
Summary:	File::DirSync - synchronize two directories rapidly
Summary(pl):	File::DirSync - szybka synchronizacja dwóch katalogów
Name:		perl-File-DirSync
Version:	1.14
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8e3ff17f612bd058f24d967f2d55c430
Patch0:		%{name}
URL:		http://search.cpan.org/dist/File-DirSync
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

%description -l pl
File::DirSync czyni dwa katalogi dok³adnie takimi samymi. Celem jest
wykonanie tego procesu synchronizacji jak najszybciej, jak najmniejsz±
liczb± operacji stat, odczytu i zapisu. Zwykle mo¿e wykonaæ proces
synchronizacji w ci±gu kilku milisekund - nawet dla gigabajtów lub
wiêkszej ilo¶ci informacji.

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
