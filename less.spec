Summary:	text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(fr):	une lecteur de fichiers texte.
Summary(pl):	Przegl±darka plików tekstowych -- mniej jest wiêcej ;)
Summary(tr):	less, more aracýna çok benzeyen ama ondan daha yetenekli bir \
Summary(tr):	dosya görüntüleme aracýdýr. Metin dosyalarýnýn sayfa sayfa \
Summary(tr):	gösterilmesini saðlar.
Name:       	less
Version:	332
Release:	6
Copyright:	distributable
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source:		ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Requires:	ncurses >= 4.2-12
Buildroot:	/tmp/%{name}-%{version}-root
Conflicts:	glibc <= 2.0.7

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
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr

make datadir=/usr/doc

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* \
	README NEWS

%ifarch axp
install -d $RPM_BUILD_ROOT/bin
ln -sf /usr/bin/less /bin/more
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS}.gz

%attr(755,root,root) /usr/bin/*
/usr/man/man1/*

%ifarch axp
%attr(755,root,root) /bin/more
%endif

%changelog
* Thu Mar 18 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [322-6]
- gzipping documentation (instead bzipping)

* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [322-5]
- added Group(pl),
- added "Requires: ncureses >= 4.2-12" and "Conflicts: glibc <= 2.0.7" for
  prevent installing in proper enviroment,
- added gzipping man pages,
- removed man group from man pages.

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [322-3]
- added pl translation,
- major modifications of the spec file.
- build against GNU libc-2.1,
- start at invalid RH spec file.
