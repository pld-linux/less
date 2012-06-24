Summary:	text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(fr):	une lecteur de fichiers texte.
Summary(pl):	Przegl�darka plik�w tekstowych -- mniej jest wi�cej ;)
Summary(tr):	less, more arac�na �ok benzeyen ama ondan daha yetenekli bir dosya g�r�nt�leme arac�d�r. Metin dosyalar�n�n sayfa sayfa g�sterilmesini sa�lar.
Name:       	less
Version:	332
Release:	5
Copyright:	distributable
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		ftp://prep.ai.mit.edu:/pub/gnu/%{name}-%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
less is a text file viewer much like 'more', only better.  

%description -l de
less ist ein Textdatei-Viewer �hnlich 'more' ... aber besser! 

%description -l fr
less est un visualisateur de fichier texte, comme � more �, mais en mieux

%description -l pl
Less jest programem podobnym w dzia�aniu do standardowego unixowego `more',
lecz o znacznie wi�kszych mo�liwo�ciach.

%description -l tr
Metin dosyas� g�r�nt�leyici - more benzeri

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

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%ifarch axp
install -d $RPM_BUILD_ROOT/bin
ln -sf /usr/bin/less /bin/more
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) /usr/bin/*
/usr/man/man1/*
%ifarch axp
%attr(755,root,root) /bin/more
%endif

%changelog
* Thu Mar 11 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [322-5]
- added Group(pl),
- added gzipping man pages,
- removed man group from man pages.

* Tue Oct 06 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [322-3]
- added pl translation,
- major modifications of the spec file.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- updated to 332 and built for Manhattan
- added buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
