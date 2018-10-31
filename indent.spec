%bcond_with	crosscompile

Summary:	A GNU program for formatting C code
Name:		indent
Version:	2.2.11
Release:	13
License:	GPLv2
Group:		Development/C
Url:		http://www.gnu.org/software/indent/indent.html
Source0:	ftp://ftp.gnu.org/pub/gnu/indent/%{name}-%{version}.tar.gz
Patch0:		indent-2.2.10.gcc-fix.patch
# do not use built texinfo2man if crosscompile
# use /usr/bin/texinfo2man
Patch1:		crosscompile-native-binary.patch


Patch5:		indent-2.2.9-lcall.patch
Patch7:		indent-2.2.9-man.patch
# Bug 733051, submitted to upstream
# <https://lists.gnu.org/archive/html/bug-indent/2011-08/msg00000.html>
Patch8:		indent-2.2.11-Do-not-split-decimal-float-suffix-from-constant.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2012-02/msg00000.html>
Patch9:		indent-2.2.11-Return-non-zero-exit-code-on-tests-failure.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2013-02/msg00000.html>
Patch10:	indent-2.2.11-Fix-compiler-warnings.patch
# Submitted to upstream, bug #912635
# <http://lists.gnu.org/archive/html/bug-indent/2013-02/msg00001.html>
Patch11:	indent-2.2.11-Allow-64-bit-stat.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2013-03/msg00002.html>
Patch12:	indent-2.2.11-Fix-copying-overlapping-comment.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2015-03/msg00002.html>
Patch13:	indent-2.2.11-Support-hexadecimal-floats.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2015-03/msg00003.html>
Patch14:	indent-2.2.11-Modernize-texi2html-arguments.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2015-04/msg00001.html>
Patch15:	indent-2.2.11-doc-Correct-a-typo-about-enabling-control-comment.patch
# Submitted to upstream
# <http://lists.gnu.org/archive/html/bug-indent/2015-11/msg00000.html>
Patch16:	indent-2.2.11-Fix-nbdfa-and-nbdfe-typo.patch

# gperf to update pre-generated code to fix compiler warnings
BuildRequires:	gperf
BuildRequires:	gettext
BuildRequires:	texi2html
BuildRequires:	gettext-devel
BuildRequires:	texinfo
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
%patch0 -p1
%if %{with crosscompile}
%patch1 -p1
%endif
%patch5 -p1
%patch7 -p1
%patch8 -p1 -b .float_suffix
%patch9 -p1 -b .exit_code
%patch10 -p1 -b .warnings
%patch11 -p1 -b .warnings
%patch12 -p1 -b .comments
%patch13 -p1 -b .hexa_float
%patch14 -p1 -b .texi2html5
%patch15 -p1 -b .doc_dcc
%patch16 -p1 -b .doc_nbdfa
# Regenerate sources
rm src/gperf.c src/gperf-cc.c


%build
libtoolize --copy --force
autoreconf -fiv
CFLAGS='%optflags -D_FILE_OFFSET_BITS=64' %configure
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
