Summary:	Various utilities for manipulating Type 1 and 2 font programs
Summary(pl):	R�ne narz�dzia do operowania na fontach Type 1 i 2
Name:		t1utils
Version:	1.28
Release:	1
License:	BSD
Group:		Applications/File
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
# Source0-md5:	36c65d82fa9899278c9a3bd36e5c0be7
URL:		http://www.lcdf.org/~eddietwo/type/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t1utils is a collection of simple Type 1 and 2 font manipulation
programs. Together, they allow you to convert between PFA (ASCII) and
PFB (binary) formats, disassemble PFA or PFB files into human-readable
form, reassemble them into PFA or PFB format. Additionally you can
extract font resources from a Macintosh font file (ATM/Laserwriter).

%description -l pl
t1utils jest kolekcj� prostych program�w do manipulacji na fontach
Type 1 i 2. Pozwala na konwersj� pomi�dzy PFA (ASCII) i PFB (binarny),
przekodowaniu z PFA lub PFB do "czytelnej dla cz�owieka" formy, a
nast�pnie ponowne z�o�enie do formatu PFA lub PFB. Dodatkowo mozliwe
jest wyci�gni�cie font�w z ATM/Laserwriter z Macintosh'a.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
