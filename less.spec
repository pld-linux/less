Summary:	text file browser -- less is more
Summary(de):	Programm zum Anzeigen von Textdateien - weniger ist mehr
Summary(es):	Browser para archivo texto (- es +)
Summary(fr):	une lecteur de fichiers texte.
Summary(pl):	Przegl�darka plik�w tekstowych - mniej jest wi�cej
Summary(pt_BR):	Browser para arquivo texto (- � +)
Summary(ru):	��������� ��� ��������� ��������� ������ ������� �� more, �� �����
Summary(tr):	Metin dosyas� g�r�nt�leyici - more benzeri
Summary(uk):	�������� ��� ��������� ��������� ���̦� ����� �� more, ��� �����
Name:		less
Version:	374
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/less/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Source2:	%{name}pipe.sh
Source3:	%{name}.sh
Source4:	%{name}.csh
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-shell.patch
Patch2:		%{name}-edit.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	autoconf
URL:		http://www.flash.net/~marknu/less/
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

%build
chmod -R u+w .
autoconf
CPPFLAGS="-D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%configure

%{__make} LIBS="-ltinfo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir} $RPM_BUILD_ROOT/etc/profile.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT/etc/profile.d

gzip -9nf README NEWS

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
%attr(755,root,root) /etc/profile.d/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%ifarch axp
%attr(755,root,root) /bin/more
%endif
