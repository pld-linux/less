Summary:	text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(fr):	une lecteur de fichiers texte.
Summary(pl):	Przegl±darka plików tekstowych -- mniej jest wiêcej ;)
Summary(tr):	less, more aracýna çok benzeyen ama ondan daha yetenekli bir \
Summary(tr):	dosya görüntüleme aracýdýr. Metin dosyalarýnýn sayfa sayfa \
Summary(tr):	gösterilmesini saðlar.
Name:       	less
Version:	340
Release:	2
Copyright:	distributable
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Source1:	less.1.pl
Patch:		less-DESTDIR.patch
BuildPrereq:	ncurses-devel
BuildPrereq:	autoconf
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
%setup -q
%patch -p1

%build
chmod -R u+w .
autoconf
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

%changelog
* Mon May 17 1999 Artur Frysiak <wiget@pld.org.pl>
  [340-2]
- added less-DESTDIR.patch (using DESTDIR at install time)
- using more rpm's macros
- fixed permission to sources

* Thu Apr 28 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [340-1]
- upadted to 340,
- removed "Conflicts: glibc <= 2.0.7" (not neccessary now),
- removed Requires: ncurses,
- added BuildPrereq: ncurses-devel,
- removed --mandir=/usr/man/man1 from ./configure,
- removed mandir and datadir definitions from make and make install options 
  (they seem to be no longer needed),
- recompiled on rpm 3.

* Thu Apr  1 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [335-1]
- added pl man page for less(1).

* Thu Mar 18 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [332-6]
- gzipping documentation (instead bzipping)

* Thu Mar 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [332-5]
- added Group(pl),
- added "Requires: ncureses >= 4.2-12" and "Conflicts: glibc <= 2.0.7" for
  prevent installing in proper enviroment,
- added gzipping man pages,
- removed man group from man pages.

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [332-3]
- added pl translation,
- major modifications of the spec file.
- build against GNU libc-2.1,
- start at invalid RH spec file.
