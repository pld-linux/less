# - SECURITY: http://securitytracker.com/alerts/2004/Aug/1010988.html
Summary:	Text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(es):	Browser para archivo texto (- es +)
Summary(fr):	Une lecteur de fichiers texte
Summary(pl):	Przegl�darka plik�w tekstowych - mniej jest wi�cej
Summary(pt_BR):	Browser para arquivo texto (- � +)
Summary(ru):	��������� ��� ��������� ��������� ������ ������� �� more, �� �����
Summary(tr):	Metin dosyas� g�r�nt�leyici - more benzeri
Summary(uk):	�������� ��� ��������� ��������� ���̦� ����� �� more, ��� �����
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
less ist ein Textdatei-Viewer �hnlich 'more' ... aber besser!

%description -l es
less es un visor de archivo texto parecido con 'more', s�lo que mejor.

%description -l fr
less est un visualisateur de fichier texte, comme � more �, mais en
mieux.

%description -l pl
Less jest programem podobnym w dzia�aniu do standardowego unixowego
`more', lecz o znacznie wi�kszych mo�liwo�ciach.

%description -l pt_BR
less � um visualizador de arquivo texto parecido com 'more', s� que
melhor.

%description -l ru
��������� ��� ��������� ��������� ������, ������ �� more, �� �����
������ ������������. less ��������� ��������� �� ����� � ��������
�����������. ��������� less �� ��������� �������������� ���� �������
����, �� ����������� ����������� ������� ��������� ����������
(��������, vi).

%description -l tr
less, more arac�na �ok benzeyen ama ondan daha yetenekli bir dosya
g�r�nt�leme arac�d�r. Metin dosyalar�n�n sayfa sayfa g�sterilmesini
sa�lar.

%description -l uk
�������� ��� ��������� ��������� ���̦�; ����� �� more, ��� ��� ¦����
�����������. less ������Ѥ �������� �� ����� � ����������� ��������.
��˦���� less �� ����դ ���������� ���� �Ȧ���� ����, צ� ������������
������ ������ Φ� ������צ ��������� (���������, vi).

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
