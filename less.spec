# - SECURITY: http://securitytracker.com/alerts/2004/Aug/1010988.html
Summary:	Text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(es):	Browser para archivo texto (- es +)
Summary(fr):	Une lecteur de fichiers texte
Summary(pl):	Przegl╠darka plikСw tekstowych - mniej jest wiЙcej
Summary(pt_BR):	Browser para arquivo texto (- И +)
Summary(ru):	Программа для просмотра текстовых файлов похожая на more, но лучше
Summary(tr):	Metin dosyasЩ gЖrЭntЭleyici - more benzeri
Summary(uk):	Програма для перегляду текстових файл╕в схожа на more, але краща
Name:		less
Version:	382
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
# Source0-md5:	103fe4aef6297b93f0f73f38cc3b1bd7
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	07bb76556307ab4cecba7abd3933bad2
Source2:	%{name}pipe.sh
Source3:	%{name}echo.1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shell.patch
Patch2:		%{name}-edit.patch
Patch3:		%{name}-libtinfo.patch
Patch4:		%{name}-locale-charmap.patch
URL:		http://www.greenwoodsoftware.com/less/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
Requires:	file
Requires:	setup >= 2.4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The less utility is a text file browser that resembles more, but has
more capabilities. Less allows you to move backwards in the file as
well as forwards. Since less doesn't have to read the entire input
file before it starts, less starts up more quickly than text editors
(for example, vi).

%description -l de
less ist ein Textdatei-Viewer Дhnlich 'more' ... aber besser!

%description -l es
less es un visor de archivo texto parecido con 'more', sСlo que mejor.

%description -l fr
less est un visualisateur de fichier texte, comme ╚ more ╩, mais en
mieux.

%description -l pl
Less jest programem podobnym w dziaЁaniu do standardowego unixowego
`more', lecz o znacznie wiЙkszych mo©liwo╤ciach.

%description -l pt_BR
less И um visualizador de arquivo texto parecido com 'more', sС que
melhor.

%description -l ru
Программа для просмотра текстовых файлов, похожа на more, но имеет
больше возможностей. less позволяет двигаться по файлу в обратном
направлении. Поскольку less не считывает предварительно весь входной
файл, он запускается значительно быстрее текстовых редакторов
(например, vi).

%description -l tr
less, more aracЩna Гok benzeyen ama ondan daha yetenekli bir dosya
gЖrЭntЭleme aracЩdЩr. Metin dosyalarЩnЩn sayfa sayfa gЖsterilmesini
saПlar.

%description -l uk
Програма для перегляду текстових файл╕в; схожа на more, але ма╓ б╕льше
можливостей. less дозволя╓ рухатись по файлу в зворотньому напрямку.
Оск╕льки less не зчиту╓ попередньо весь вх╕дний файл, в╕н запуска╓ться
значно швидше н╕ж текстов╕ редактори (наприклад, vi).

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
chmod -R u+w .
%{__autoconf}
%configure

%{__make} LIBS="-ltinfo" \
	CPPFLAGS="-D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT/etc/env.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man1/

# Prepare env file
cat > $RPM_BUILD_ROOT/etc/env.d/LESSOPEN <<EOF
LESSOPEN="|lesspipe.sh %s"
EOF

%ifarch axp
install -d $RPM_BUILD_ROOT/bin
ln -sf %{_bindir}/less $RPM_BUILD_ROOT/bin/more
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS

%attr(755,root,root) %{_bindir}/*
%config(noreplace,missingok) %verify(not md5 size mtime) /etc/env.d/LESSOPEN
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%ifarch axp
%attr(755,root,root) /bin/more
%endif
