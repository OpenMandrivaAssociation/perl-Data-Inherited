%define upstream_name    Data-Inherited
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Hierarchy-wide accumulation of list and hash results
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


