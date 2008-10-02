%define distrib_name Mandriva Linux
%define group Books/Computer books
%define libdrakx %{_prefix}/lib/libDrakX
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name:		mandriva-doc
Summary:	%distrib_name documentation
Version:	2009.0
Release:	%mkrel 0.6
License:	Open Publication License
Group:		%group
Url:		http://wiki.mandriva.com/en/Development/Tasks/Documentation

Source0:	%name.tar.bz2
Source1:	%name-%version.tar.bz2

Buildroot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch
BuildRequires:  wget
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


%package Mastering-Manual-en
Summary:        The %distrib_name manuals in English
Group:          %group
Requires:       locales-en
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-en
Provides:       mandriva-doc-Discovery-en = %version
Obsoletes:      mandriva-doc-Discovery-en                                                                                                                                                            
Provides:       mandriva-doc-Discovery-en = %version
Obsoletes:      mandrake-doc-Mastering-Manual-en
Provides:       mandrake-doc-Mastering-Manual-en = %version

%description Mastering-Manual-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

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

%package Introducing-en
Summary:        The %distrib_name manuals in English
Group:          %group
Requires:       locales-en
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-en
Provides:       mandrake_doc-en = %version
Obsoletes:      mandrake-doc-en
Provides:       mandrake-doc-en = %version
Obsoletes:      mandrake-doc-Introducing-en
Provides:       mandrake-doc-Introducing-en = %version

%description Introducing-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Mastering-Manual-fr
Summary:        The %distrib_name manuals in French
Group:          %group
Requires:       locales-fr
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-drakxtools-fr
Provides:       mandriva-doc-Discovery-fr = %version
Obsoletes:      mandriva-doc-Discovery-fr                                                                                                                                                            
Provides:       mandriva-doc-Discovery-fr = %version
Obsoletes:      mandrake-doc-Mastering-Manual-fr
Provides:       mandrake-doc-Mastering-Manual-fr = %version

%description Mastering-Manual-fr
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

%package Introducing-fr
Summary:        The %distrib_name manuals in French
Group:          %group
Requires:       locales-fr
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-fr
Provides:       mandrake_doc-fr = %version
Obsoletes:      mandrake-doc-fr
Provides:       mandrake-doc-fr = %version
Obsoletes:      mandrake-doc-Introducing-fr
Provides:       mandrake-doc-Introducing-fr = %version

%description Introducing-fr
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

%package Introducing-pt_br
Summary:        The %distrib_name manuals in Brazilian Portuguese
Group:          %group
Requires:       locales-pt
Requires:       mandriva-doc-common >= %version-%release
Obsoletes:      mandrake_doc-pt_br
Provides:       mandrake_doc-pt_br = %version
Obsoletes:      mandrake-doc-pt_br
Provides:       mandrake-doc-pt_br = %version
Obsoletes:      mandrake-doc-Introducing-pt_br
Provides:       mandrake-doc-Introducing-pt_br = %version

%description Introducing-pt_br
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

%setup -q -c %name-%version -a 1


%install
rm -fr %buildroot


install -d -m 0755 %buildroot/%_menudir
DESTDIR=%buildroot/%{_docdir}

#install the books themselves and menu entries

install -d -m 0755 $DESTDIR/mandriva/images/


# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Mastering-Manual-en.desktop << EOF
[Desktop Entry]
Name=%distrib_name Starter Guide in English
Comment=The %distrib_name manuals in English
Exec=%{_bindir}/www-browser %_docdir/mandriva/en/Mastering-Manual/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/Mastering-Manual/
mv publications/en/Mastering-Manual.html $DESTDIR/mandriva/en/Mastering-Manual/Mastering-Manual.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/en/
for f in publications/en/DrakX-Help.html/*.html; do
i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
mv $f %buildroot/%_docdir/installer-help/en/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/en/images
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
mv publications/en/Drakxtools-Guide.html $DESTDIR/mandriva/en/Drakxtools-Guide/Drakxtools-Guide.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Introducing-en.desktop << EOF
[Desktop Entry]
Name=%distrib_name Quick Startup Guide in English
Comment=The %distrib_name manuals in English
Exec=%{_bindir}/www-browser %_docdir/mandriva/en/Introducing/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/en/
install -d -m 0755 $DESTDIR/mandriva/en/Introducing/
mv publications/en/Introducing.html $DESTDIR/mandriva/en/Introducing/Introducing.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Mastering-Manual-fr.desktop << EOF
[Desktop Entry]
Name=%distrib_name Starter Guide in French
Comment=The %distrib_name manuals in French
Exec=%{_bindir}/www-browser %_docdir/mandriva/fr/Mastering-Manual/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/Mastering-Manual/
mv publications/fr/Mastering-Manual.html $DESTDIR/mandriva/fr/Mastering-Manual/Mastering-Manual.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/fr/
for f in publications/fr/DrakX-Help.html/*.html; do
i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
mv $f %buildroot/%_docdir/installer-help/fr/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/fr/images
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
mv publications/fr/Drakxtools-Guide.html $DESTDIR/mandriva/fr/Drakxtools-Guide/Drakxtools-Guide.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Introducing-fr.desktop << EOF
[Desktop Entry]
Name=%distrib_name Quick Startup Guide in French
Comment=The %distrib_name manuals in French
Exec=%{_bindir}/www-browser %_docdir/mandriva/fr/Introducing/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/fr/
install -d -m 0755 $DESTDIR/mandriva/fr/Introducing/
mv publications/fr/Introducing.html $DESTDIR/mandriva/fr/Introducing/Introducing.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/pt_br/
for f in publications/pt_br/DrakX-Help.html/*.html; do
i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
mv $f %buildroot/%_docdir/installer-help/pt_br/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/pt_br/images
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
mv publications/pt_br/Drakxtools-Guide.html $DESTDIR/mandriva/pt_br/Drakxtools-Guide/Drakxtools-Guide.html

# build menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}-Introducing-pt_br.desktop << EOF
[Desktop Entry]
Name=%distrib_name Quick Startup Guide in Brazilian Portuguese
Comment=The %distrib_name manuals in Brazilian Portuguese
Exec=%{_bindir}/www-browser %_docdir/mandriva/pt_br/Introducing/index.html
Icon=documentation_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Documentation;
EOF

# install manuals
install -d -m 0755 $DESTDIR/mandriva/pt_br/
install -d -m 0755 $DESTDIR/mandriva/pt_br/Introducing/
mv publications/pt_br/Introducing.html $DESTDIR/mandriva/pt_br/Introducing/Introducing.html

#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/it/
for f in publications/it/DrakX-Help.html/*.html; do
i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
mv $f %buildroot/%_docdir/installer-help/it/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/it/images
#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/de/
for f in publications/de/DrakX-Help.html/*.html; do
i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
mv $f %buildroot/%_docdir/installer-help/de/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/de/images
#install the DrakX Inline HTML Help
install -d -m 0755 $DESTDIR/installer-help/es/
for f in publications/es/DrakX-Help.html/*.html; do
i=$(basename $f | sed -e "s/drakxid-//; s/drakx-//")
mv $f %buildroot/%_docdir/installer-help/es/$i
done
ln -s ../images  %buildroot/%_docdir/installer-help/es/images
mv %buildroot/%_docdir/installer-help/en/* %buildroot/%_docdir/installer-help/
rm -f %buildroot/%_docdir/installer-help/images
mv publications/en/DrakX-Help.html/images %buildroot/%_docdir/installer-help/
rm -rf %buildroot/%_docdir/installer-help/en
ln -s . %buildroot/%_docdir/installer-help/en
sed -i -e 's!drakxid-!!g; s!drakx-!!g' %buildroot/%_docdir/installer-help/*.html %buildroot/%_docdir/installer-help/*/*.html


