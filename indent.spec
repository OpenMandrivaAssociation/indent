Summary:	A GNU program for formatting C code
Name:		indent
Version:	2.2.11
Release:	2
License:	GPL
Group:		Development/C
URL:		http://www.gnu.org/software/indent/indent.html
Source:		ftp://ftp.gnu.org/pub/gnu/indent/%{name}-%{version}.tar.gz
Patch1: indent-2.2.10.gcc-fix.patch
# https://lists.gnu.org/archive/html/bug-indent/2011-08/msg00000.html
Patch2: indent-2.2.11-Do-not-split-decimal-float-suffix-from-constant.patch
# https://lists.gnu.org/archive/html/bug-indent/2012-02/msg00000.html
Patch3: indent-2.2.11-Return-non-zero-exit-code-on-tests-failure.patch
BuildRequires: texi2html
BuildRequires: gettext

%description
Indent is a GNU program for beautifying C code, so that it is easier to read.
Indent can also convert from one C writing style to a different one. Indent
understands correct C syntax and tries to handle incorrect C syntax.

Install the indent package if you are developing applications in C and you'd
like to format your code automatically.

%prep

%setup -q
%patch1 -p0
%patch2 -p1 -b .float-suffix
%patch3 -p1 -b .exit-code

%build
%configure2_5x
%make

%install
%makeinstall_std

# html file handled in percent-doc
rm -rf %{buildroot}%{_prefix}/doc

# fix message catalog name
[ -d %{buildroot}%{_datadir}/locale/zh_TW.Big5 ] && \
  mv %{buildroot}%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS ChangeLog README doc/indent.html
%{_bindir}/indent
%{_bindir}/texinfo2man
%{_mandir}/man?/*
%{_infodir}/*.info*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.10-5mdv2011.0
+ Revision: 665509
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.10-4mdv2011.0
+ Revision: 605974
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.10-3mdv2010.1
+ Revision: 520127
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.2.10-2mdv2010.0
+ Revision: 425335
- rebuild

* Tue Mar 17 2009 Erwan Velu <erwan@mandriva.org> 2.2.10-1mdv2009.1
+ Revision: 356947
- 2.2.10

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.9-9mdv2009.1
+ Revision: 316780
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.2.9-8mdv2009.0
+ Revision: 221630
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.2.9-7mdv2008.1
+ Revision: 127056
- kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.9-7mdv2007.1
+ Revision: 145451
- Import indent

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.9-7mdv2007.1
- bunzip patches

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.2.9-6mdk
- Rebuild

* Fri Jul 01 2005 Michael Scherer <misc@mandriva.org> 2.2.9-5mdk
- fix prereq
- fix url ( #16655, thanks to juke )
- mkrel
- fix compilation

* Fri May 28 2004 Abel Cheung <deaddog@deaddog.org> 2.2.9-4mdk
- More macros
- BuildRequires
- Various other tuning

