#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	SMTP-TLS-ButMaintained
%include	/usr/lib/rpm/macros.perl
Summary:	Net::SMTP::TLS::ButMaintained - An SMTP client supporting TLS and AUTH
Name:		perl-Net-SMTP-TLS-ButMaintained
Version:	0.20
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c23283a44d355bab1d70722a43cf27eb
URL:		http://search.cpan.org/dist/Net-SMTP-TLS-ButMaintained/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-IO-Socket-SSL >= 1.76
BuildRequires:	perl-Net-SSLeay
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::SMTP::TLS::ButMaintained is forked from Net::SMTP::TLS. blame
Evan Carroll for the idea. :)

Net::SMTP::TLS::ButMaintained is a TLS and AUTH capable SMTP client
which offers an interface that users will find familiar from
Net::SMTP. Net::SMTP::TLS::ButMaintained implements a subset of the
methods provided by that module, but certainly not (yet) a complete
mirror image of that API.

The methods supported by Net::SMTP::TLS::ButMaintained are used in the
above example. Though self explanatory for the most part, please see
the perldoc for Net::SMTP if you are unclear.

The differences in the methods provided are as follows:

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
%dir %{perl_vendorlib}/Net/SMTP/TLS
%{perl_vendorlib}/Net/SMTP/TLS/*.pm
%{_mandir}/man3/*
