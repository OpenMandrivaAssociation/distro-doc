%define distrib_name Mandriva Linux
%define group Books/Computer books
%define libdrakx %{_prefix}/lib/libDrakX

Name:		mandriva-doc
Summary:	%distrib_name documentation
Version:	2008.0
Release:	%mkrel 0.1
License:	Open Publication License
Group:		%group
Url:		http://wiki.mandriva.com/en/Development/Tasks/Documentation/

Source0:	%name-%version.tar.bz2
Source1:	%name.tar.bz2

Buildroot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires: 	make
BuildRequires: 	perl
BuildRequires: 	libxslt-proc
BuildRequires: 	ImageMagick
BuildRequires: 	docbook-style-xsl
BuildRequires:	docbook-dtd44-xml
BuildRequires:	tetex-cmsuper
BuildRequires: 	inkscape
BuildRequires:  locales-en
BuildRequires:  locales-fr
BuildRequires:  locales-pt
BuildRequires:  locales-it
BuildRequires:  locales-de
BuildRequires:  locales-es


%define LANGS en fr pt_br it de es

%description
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the menus.


%package Drakxtools-Guide-en
Summary:        The %distrib_name manuals in English
Group:          %group
Requires:       locales-en
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-en
Provides:       mandrake_doc-drakxtools-en = %version
Obsoletes:      mandrake-doc-drakxtools-en
Provides:       mandrake-doc-drakxtools-en = %version
Obsoletes:      mandrake-doc-Drakxtools-Guide-en
Provides:       mandrake-doc-Drakxtools-Guide-en = %version

%description Drakxtools-Guide-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package DVD-Booklet-en
Summary:        The %distrib_name manuals in English
Group:          %group
Requires:       locales-en
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-en
Provides:       mandrake_doc-en = %version
Obsoletes:      mandrake-doc-en
Provides:       mandrake-doc-en = %version
Obsoletes:      mandrake-doc-DVD-Booklet-en
Provides:       mandrake-doc-DVD-Booklet-en = %version

%description DVD-Booklet-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-fr
Summary:        The %distrib_name manuals in French
Group:          %group
Requires:       locales-fr
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-fr
Provides:       mandrake_doc-drakxtools-fr = %version
Obsoletes:      mandrake-doc-drakxtools-fr
Provides:       mandrake-doc-drakxtools-fr = %version
Obsoletes:      mandrake-doc-Drakxtools-Guide-fr
Provides:       mandrake-doc-Drakxtools-Guide-fr = %version

%description Drakxtools-Guide-fr
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package DVD-Booklet-fr
Summary:        The %distrib_name manuals in French
Group:          %group
Requires:       locales-fr
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-fr
Provides:       mandrake_doc-fr = %version
Obsoletes:      mandrake-doc-fr
Provides:       mandrake-doc-fr = %version
Obsoletes:      mandrake-doc-DVD-Booklet-fr
Provides:       mandrake-doc-DVD-Booklet-fr = %version

%description DVD-Booklet-fr
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-pt_br
Summary:        The %distrib_name manuals in Brazilian Portuguese
Group:          %group
Requires:       locales-pt
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-pt_br
Provides:       mandrake_doc-drakxtools-pt_br = %version
Obsoletes:      mandrake-doc-drakxtools-pt_br
Provides:       mandrake-doc-drakxtools-pt_br = %version
Obsoletes:      mandrake-doc-Drakxtools-Guide-pt_br
Provides:       mandrake-doc-Drakxtools-Guide-pt_br = %version

%description Drakxtools-Guide-pt_br
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package DVD-Booklet-pt_br
Summary:        The %distrib_name manuals in Brazilian Portuguese
Group:          %group
Requires:       locales-pt
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-pt_br
Provides:       mandrake_doc-pt_br = %version
Obsoletes:      mandrake-doc-pt_br
Provides:       mandrake-doc-pt_br = %version
Obsoletes:      mandrake-doc-DVD-Booklet-pt_br
Provides:       mandrake-doc-DVD-Booklet-pt_br = %version

%description DVD-Booklet-pt_br
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-it
Summary:        The %distrib_name manuals in Italian
Group:          %group
Requires:       locales-it
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-it
Provides:       mandrake_doc-drakxtools-it = %version
Obsoletes:      mandrake-doc-drakxtools-it
Provides:       mandrake-doc-drakxtools-it = %version
Obsoletes:      mandrake-doc-Drakxtools-Guide-it
Provides:       mandrake-doc-Drakxtools-Guide-it = %version

