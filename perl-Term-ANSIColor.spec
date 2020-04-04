%{?scl:%scl_package perl-Term-ANSIColor}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Term_ANSIColor_enables_optional_test
%else
%bcond_with perl_Term_ANSIColor_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Term-ANSIColor
Version:        4.06
Release:        452%{?dist}
Summary:        Color screen output using ANSI escape sequences
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-ANSIColor
Source0:        https://cpan.metacpan.org/modules/by-module/Term/Term-ANSIColor-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
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
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests
%if %{with perl_Term_ANSIColor_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(IPC::System::Simple)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%description
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), colorvalid(), and coloralias(), which have to be explicitly
imported to be used. 

%prep
%setup -q -n Term-ANSIColor-%{version}
chmod -c -x examples/*
%{?scl:scl enable %{scl} '}perl -MConfig -i -pe %{?scl:'"}'%{?scl:"'}s{^#!/usr/bin/perl}{$Config{startperl}}%{?scl:'"}'%{?scl:"'} examples/*%{?scl:'}

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
* Tue Mar 17 2020 Petr Pisar <ppisar@redhat.com> - 4.06-452
- Normalize shebangs in the examples (bug #1813314)

* Thu Jan 02 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-393
- Perl 5.26 rebuild

* Fri May 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-3
- Don't BR: perl(IPC::System::Simple) when bootstrapping

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.06-1
- 4.06 bump

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
