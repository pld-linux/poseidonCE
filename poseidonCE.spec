Summary:	Poseidon Community Edition for UML
Summary(pl):	Poseidon dla UMLa
Name:		poseidonCE
Version:	2.1.1
Release:	1
License:	free/commercial (Gentleware AG)
Group:		X11/Applications
URL:		http://www.gentleware.com/products/descriptions/ce.php4
Source0:	http://download.gentleware.org/poseidonCE-2.1.1.zip
# Source0-md5:	25aa5d4df234a054bdbcf98a118028bd
Patch0:		%{name}-dirs.patch
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Community Edition is fully usable for modeling UML, and you may
use it for any purpose, commercial or not, for any duration and in any
number. It contains all UML diagrams and all implemented diagram
elements. You can create, save, and load projects, browse existing
models, exchange models, generate Java code, export your diagrams to
various formats and much more. You may freely distribute it, put it on
local or Internet servers, and distribute it on CDs or DVDs.
Gentleware does not provide support for the Community Edition.

Generally speaking, the Community Edition provides everything you need
to learn and to use UML at a non-professional level. However, there
are some restrictions. A few features are available in the commercial
editions but not in the free Community Edition.

These features are nice to have in order to increase your
productivity, but are not necessary to build UML models. Perhaps most
importantly, the Community Edition does not support reverse or
round-trip engineering, and it cannot load plug-ins. The Community
Edition also does not support printing, copy and paste to the Windows
clipboard (to copy diagrams to Word or Powerpoint for example), and
the zoom is restricted. The other Editions meet the requirements of
professional users.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},{%{_datadir},%{_examplesdir}}/%{name}}

sed -e 's#DATADIR#%{_datadir}#g' bin/poseidon.sh > $RPM_BUILD_ROOT%{_bindir}/poseidon
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}/
cp -a lib license-keys.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

ln -sf %{_defaultdocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_examplesdir}/%{name}