%description Drakxtools-Guide-it
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-de
Summary:        The %distrib_name manuals in German
Group:          %group
Requires:       locales-de
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-de
Provides:       mandrake_doc-drakxtools-de = %version
Obsoletes:      mandrake-doc-drakxtools-de
Provides:       mandrake-doc-drakxtools-de = %version
Obsoletes:      mandrake-doc-Drakxtools-Guide-de
Provides:       mandrake-doc-Drakxtools-Guide-de = %version

%description Drakxtools-Guide-de
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-es
Summary:        The %distrib_name manuals in Spanish
Group:          %group
Requires:       locales-es
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-es
Provides:       mandrake_doc-drakxtools-es = %version
Obsoletes:      mandrake-doc-drakxtools-es
Provides:       mandrake-doc-drakxtools-es = %version
Obsoletes:      mandrake-doc-Drakxtools-Guide-es
Provides:       mandrake-doc-Drakxtools-Guide-es = %version

%description Drakxtools-Guide-es
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.




%package common
Summary:	Common data for all %distrib_name specific documentation
Group:		%group
Conflicts:	mandrake_doc < 9.2
Obsoletes: 	mandrake_doc-common
Provides:	mandrake_doc-common
Obsoletes: 	mandrake-doc-common
Provides:	mandrake-doc-common

%description common

This package contains common icons and images for all %distrib_name
specific documentation, plus the index file matching Help IDs to HTML
help pages.

%package installer-help
Summary:	DrakX Installer help in all available languages for %distrib_name
Group:		%group

%description installer-help

This package contains the HTML files used as inline help during the
installation procedure of %distrib_name


%prep

%setup -q -a 1

%build

make -C en Master-DrakX-Guide.html
make -C en Master-Drakxtools-Guide.html
make -C en Master-DVD-Booklet.html
make -C fr Master-DrakX-Guide.html
make -C fr Master-Drakxtools-Guide.html
make -C fr Master-DVD-Booklet.html
make -C pt_br Master-DrakX-Guide.html
make -C pt_br Master-Drakxtools-Guide.html
make -C pt_br Master-DVD-Booklet.html
make -C it Master-DrakX-Guide.html
make -C it Master-Drakxtools-Guide.html
make -C de Master-DrakX-Guide.html
make -C de Master-Drakxtools-Guide.html
make -C es Master-DrakX-Guide.html
make -C es Master-Drakxtools-Guide.html


%install
rm -fr %buildroot


install -d -m 0755 %buildroot/%_menudir
DESTDIR=%buildroot/%{_docdir}

#install the books themselves and menu entries

install -d -m 0755 $DESTDIR/mandriva/images/


# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Drakxtools-Guide-en.desktop << EOF
[Desktop Entry]
Name=%distrib_name DrakXTools User Manual in English
Comment=The %distrib_name manuals in English
Exec=%{_bindir}/www-browser %_docdir/mandriva/en/Drakxtools-Guide/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/Drakxtools-Guide/
mv en/Master-Drakxtools-Guide.html $DESTDIR/mandriva/en/Drakxtools-Guide/Drakxtools-Guide.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-DVD-Booklet-en.desktop << EOF
[Desktop Entry]
Name=%distrib_name Quick Startup Guide in English
Comment=The %distrib_name manuals in English
Exec=%{_bindir}/www-browser %_docdir/mandriva/en/DVD-Booklet/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/DVD-Booklet/
mv en/Master-DVD-Booklet.html $DESTDIR/mandriva/en/DVD-Booklet/DVD-Booklet.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/en/
    for f in en/Master-DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    mv $f %buildroot/%_docdir/installer-help/en/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/en/images
# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Drakxtools-Guide-fr.desktop << EOF
[Desktop Entry]
Name=%distrib_name DrakXTools User Manual in French
Comment=The %distrib_name manuals in French
Exec=%{_bindir}/www-browser %_docdir/mandriva/fr/Drakxtools-Guide/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/Drakxtools-Guide/
mv fr/Master-Drakxtools-Guide.html $DESTDIR/mandriva/fr/Drakxtools-Guide/Drakxtools-Guide.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-DVD-Booklet-fr.desktop << EOF
[Desktop Entry]
Name=%distrib_name Quick Startup Guide in French
Comment=The %distrib_name manuals in French
Exec=%{_bindir}/www-browser %_docdir/mandriva/fr/DVD-Booklet/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/DVD-Booklet/
mv fr/Master-DVD-Booklet.html $DESTDIR/mandriva/fr/DVD-Booklet/DVD-Booklet.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/fr/
    for f in fr/Master-DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    mv $f %buildroot/%_docdir/installer-help/fr/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/fr/images
# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Drakxtools-Guide-pt_br.desktop << EOF
[Desktop Entry]
Name=%distrib_name DrakXTools User Manual in Brazilian Portuguese
Comment=The %distrib_name manuals in Brazilian Portuguese
Exec=%{_bindir}/www-browser %_docdir/mandriva/pt_br/Drakxtools-Guide/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/pt_br/
install -d -m 0755 $DESTDIR/mandriva/pt_br/Drakxtools-Guide/
mv pt_br/Master-Drakxtools-Guide.html $DESTDIR/mandriva/pt_br/Drakxtools-Guide/Drakxtools-Guide.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-DVD-Booklet-pt_br.desktop << EOF
[Desktop Entry]
Name=%distrib_name Quick Startup Guide in Brazilian Portuguese
Comment=The %distrib_name manuals in Brazilian Portuguese
Exec=%{_bindir}/www-browser %_docdir/mandriva/pt_br/DVD-Booklet/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/pt_br/
install -d -m 0755 $DESTDIR/mandriva/pt_br/DVD-Booklet/
mv pt_br/Master-DVD-Booklet.html $DESTDIR/mandriva/pt_br/DVD-Booklet/DVD-Booklet.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/pt_br/
    for f in pt_br/Master-DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    mv $f %buildroot/%_docdir/installer-help/pt_br/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/pt_br/images
# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Drakxtools-Guide-it.desktop << EOF
[Desktop Entry]
Name=%distrib_name DrakXTools User Manual in Italian
Comment=The %distrib_name manuals in Italian
Exec=%{_bindir}/www-browser %_docdir/mandriva/it/Drakxtools-Guide/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/it/
install -d -m 0755 $DESTDIR/mandriva/it/Drakxtools-Guide/
mv it/Master-Drakxtools-Guide.html $DESTDIR/mandriva/it/Drakxtools-Guide/Drakxtools-Guide.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/it/
    for f in it/Master-DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    mv $f %buildroot/%_docdir/installer-help/it/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/it/images
# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Drakxtools-Guide-de.desktop << EOF
[Desktop Entry]
Name=%distrib_name DrakXTools User Manual in German
Comment=The %distrib_name manuals in German
Exec=%{_bindir}/www-browser %_docdir/mandriva/de/Drakxtools-Guide/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/de/
install -d -m 0755 $DESTDIR/mandriva/de/Drakxtools-Guide/
mv de/Master-Drakxtools-Guide.html $DESTDIR/mandriva/de/Drakxtools-Guide/Drakxtools-Guide.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/de/
    for f in de/Master-DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    mv $f %buildroot/%_docdir/installer-help/de/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/de/images
# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Drakxtools-Guide-es.desktop << EOF
[Desktop Entry]
Name=%distrib_name DrakXTools User Manual in Spanish
Comment=The %distrib_name manuals in Spanish
Exec=%{_bindir}/www-browser %_docdir/mandriva/es/Drakxtools-Guide/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/es/
install -d -m 0755 $DESTDIR/mandriva/es/Drakxtools-Guide/
mv es/Master-Drakxtools-Guide.html $DESTDIR/mandriva/es/Drakxtools-Guide/Drakxtools-Guide.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/es/
    for f in es/Master-DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    mv $f %buildroot/%_docdir/installer-help/es/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/es/images
mv %buildroot/%_docdir/installer-help/en/* %buildroot/%_docdir/installer-help/
rm -f %buildroot/%_docdir/installer-help/images
mv en/Master-DrakX-Guide.html/images %buildroot/%_docdir/installer-help/
rm -rf %buildroot/%_docdir/installer-help/en
ln -s . %buildroot/%_docdir/installer-help/en
sed -i -e 's!drakxid-!!g; s!drakx-!!g' %buildroot/%_docdir/installer-help/*.html %buildroot/%_docdir/installer-help/*/*.html


# build HTML index file
cat > $DESTDIR/mandriva/en/Drakxtools-Guide/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="Drakxtools-Guide.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/en/DVD-Booklet/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="DVD-Booklet.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="DVD-Booklet.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/fr/Drakxtools-Guide/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="Drakxtools-Guide.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/fr/DVD-Booklet/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="DVD-Booklet.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="DVD-Booklet.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/pt_br/Drakxtools-Guide/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="Drakxtools-Guide.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/pt_br/DVD-Booklet/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="DVD-Booklet.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="DVD-Booklet.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/it/Drakxtools-Guide/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="Drakxtools-Guide.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/de/Drakxtools-Guide/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="Drakxtools-Guide.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/es/Drakxtools-Guide/index.html <<EOF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body>
<center>
<img src="../../images/MDKlinux.png" border="0">
<br/><br/>
<table style="width: 80%;" >
  <tbody>
    <tr>
    <a href="Drakxtools-Guide.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
