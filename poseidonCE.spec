Summary:	Poseidon Community Edition for UML
Summary(pl.UTF-8):	Poseidon dla UML-a w wersji Community Edition
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

%description -l pl.UTF-8
Wersja Community Edition jest w pełni użyteczna do modelowania UML i
może być używana w dowolnych zastosowaniach, komercyjnych lub nie,
przez dowolny okres i dowolnie dużo. Zawiera wszystkie diagramy UML i
wszystkie zaimplementowane elementy diagramów. Można tworzyć,
zapisywać i wczytywać obiekty, przeglądać istniejące modele, wymieniać
modele, generować kod w Javie, eksportować diagramy do różnych
formatów i wiele więcej. Można ją za darmo rozpowszechniać, umieszczać
na lokalnych lub internetowych serwerach, dystrybuować na CD lub DVD.
Gentleware nie udziela wsparcia dla wersji Community Edition.

Ogólnie Community Edition dostarcza wszystko co potrzebne do nauki i
używania UML-a w nieprofesjonalnym zakresie. Jednak ma kilka
restrykcji. Niektóre możliwości są dostępne tylko w wersjach
komercyjnych, a nieobecne w darmowej Community Edition.

Te możliwości są przydatne do zwiększenia produktywności, ale nie są
niezbędne do tworzenia modeli UML. Z ważniejszych rzeczy, Community
Edition nie wspiera reverse- ani round-trip engineeringu oraz nie może
wczytywać wtyczek. Nie obsługuje drukowania, kopiowania i wklejania do
schowka Windows, a powiększanie jest ograniczone. Inne edycje mogą
sprostać wymaganiom profesjonalnych użytkowników.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},{%{_datadir},%{_examplesdir}}/%{name}}

sed -e 's#DATADIR#%{_datadir}#g' bin/poseidon.sh > $RPM_BUILD_ROOT%{_bindir}/poseidon
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -a lib license-keys.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

ln -sf %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt docs/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_examplesdir}/%{name}
