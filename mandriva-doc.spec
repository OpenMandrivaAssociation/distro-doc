%define distrib_name Mandriva Linux
%define group Books/Computer books
%define libdrakx %{_prefix}/lib/libDrakX

Name:		mandriva-doc
Summary:	%distrib_name documentation
Version:	2007.1
Release:	%mkrel 1.1
License:	Open Publication License
Group:		%group
Url:		http://mandrivalinux.com/en/doc/project/

Source0:	%name-%version.tar.bz2
Source1:	%name.tar.bz2

Buildroot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires: 	Borges-DocBook
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

%package Discovery-en
Summary:        The %distrib_name manuals in English
Group:          %group
Requires:       locales-en
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-en
Provides:       mandrake_doc-en = %version
Obsoletes:      mandrake-doc-en
Provides:       mandrake-doc-en = %version
Obsoletes:      mandrake-doc-Discovery-en
Provides:       mandrake-doc-Discovery-en = %version

%description Discovery-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Starter-en
Summary:        The %distrib_name manuals in English
Group:          %group
Requires:       locales-en
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-en
Provides:       mandrake_doc-en = %version
Obsoletes:      mandrake-doc-en
Provides:       mandrake-doc-en = %version
Obsoletes:      mandrake-doc-Starter-en
Provides:       mandrake-doc-Starter-en = %version

%description Starter-en
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

%package Discovery-fr
Summary:        The %distrib_name manuals in French
Group:          %group
Requires:       locales-fr
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-fr
Provides:       mandrake_doc-fr = %version
Obsoletes:      mandrake-doc-fr
Provides:       mandrake-doc-fr = %version
Obsoletes:      mandrake-doc-Discovery-fr
Provides:       mandrake-doc-Discovery-fr = %version

%description Discovery-fr
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Starter-fr
Summary:        The %distrib_name manuals in French
Group:          %group
Requires:       locales-fr
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-fr
Provides:       mandrake_doc-fr = %version
Obsoletes:      mandrake-doc-fr
Provides:       mandrake-doc-fr = %version
Obsoletes:      mandrake-doc-Starter-fr
Provides:       mandrake-doc-Starter-fr = %version

%description Starter-fr
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

%package Starter-de
Summary:        The %distrib_name manuals in German
Group:          %group
Requires:       locales-de
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-de
Provides:       mandrake_doc-de = %version
Obsoletes:      mandrake-doc-de
Provides:       mandrake-doc-de = %version
Obsoletes:      mandrake-doc-Starter-de
Provides:       mandrake-doc-Starter-de = %version

%description Starter-de
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

%package Starter-es
Summary:        The %distrib_name manuals in Spanish
Group:          %group
Requires:       locales-es
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-es
Provides:       mandrake_doc-es = %version
Obsoletes:      mandrake-doc-es
Provides:       mandrake-doc-es = %version
Obsoletes:      mandrake-doc-Starter-es
Provides:       mandrake-doc-Starter-es = %version

%description Starter-es
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

./configure
make all MAX_TEX_RECURSION=10

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
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/Drakxtools-Guide/
mv Outputs/%name/en/Drakxtools-Guide.* $DESTDIR/mandriva/en/Drakxtools-Guide/

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Discovery-en.desktop << EOF
[Desktop Entry]
Name=%distrib_name Discovery User Guide in English
Comment=The %distrib_name manuals in English
Exec=%{_bindir}/www-browser %_docdir/mandriva/en/Discovery/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/Discovery/
mv Outputs/%name/en/Discovery.* $DESTDIR/mandriva/en/Discovery/

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Starter-en.desktop << EOF
[Desktop Entry]
Name=%distrib_name Starter Guide in English
Comment=The %distrib_name manuals in English
Exec=%{_bindir}/www-browser %_docdir/mandriva/en/Starter/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/Starter/
mv Outputs/%name/en/Starter.* $DESTDIR/mandriva/en/Starter/

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/en/
    for f in Outputs/%name/en/DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    install -m 0644 $f %buildroot/%_docdir/installer-help/en/$i
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
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/Drakxtools-Guide/
mv Outputs/%name/fr/Drakxtools-Guide.* $DESTDIR/mandriva/fr/Drakxtools-Guide/

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Discovery-fr.desktop << EOF
[Desktop Entry]
Name=%distrib_name Discovery User Guide in French
Comment=The %distrib_name manuals in French
Exec=%{_bindir}/www-browser %_docdir/mandriva/fr/Discovery/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/Discovery/
mv Outputs/%name/fr/Discovery.* $DESTDIR/mandriva/fr/Discovery/

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Starter-fr.desktop << EOF
[Desktop Entry]
Name=%distrib_name Starter Guide in French
Comment=The %distrib_name manuals in French
Exec=%{_bindir}/www-browser %_docdir/mandriva/fr/Starter/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/Starter/
mv Outputs/%name/fr/Starter.* $DESTDIR/mandriva/fr/Starter/

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/fr/
    for f in Outputs/%name/fr/DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    install -m 0644 $f %buildroot/%_docdir/installer-help/fr/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/fr/images
