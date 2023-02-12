Summary:	Text file browser -- less is more
Summary(de.UTF-8):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(es.UTF-8):	Browser para archivo texto (- es +)
Summary(fr.UTF-8):	Une lecteur de fichiers texte
Summary(pl.UTF-8):	Przeglądarka plików tekstowych - mniej jest więcej
Summary(pt_BR.UTF-8):	Browser para arquivo texto (- é +)
Summary(ru.UTF-8):	Программа для просмотра текстовых файлов похожая на more, но лучше
Summary(tr.UTF-8):	Metin dosyası görüntüleyici - more benzeri
Summary(uk.UTF-8):	Програма для перегляду текстових файлів схожа на more, але краща
Name:		less
Version:	608
Release:	2
License:	GPL v3+
Group:		Applications/Text
#Source0Download: http://www.greenwoodsoftware.com/less/download.html
Source0:	https://www.greenwoodsoftware.com/less/%{name}-%{version}.tar.gz
# Source0-md5:	1cdec714569d830a68f4cff11203cdba
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	07bb76556307ab4cecba7abd3933bad2
Source2:	%{name}echo.1
Patch0:		%{name}-shell.patch
Patch1:		%{name}-multilib.patch
Patch2:		%{name}-libtinfo.patch
Patch3:		%{name}-procfs.patch
URL:		http://www.greenwoodsoftware.com/less/
BuildRequires:	autoconf >= 2.50
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.317
Requires:	setup >= 2.4.6
Suggests:	lesspipe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The less utility is a text file browser that resembles more, but has
more capabilities. Less allows you to move backwards in the file as
well as forwards. Since less doesn't have to read the entire input
file before it starts, less starts up more quickly than text editors
(for example, vi).

%description -l de.UTF-8
less ist ein Textdatei-Viewer ähnlich 'more' ... aber besser!

%description -l es.UTF-8
less es un visor de archivo texto parecido con 'more', sólo que mejor.

%description -l fr.UTF-8
less est un visualisateur de fichier texte, comme « more », mais en
mieux.

%description -l pl.UTF-8
Less jest programem podobnym w działaniu do standardowego uniksowego
`more', lecz o znacznie większych możliwościach.

%description -l pt_BR.UTF-8
less é um visualizador de arquivo texto parecido com 'more', só que
melhor.

%description -l ru.UTF-8
Программа для просмотра текстовых файлов, похожа на more, но имеет
больше возможностей. less позволяет двигаться по файлу в обратном
направлении. Поскольку less не считывает предварительно весь входной
файл, он запускается значительно быстрее текстовых редакторов
(например, vi).

%description -l tr.UTF-8
less, more aracına çok benzeyen ama ondan daha yetenekli bir dosya
görüntüleme aracıdır. Metin dosyalarının sayfa sayfa gösterilmesini
sağlar.

%description -l uk.UTF-8
Програма для перегляду текстових файлів; схожа на more, але має більше
можливостей. less дозволяє рухатись по файлу в зворотньому напрямку.
Оскільки less не зчитує попередньо весь вхідний файл, він запускається
значно швидше ніж текстові редактори (наприклад, vi).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir},/etc/env.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Prepare env files
echo '#LESS="i m q s X -M"' > $RPM_BUILD_ROOT/etc/env.d/LESS
echo '#PAGER=less' > $RPM_BUILD_ROOT/etc/env.d/PAGER

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1

%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.less-non-english-man-pages*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%env_update

%postun
%env_update

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/less*
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/LESS
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/PAGER
%{_mandir}/man1/less*.1*
%lang(de) %{_mandir}/de/man1/less.1*
%lang(hu) %{_mandir}/hu/man1/less.1*
%lang(it) %{_mandir}/it/man1/less*.1*
%lang(ja) %{_mandir}/ja/man1/less*.1*
%lang(pl) %{_mandir}/pl/man1/less*.1*
