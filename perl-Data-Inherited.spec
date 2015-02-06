%define upstream_name    Data-Inherited
%define upstream_version 1.100860

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Hierarchy-wide accumulation of list and hash results
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
NEXT.pm adds a pseudoclass named 'NEXT' to any program that uses it. If a
method 'm' calls '$self-'NEXT::m()>, the call to 'm' is redispatched as if
the calling method had not originally been found.

In other words, a call to '$self-'NEXT::m()> resumes the depth-first,
left-to-right search of '$self''s class hierarchy that resulted in the
original call to 'm'.

Note that this is not the same thing as '$self-'SUPER::m()>, which begins a
new dispatch that is restricted to searching the ancestors of the current
class. '$self-'NEXT::m()> can backtrack past the current class -- to look
for a suitable method in other ancestors of '$self' -- whereas
'$self-'SUPER::m()> cannot.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.860-2mdv2011.0
+ Revision: 654907
- rebuild for updated spec-helper

* Sun Mar 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.860-1mdv2011.0
+ Revision: 528430
- update to 1.100860

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.850-1mdv2010.1
+ Revision: 527731
- update to 1.100850

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.1
+ Revision: 503863
- update to 1.07

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 444081
- import perl-Data-Inherited


* Thu Sep 17 2009 cpan2dist 1.06-1mdv
- initial mdv release, generated with cpan2dist