# build HTML index file
cat > $DESTDIR/mandriva/en/Mastering-Manual/index.html <<EOF
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
    <a href="Mastering-Manual.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Mastering-Manual.pdf">
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
cat > $DESTDIR/mandriva/en/Introducing/index.html <<EOF
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
    <a href="Introducing.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Introducing.pdf">
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
cat > $DESTDIR/mandriva/fr/Mastering-Manual/index.html <<EOF
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
    <a href="Mastering-Manual.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Mastering-Manual.pdf">
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
cat > $DESTDIR/mandriva/fr/Introducing/index.html <<EOF
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
    <a href="Introducing.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Introducing.pdf">
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
cat > $DESTDIR/mandriva/pt_br/Introducing/index.html <<EOF
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
    <a href="Introducing.html/index.html">
      <img src="../../images/manuel-face.png" align="center" border="0">
       HTML</a>
    </tr>
<!--
    <tr>
      <a href="Introducing.pdf">
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


%post Mastering-Manual-en
%{update_menus}
%postun Mastering-Manual-en
%{clean_menus}

%post Drakxtools-Guide-en
%{update_menus}
%postun Drakxtools-Guide-en
%{clean_menus}

%post Introducing-en
%{update_menus}
%postun Introducing-en
%{clean_menus}

%post Mastering-Manual-fr
%{update_menus}
%postun Mastering-Manual-fr
%{clean_menus}

%post Drakxtools-Guide-fr
%{update_menus}
%postun Drakxtools-Guide-fr
%{clean_menus}

%post Introducing-fr
%{update_menus}
%postun Introducing-fr
%{clean_menus}

%post Drakxtools-Guide-pt_br
%{update_menus}
%postun Drakxtools-Guide-pt_br
%{clean_menus}

%post Introducing-pt_br
%{update_menus}
%postun Introducing-pt_br
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

%files Mastering-Manual-en
%defattr(-,root,root)
%{_datadir}/applications/%name-Mastering-Manual-en.desktop
%dir %_docdir/mandriva/en/Mastering-Manual
%doc %_docdir/mandriva/en/Mastering-Manual/*

%files Drakxtools-Guide-en
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-en.desktop
%dir %_docdir/mandriva/en/Drakxtools-Guide
%doc %_docdir/mandriva/en/Drakxtools-Guide/*

%files Introducing-en
%defattr(-,root,root)
%{_datadir}/applications/%name-Introducing-en.desktop
%dir %_docdir/mandriva/en/Introducing
%doc %_docdir/mandriva/en/Introducing/*

%files Mastering-Manual-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Mastering-Manual-fr.desktop
%dir %_docdir/mandriva/fr/Mastering-Manual
%doc %_docdir/mandriva/fr/Mastering-Manual/*

%files Drakxtools-Guide-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-fr.desktop
%dir %_docdir/mandriva/fr/Drakxtools-Guide
%doc %_docdir/mandriva/fr/Drakxtools-Guide/*

%files Introducing-fr
%defattr(-,root,root)
%{_datadir}/applications/%name-Introducing-fr.desktop
%dir %_docdir/mandriva/fr/Introducing
%doc %_docdir/mandriva/fr/Introducing/*

%files Drakxtools-Guide-pt_br
%defattr(-,root,root)
%{_datadir}/applications/%name-Drakxtools-Guide-pt_br.desktop
%dir %_docdir/mandriva/pt_br/Drakxtools-Guide
%doc %_docdir/mandriva/pt_br/Drakxtools-Guide/*

%files Introducing-pt_br
%defattr(-,root,root)
%{_datadir}/applications/%name-Introducing-pt_br.desktop
%dir %_docdir/mandriva/pt_br/Introducing
%doc %_docdir/mandriva/pt_br/Introducing/*



%changelog