#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/pt_br/
    for f in Outputs/%name/pt_br/DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    install -m 0644 $f %buildroot/%_docdir/installer-help/pt_br/$i
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
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/it/
install -d -m 0755 $DESTDIR/mandriva/it/Drakxtools-Guide/
mv Outputs/%name/it/Drakxtools-Guide.* $DESTDIR/mandriva/it/Drakxtools-Guide/

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/it/
    for f in Outputs/%name/it/DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    install -m 0644 $f %buildroot/%_docdir/installer-help/it/$i
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
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/de/
install -d -m 0755 $DESTDIR/mandriva/de/Drakxtools-Guide/
mv Outputs/%name/de/Drakxtools-Guide.* $DESTDIR/mandriva/de/Drakxtools-Guide/

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Starter-de.desktop << EOF
[Desktop Entry]
Name=%distrib_name Starter Guide in German
Comment=The %distrib_name manuals in German
Exec=%{_bindir}/www-browser %_docdir/mandriva/de/Starter/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/de/
install -d -m 0755 $DESTDIR/mandriva/de/Starter/
mv Outputs/%name/de/Starter.* $DESTDIR/mandriva/de/Starter/

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/de/
    for f in Outputs/%name/de/DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    install -m 0644 $f %buildroot/%_docdir/installer-help/de/$i
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
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/es/
install -d -m 0755 $DESTDIR/mandriva/es/Drakxtools-Guide/
mv Outputs/%name/es/Drakxtools-Guide.* $DESTDIR/mandriva/es/Drakxtools-Guide/

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Starter-es.desktop << EOF
[Desktop Entry]
Name=%distrib_name Starter Guide in Spanish
Comment=The %distrib_name manuals in Spanish
Exec=%{_bindir}/www-browser %_docdir/mandriva/es/Starter/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Documentation
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/es/
install -d -m 0755 $DESTDIR/mandriva/es/Starter/
mv Outputs/%name/es/Starter.* $DESTDIR/mandriva/es/Starter/

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/es/
    for f in Outputs/%name/es/DrakX-Guide.html/*.html; do
    i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
    install -m 0644 $f %buildroot/%_docdir/installer-help/es/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/es/images
mv %buildroot/%_docdir/installer-help/en/* %buildroot/%_docdir/installer-help/
rm -f %buildroot/%_docdir/installer-help/images
mv Outputs/%name/en/DrakX-Guide.html/images %buildroot/%_docdir/installer-help/
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
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/en/Discovery/index.html <<EOF
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
    <a href="Discovery.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
    <tr>
      <a href="Discovery.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/en/Starter/index.html <<EOF
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
    <a href="Starter.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
    <tr>
      <a href="Starter.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
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
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/fr/Discovery/index.html <<EOF
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
    <a href="Discovery.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
    <tr>
      <a href="Discovery.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/fr/Starter/index.html <<EOF
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
    <a href="Starter.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
    <tr>
      <a href="Starter.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
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
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
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
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/de/Starter/index.html <<EOF
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
    <a href="Starter.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
    <tr>
      <a href="Starter.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
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
    <tr>
      <a href="Drakxtools-Guide.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
    </tbody>
  </table>
</center>
</body>
</html>
EOF
# build HTML index file
cat > $DESTDIR/mandriva/es/Starter/index.html <<EOF
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
    <a href="Starter.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
    <tr>
      <a href="Starter.pdf">
      <img src="../../images/manuel-face.png" align="center" border="0"> 
      PDF</a>
      </tr>
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

%post Discovery-en
%{update_menus}
%postun Discovery-en
%{clean_menus}

%post Starter-en
%{update_menus}
%postun Starter-en
%{clean_menus}

%post Drakxtools-Guide-fr
%{update_menus}
%postun Drakxtools-Guide-fr
%{clean_menus}

%post Discovery-fr
%{update_menus}
%postun Discovery-fr
%{clean_menus}

%post Starter-fr
%{update_menus}
%postun Starter-fr
%{clean_menus}

%post Drakxtools-Guide-it
%{update_menus}
%postun Drakxtools-Guide-it
%{clean_menus}

%post Drakxtools-Guide-de
%{update_menus}
%postun Drakxtools-Guide-de
%{clean_menus}

%post Starter-de
%{update_menus}
%postun Starter-de
%{clean_menus}

%post Drakxtools-Guide-es
%{update_menus}
%postun Drakxtools-Guide-es
%{clean_menus}

%post Starter-es
%{update_menus}
%postun Starter-es
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

%files Discovery-en
%defattr(-,root,root)
%{_datadir}/applications/%name-Discovery-en.desktop
%dir %_docdir/mandriva/en/Discovery
%doc %_docdir/mandriva/en/Discovery/*

%files Starter-en
%defattr(-,root,root)
%{_datadir}/applications/%name-Starter-en.desktop
%dir %_docdir/mandriva/en/Starter
%doc %_docdir/mandriva/en/Starter/*

%files Drakxtools-Guide-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-fr.desktop
%dir %_docdir/mandriva/fr/Drakxtools-Guide
%doc %_docdir/mandriva/fr/Drakxtools-Guide/*

%files Discovery-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Discovery-fr.desktop
%dir %_docdir/mandriva/fr/Discovery
%doc %_docdir/mandriva/fr/Discovery/*

%files Starter-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Starter-fr.desktop
%dir %_docdir/mandriva/fr/Starter
%doc %_docdir/mandriva/fr/Starter/*

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

%files Starter-de
%defattr(-,root,root)
%{_datadir}/applications/%name-Starter-de.desktop
%dir %_docdir/mandriva/de/Starter
%doc %_docdir/mandriva/de/Starter/*

%files Drakxtools-Guide-es
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-es.desktop
%dir %_docdir/mandriva/es/Drakxtools-Guide
%doc %_docdir/mandriva/es/Drakxtools-Guide/*

%files Starter-es
%defattr(-,root,root)
%{_datadir}/applications/%name-Starter-es.desktop
%dir %_docdir/mandriva/es/Starter
%doc %_docdir/mandriva/es/Starter/*





