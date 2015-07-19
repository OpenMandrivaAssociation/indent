%bcond_with	crosscompile

Summary:	A GNU program for formatting C code
Name:		indent
Version:	2.2.11
Release:	12
License:	GPLv2
Group:		Development/C
Url:		http://www.gnu.org/software/indent/indent.html
Source0:	ftp://ftp.gnu.org/pub/gnu/indent/%{name}-%{version}.tar.gz
Patch1:		indent-2.2.10.gcc-fix.patch
# https://lists.gnu.org/archive/html/bug-indent/2011-08/msg00000.html
Patch2:		indent-2.2.11-Do-not-split-decimal-float-suffix-from-constant.patch
# https://lists.gnu.org/archive/html/bug-indent/2012-02/msg00000.html
Patch3:		indent-2.2.11-Return-non-zero-exit-code-on-tests-failure.patch
# do not use built texinfo2man if crosscompile
# use /usr/bin/texinfo2man
Patch4:		crosscompile-native-binary.patch

BuildRequires:	gettext
BuildRequires:	texi2html
BuildRequires:	gettext-devel
%if %{with crosscompile}
BuildRequires:	indent
%endif

%description
Indent is a GNU program for beautifying C code, so that it is easier to read.
Indent can also convert from one C writing style to a different one. Indent
understands correct C syntax and tries to handle incorrect C syntax.

Install the indent package if you are developing applications in C and you'd
like to format your code automatically.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if %{with crosscompile}
%patch4 -p1
%endif


%build
export CC=gcc
libtoolize --copy --force
autoreconf -fiv
%configure
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
%doc AUTHORS COPYING NEWS ChangeLog README doc/indent.html
%{_bindir}/indent
%{_bindir}/texinfo2man
%{_mandir}/man?/*
%{_infodir}/*.info*