-->
    </tbody>
  </table>
</center>
</body>
</html>
EOF


# install ctxhelp.pm which tells drakhelp which HTML help page
# corresponds to which application help button
install -d -m 0755 %buildroot/%{libdrakx}/
install -m 0644 %name/ctxhelp.pm %buildroot/%{libdrakx}/
install -d -m 0755 %buildroot/%_sbindir/
install -m 0755 %name/drakhelp_inst %buildroot/%_sbindir/
# install images for index files
for i in mandriva-doc/images/*; do
  install -m 0644 $i %buildroot/%_docdir/mandriva/images/
done

%clean
rm -fr %buildroot


%post Drakxtools-Guide-en
%{update_menus}
%postun Drakxtools-Guide-en
%{clean_menus}

%post DVD-Booklet-en
%{update_menus}
%postun DVD-Booklet-en
%{clean_menus}

%post Drakxtools-Guide-fr
%{update_menus}
%postun Drakxtools-Guide-fr
%{clean_menus}

%post DVD-Booklet-fr
%{update_menus}
%postun DVD-Booklet-fr
%{clean_menus}

%post Drakxtools-Guide-pt_br
%{update_menus}
%postun Drakxtools-Guide-pt_br
%{clean_menus}

%post DVD-Booklet-pt_br
%{update_menus}
%postun DVD-Booklet-pt_br
%{clean_menus}

%post Drakxtools-Guide-it
%{update_menus}
%postun Drakxtools-Guide-it
%{clean_menus}

%post Drakxtools-Guide-de
%{update_menus}
%postun Drakxtools-Guide-de
%{clean_menus}

%post Drakxtools-Guide-es
%{update_menus}
%postun Drakxtools-Guide-es
%{clean_menus}




%files common
%defattr(-,root,root)
%dir %_docdir/mandriva/
%{libdrakx}/ctxhelp.pm
%_sbindir/drakhelp_inst
%docdir %_docdir/mandriva/images/
%dir %_docdir/mandriva/images/
%doc %_docdir/mandriva/images/*

%files installer-help
%defattr(-,root,root)
%dir %_docdir/installer-help/
%docdir %_docdir/installer-help/
%doc %_docdir/installer-help/*

%files Drakxtools-Guide-en
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-en.desktop
%dir %_docdir/mandriva/en/Drakxtools-Guide
%doc %_docdir/mandriva/en/Drakxtools-Guide/*

%files DVD-Booklet-en
%defattr(-,root,root)
%{_datadir}/applications/%name-DVD-Booklet-en.desktop
%dir %_docdir/mandriva/en/DVD-Booklet
%doc %_docdir/mandriva/en/DVD-Booklet/*

%files Drakxtools-Guide-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-fr.desktop
%dir %_docdir/mandriva/fr/Drakxtools-Guide
%doc %_docdir/mandriva/fr/Drakxtools-Guide/*

%files DVD-Booklet-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-DVD-Booklet-fr.desktop
%dir %_docdir/mandriva/fr/DVD-Booklet
%doc %_docdir/mandriva/fr/DVD-Booklet/*

%files Drakxtools-Guide-pt_br
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-pt_br.desktop
%dir %_docdir/mandriva/pt_br/Drakxtools-Guide
%doc %_docdir/mandriva/pt_br/Drakxtools-Guide/*

%files DVD-Booklet-pt_br
%defattr(-,root,root)
%{_datadir}/applications/%name-DVD-Booklet-pt_br.desktop
%dir %_docdir/mandriva/pt_br/DVD-Booklet
%doc %_docdir/mandriva/pt_br/DVD-Booklet/*

%files Drakxtools-Guide-it
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-it.desktop
%dir %_docdir/mandriva/it/Drakxtools-Guide
%doc %_docdir/mandriva/it/Drakxtools-Guide/*

%files Drakxtools-Guide-de
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-de.desktop
%dir %_docdir/mandriva/de/Drakxtools-Guide
%doc %_docdir/mandriva/de/Drakxtools-Guide/*

%files Drakxtools-Guide-es
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-es.desktop
%dir %_docdir/mandriva/es/Drakxtools-Guide
%doc %_docdir/mandriva/es/Drakxtools-Guide/*



%changelog

