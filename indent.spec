%bcond_with	crosscompile

Summary:	A GNU program for formatting C code
Name:		indent
Version:	2.2.13
Release:	1
License:	GPLv2
Group:		Development/C
Url:		http://www.gnu.org/software/indent/indent.html
Source0:	ftp://ftp.gnu.org/pub/gnu/indent/%{name}-%{version}.tar.gz

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
# Regenerate sources
rm src/gperf.c src/gperf-cc.c


%build
libtoolize --copy --force
autoreconf -fiv
CFLAGS='%optflags -D_FILE_OFFSET_BITS=64' %configure
%make_build

%install
%make_install

# html file handled in percent-doc
rm -rf %{buildroot}%{_prefix}/doc

# fix message catalog name
[ -d %{buildroot}%{_datadir}/locale/zh_TW.Big5 ] && \
  mv %{buildroot}%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS ChangeLog doc/indent.html
%{_bindir}/indent
%{_mandir}/man?/*
%{_infodir}/*.info*
