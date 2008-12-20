Summary:	A GNU program for formatting C code
Name:		indent
Version:	2.2.9
Release:	%mkrel 9
License:	GPL
Group:		Development/C
URL:		http://www.gnu.org/software/indent/indent.html
Source:		ftp://ftp.gnu.org/pub/gnu/indent/%{name}-%{version}.tar.bz2
Patch:		indent-2.2.9.gcc-fix.patch
Requires(post): info-install
Requires(preun): info-install
BuildRequires:	gettext
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Indent is a GNU program for beautifying C code, so that it is easier to read.
Indent can also convert from one C writing style to a different one. Indent
understands correct C syntax and tries to handle incorrect C syntax.

Install the indent package if you are developing applications in C and you'd
like to format your code automatically.

%prep

%setup -q
%patch -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# html file handled in percent-doc
rm -rf %{buildroot}%{_prefix}/doc

# fix message catalog name
[ -d %{buildroot}%{_datadir}/locale/zh_TW.Big5 ] && \
  mv %{buildroot}%{_datadir}/locale/zh_TW{.Big5,}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%_install_info %{name}.info
#/sbin/install-info %{_infodir}/indent.info.bz2 %{_infodir}/dir --entry="* indent: (indent).				Program to format source code."

%preun
%_remove_install_info %{name}.info
#if [ "$1" = 0 ]; then
#	/sbin/install-info --delete %{_infodir}/indent.info.bz2 %{_infodir}/dir --entry="* indent: (indent).                 	 Program to format source code."
#fi

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS ChangeLog README doc/indent.html
%{_bindir}/indent
%{_bindir}/texinfo2man
%{_mandir}/man?/*
%{_infodir}/*.info*


