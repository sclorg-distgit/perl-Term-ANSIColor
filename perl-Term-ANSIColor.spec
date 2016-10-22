%{?scl:%scl_package perl-Term-ANSIColor}

Name:           %{?scl_prefix}perl-Term-ANSIColor
Version:        4.05
Release:        3%{?dist}
Summary:        Color screen output using ANSI escape sequences
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Term-ANSIColor/
Source0:        http://www.cpan.org/modules/by-module/Term/Term-ANSIColor-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
# Tests
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), colorvalid(), and coloralias(), which have to be explicitly
imported to be used. 

%prep
%setup -q -n Term-ANSIColor-%{version}
chmod -c -x examples/*

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 4.05-3
- SCL

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-2
- Perl 5.24 rebuild

* Fri Apr 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.05-1
- 4.05 bump

* Fri Mar 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.04-1
- 4.04 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.03-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.03-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.03-345
- Increase release to favour standalone package

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.03-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.03-3
- Perl 5.20 rebuild

* Mon Aug 11 2014 David Dick <ddick@cpan.org> - 4.03-2
- Re-adding for master

* Tue Jul 22 2014 David Dick <ddick@cpan.org> - 4.03-1
- Initial release
