Summary:	Poseidon Community Edition for UML
Summary(pl):	Poseidon dla UML-a w wersji Community Edition
Name:		poseidonCE
Version:	2.3.1
Release:	1
License:	free/commercial (Gentleware AG)
Group:		X11/Applications
#Source0Download: http://www.gentleware.com/products/download.php4
Source0:	ftp://download.gentleware.biz/%{name}-%{version}.zip
# Source0-md5:	2944feeb94b8452393993855753327ee
URL:		http://www.gentleware.com/products/descriptions/ce.php4
Patch0:		%{name}-dirs.patch
BuildRequires:	unzip
Requires:	jre >= 1.4
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

%description -l pl
Wersja Community Edition jest w pe³ni u¿yteczna do modelowania UML i
mo¿e byæ u¿ywana w dowolnych zastosowaniach, komercyjnych lub nie,
przez dowolny okres i dowolnie du¿o. Zawiera wszystkie diagramy UML i
wszystkie zaimplementowane elementy diagramów. Mo¿na tworzyæ,
zapisywaæ i wczytywaæ obiekty, przegl±daæ istniej±ce modele, wymieniaæ
modele, generowaæ kod w Javie, eksportowaæ diagramy do ró¿nych
formatów i wiele wiêcej. Mo¿na j± za darmo rozpowszechniaæ, umieszczaæ
na lokalnych lub internetowych serwerach, dystrybuowaæ na CD lub DVD.
Gentleware nie udziela wsparcia dla wersji Community Edition.

Ogólnie Community Edition dostarcza wszystko co potrzebne do nauki i
u¿ywania UML-a w nieprofesjonalnym zakresie. Jednak ma kilka
restrykcji. Niektóre mo¿liwo¶ci s± dostêpne tylko w wersjach
komercyjnych, a nieobecne w darmowej Community Edition.

Te mo¿liwo¶ci s± przydatne do zwiêkszenia produktywno¶ci, ale nie s±
niezbêdne do tworzenia modeli UML. Z wa¿niejszych rzeczy, Community
Edition nie wspiera reverse- ani round-trip engineeringu oraz nie
mo¿e wczytywaæ wtyczek. Nie obs³uguje drukowania, kopiowania i
wklejania do schowka Windows, a powiêkszanie jest ograniczone. Inne
edycje mog± sprostaæ wymaganiom profesjonalnych u¿ytkowników.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},{%{_datadir},%{_examplesdir}}/%{name}}

sed -e 's#DATADIR#%{_datadir}#g' bin/poseidon.sh > $RPM_BUILD_ROOT%{_bindir}/poseidon
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}
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
