Summary:	text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(fr):	une lecteur de fichiers texte.
Summary(pl):	Przegl±darka plików tekstowych -- mniej jest wiêcej ;)
Summary(tr):	less, more aracýna çok benzeyen ama ondan daha yetenekli bir \
Summary(tr):	dosya görüntüleme aracýdýr. Metin dosyalarýnýn sayfa sayfa \
Summary(tr):	gösterilmesini saðlar.
Name:       	less
Version:	340
Release:	3
Copyright:	distributable
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Source1:	less.1.pl
Patch0:		less-DESTDIR.patch
Patch1:		less-keys.patch
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
Buildroot:	/tmp/%{name}-%{version}-root

%description
less is a text file viewer much like 'more', only better.  

%description -l de
less ist ein Textdatei-Viewer ähnlich 'more' ... aber besser! 

%description -l fr
less est un visualisateur de fichier texte, comme « more », mais en mieux

%description -l pl
Less jest programem podobnym w dzia³aniu do standardowego unixowego
`more', lecz o znacznie wiêkszych mo¿liwo¶ciach.

%description -l tr
Metin dosyasý görüntüleyici - more benzeri

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
chmod -R u+w .
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pl/man1

make install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/less.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1/*,pl/man1/*} \
	README NEWS

%ifarch axp
install -d $RPM_BUILD_ROOT/bin
ln -sf %{_bindir}/less $RPM_BUILD_ROOT/bin/more
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS}.gz

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%ifarch axp
%attr(755,root,root) /bin/more
%endif
