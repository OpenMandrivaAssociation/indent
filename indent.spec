Name:		indent
Version:	2.2.11
Release:	%mkrel 1
Summary:	A GNU program for formatting C code
License:	GPLv3
Group:		Development/C
URL:		http://indent.isidore-it.eu/beautify.html
Source:		http://indent.isidore-it.eu/%{name}-%{version}.tar.gz
Patch1:		indent-2.2.10.gcc-fix.patch
# https://lists.gnu.org/archive/html/bug-indent/2011-08/msg00000.html
Patch2:		indent-2.2.11-Do-not-split-decimal-float-suffix-from-constant.patch
# https://lists.gnu.org/archive/html/bug-indent/2012-02/msg00000.html
Patch3:		indent-2.2.11-Return-non-zero-exit-code-on-tests-failure.patch
BuildRequires:	texi2html

%if %{mdvver} < 201200
Requires(post):		info-install
Requires(preun):	info-install
%endif

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
%__rm -rf %{buildroot}
%makeinstall_std

# html file handled in percent-doc
%__rm -rf %{buildroot}%{_prefix}/doc

# fix message catalog name
[ -d %{buildroot}%{_datadir}/locale/zh_TW.Big5 ] && \
  %__mv %{buildroot}%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%if %{mdvver} < 201200
%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info
%endif

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS ChangeLog README doc/indent.html
%{_bindir}/indent
%{_bindir}/texinfo2man
%{_mandir}/man?/*
%{_infodir}/*.info*

