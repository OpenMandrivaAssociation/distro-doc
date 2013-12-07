%define distrib_name Mandriva Linux
%define group Books/Computer books
%define libdrakx %{_prefix}/lib/libDrakX
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name:		mandriva-doc
Summary:	%distrib_name documentation
Version:	2010.1
Release:	1.4

License:	Open Publication License
Group:		%group
Url:		http://wiki.mandriva.com/en/Development/Tasks/Documentation

Source0:	%name.tar.bz2
Source1:	%name-%version.tar.bz2

BuildArch:	noarch
BuildRequires:	wget
BuildRequires:	locales-en
BuildRequires:	locales-fr
BuildRequires:	locales-pt
BuildRequires:	locales-it
BuildRequires:	locales-de
BuildRequires:	locales-es


%define LANGS en fr pt_br it de es

%description
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the menus.


%package Mastering-Manual-en
Summary:		The %distrib_name manuals in English
Group:			%group
Requires:		locales-en
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-drakxtools-en
Provides:		mandriva-doc-Discovery-en = %{version}-%{release}
Obsoletes:		mandriva-doc-Discovery-en < %{version}-%{release}                                                                                                                                    
Provides:		mandriva-doc-Discovery-en = %{version}-%{release}
Obsoletes:		mandrake-doc-Mastering-Manual-en < %{version}-%{release}
Provides:		mandrake-doc-Mastering-Manual-en = %{version}-%{release}

%description Mastering-Manual-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-en
Summary:		The %distrib_name manuals in English
Group:			%group
Requires:		locales-en
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-drakxtools-en < %{version}-%{release}
Provides:		mandrake_doc-drakxtools-en = %{version}-%{release}
Obsoletes:		mandrake-doc-drakxtools-en < %{version}-%{release}
Provides:		mandrake-doc-drakxtools-en = %{version}-%{release}
Obsoletes:		mandrake-doc-Drakxtools-Guide-en < %{version}-%{release}
Provides:		mandrake-doc-Drakxtools-Guide-en = %{version}-%{release}

%description Drakxtools-Guide-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Introducing-en
Summary:		The %distrib_name manuals in English
Group:			%group
Requires:		locales-en
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-en < %{version}-%{release}
Provides:		mandrake_doc-en = %{version}-%{release}
Obsoletes:		mandrake-doc-en < %{version}-%{release}
Provides:		mandrake-doc-en = %{version}-%{release}
Obsoletes:		mandrake-doc-Introducing-en < %{version}-%{release}
Provides:		mandrake-doc-Introducing-en = %{version}-%{release}

%description Introducing-en
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Mastering-Manual-fr
Summary:		The %distrib_name manuals in French
Group:			%group
Requires:		locales-fr
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-drakxtools-fr < %{version}-%{release}
Provides:		mandriva-doc-Discovery-fr = %{version}-%{release}
Obsoletes:		mandriva-doc-Discovery-fr < %{version}-%{release}                                                                                                                                                 
Provides:		mandriva-doc-Discovery-fr = %{version}-%{release}
Obsoletes:		mandrake-doc-Mastering-Manual-fr < %{version}-%{release}
Provides:		mandrake-doc-Mastering-Manual-fr = %{version}-%{release}

%description Mastering-Manual-fr
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-fr
Summary:		The %distrib_name manuals in French
Group:			%group
Requires:		locales-fr
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-drakxtools-fr < %{version}-%{release}
Provides:		mandrake_doc-drakxtools-fr = %{version}-%{release}
Obsoletes:		mandrake-doc-drakxtools-fr < %{version}-%{release}
Provides:		mandrake-doc-drakxtools-fr = %{version}-%{release}
Obsoletes:		mandrake-doc-Drakxtools-Guide-fr < %{version}-%{release}
Provides:		mandrake-doc-Drakxtools-Guide-fr = %{version}-%{release}

%description Drakxtools-Guide-fr
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Introducing-fr
Summary:		The %distrib_name manuals in French
Group:			%group
Requires:		locales-fr
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-fr < %{version}-%{release}
Provides:		mandrake_doc-fr = %{version}-%{release}
Obsoletes:		mandrake-doc-fr < %{version}-%{release}
Provides:		mandrake-doc-fr = %{version}-%{release}
Obsoletes:		mandrake-doc-Introducing-fr < %{version}-%{release}
Provides:		mandrake-doc-Introducing-fr = %{version}-%{release}

%description Introducing-fr
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Drakxtools-Guide-pt_br
Summary:		The %distrib_name manuals in Brazilian Portuguese
Group:			%group
Requires:		locales-pt
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-drakxtools-pt_br < %{version}-%{release}
Provides:		mandrake_doc-drakxtools-pt_br = %{version}-%{release}
Obsoletes:		mandrake-doc-drakxtools-pt_br < %{version}-%{release}
Provides:		mandrake-doc-drakxtools-pt_br = %{version}-%{release}
Obsoletes:		mandrake-doc-Drakxtools-Guide-pt_br < %{version}-%{release}
Provides:		mandrake-doc-Drakxtools-Guide-pt_br = %{version}-%{release}

%description Drakxtools-Guide-pt_br
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package Introducing-pt_br
Summary:		The %distrib_name manuals in Brazilian Portuguese
Group:			%group
Requires:		locales-pt
Requires:		mandriva-doc-common >= %{version}-%{release}
Obsoletes:		mandrake_doc-pt_br <%{version}-%{release}
Provides:		mandrake_doc-pt_br = %{version}-%{release}
Obsoletes:		mandrake-doc-pt_br < %{version}-%{release}
Provides:		mandrake-doc-pt_br = %{version}-%{release}
Obsoletes:		mandrake-doc-Introducing-pt_br < %{version}-%{release}
Provides:		mandrake-doc-Introducing-pt_br = %{version}-%{release}

%description Introducing-pt_br
This package contains some useful documentation for %distrib_name systems.
This documentation is directly accessible through the main menu.

%package common
Summary:	Common data for all %distrib_name specific documentation
Group:		%group
Conflicts:	mandrake_doc < 9.2
Obsoletes:	mandrake_doc-common < %{version}-%{release}
Provides:	mandrake_doc-common = %{version}-%{release}
Obsoletes:	mandrake-doc-common < %{version}-%{release}
Provides:	mandrake-doc-common = %{version}-%{release}

%description common

This package contains common icons and images for all %distrib_name
specific documentation, plus the index file matching Help IDs to HTML
help pages.

%package installer-help
Summary:	DrakX Installer help in all available languages for %distrib_name
Group:		%group

%description installer-help
This package contains the HTML files used as inline help during the
installation procedure of %distrib_name.


%prep
%setup -q -c %name-%version -a 1


%install
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
* Tue May 25 2010 Anne Nicolas <anne.nicolas@mandriva.com> 2010.1-1.0mdv2010.1
+ Revision: 545945
- first update for 2010 Spring
- remove tarball for 2010.0 version

* Sun Nov 08 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-4.0mdv2010.1
+ Revision: 463223
- Fix dates and images for 2010

* Fri Oct 30 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-3.0mdv2010.0
+ Revision: 460235
- fix images

* Thu Oct 29 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-2.0mdv2010.0
+ Revision: 460186
- update doc

* Thu Oct 29 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2010.0-1.0mdv2010.0
+ Revision: 460094
- Official documentation for 2010.0

* Tue Apr 21 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2009.1-2.0mdv2009.1
+ Revision: 368590
- update doc

* Fri Apr 17 2009 Anne Nicolas <anne.nicolas@mandriva.com> 2009.1-1mdv2009.1
+ Revision: 367870
- add second tarball
- add 2009.1 tarball
- remove old tarballs
- fix release

  + Camille Bégnis <camille@mandriva.com>
    - instructions for packager
    - Major update for French manuals

* Fri Oct 03 2008 Camille Bégnis <camille@mandriva.com> 2009.0-1.0mdv2009.0
+ Revision: 291047
- Last minute fixes, hopefully final for release.

* Fri Oct 03 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.9mdv2009.0
+ Revision: 291017
- Last minute fixes, more to come...

* Fri Oct 03 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.8mdv2009.0
+ Revision: 290976
- All manuals in English final.

* Thu Oct 02 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.7mdv2009.0
+ Revision: 290803
- More fixes in DrakX help

* Thu Oct 02 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.6mdv2009.0
+ Revision: 290749
- Activate profiling for DrakX help

* Thu Oct 02 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.5mdv2009.0
+ Revision: 290733
- DrakX help final, rest almost

* Mon Sep 29 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-0.4mdv2009.0
+ Revision: 289919
- fix drakhelp breakage in another place too :-(
- remove old tarballs

* Mon Sep 29 2008 Thierry Vignaud <tv@mandriva.org> 2009.0-0.3mdv2009.0
+ Revision: 289898
- fix drakhelp breakage

* Mon Sep 29 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.2mdv2009.0
+ Revision: 289884
- update, still in progress.
- add mcc-localdisks

* Wed Sep 17 2008 Camille Bégnis <camille@mandriva.com> 2009.0-0.1mdv2009.0
+ Revision: 285473
- First draft for 2009.0 doc
- First draft for 2009.0 doc
- removed drakcronat
- first 2009.0 draft doc
- new doc available in 2009.0

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Apr 02 2008 Camille Bégnis <camille@mandriva.com> 2008.1-0.4mdv2008.1
+ Revision: 191781
- minor fixes in all langs

* Wed Apr 02 2008 Camille Bégnis <camille@mandriva.com> 2008.1-0.3mdv2008.1
+ Revision: 191621
- All content final in main languages, though some minor mistakes may remain
- add back packaging filaes

* Fri Mar 21 2008 Camille Bégnis <camille@mandriva.com> 2008.1-0.1mdv2008.1
+ Revision: 189395
- include html in SRPM
- adapt to 2008.1, now gets the HTML docs directly from auto publications server
- Old scripts to be adapted for 2008.1
- Fix release Number
- Uptade pt_br, fixes in other langs.

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 05 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.13mdv2008.0
+ Revision: 95623
- Update doc and fix #34508

* Wed Oct 03 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.12mdv2008.0
+ Revision: 95217
- update doc

* Tue Oct 02 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.10mdv2008.0
+ Revision: 94596
- update doc

* Mon Oct 01 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.9mdv2008.0
+ Revision: 94102
- update doc

* Sat Sep 29 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.8mdv2008.0
+ Revision: 93868
- EN finished

* Wed Sep 26 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.6mdv2008.0
+ Revision: 93122
- General update, plus clean up installer help to remove navigation header and footer, plus images

* Mon Sep 24 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.5mdv2008.0
+ Revision: 92665
- update doc (in progress)

* Fri Sep 21 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.4mdv2008.0
+ Revision: 91745
- update doc (in progress)
- update doc (in progress)

* Wed Sep 19 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.3mdv2008.0
+ Revision: 90799
- doc in progress now include (obsolete?\195) Starter manual

* Wed Sep 19 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.2mdv2008.0
+ Revision: 90481
- update doc (in progress)
- update doc (in progress)
- update doc (in progress)

* Sat Sep 08 2007 Camille Bégnis <camille@mandriva.com> 2008.0-0.1mdv2008.0
+ Revision: 82292
- Preliminary packaging for 2008.0 doc

* Thu Aug 30 2007 Thierry Vignaud <tv@mandriva.org> 2007.1-1.1mdv2008.0
+ Revision: 75539
- kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character


* Tue Mar 27 2007 Camille Bégnis <camille@mandriva.com> 2007.1-1.1mdv2007.1
+ Revision: 148837
- update pt_br installer doc

* Fri Mar 23 2007 Camille Bégnis <camille@mandriva.com> 2007.1-1.0mdv2007.1
+ Revision: 148419
- fix some rpmdrake screenshots (thanks Tv)

* Thu Mar 22 2007 Camille Bégnis <camille@mandriva.com> 2007.1-0.6mdv2007.1
+ Revision: 148082
- Last fixes and updates for 2007 Spring

* Wed Mar 21 2007 Camille Bégnis <camille@mandriva.com> 2007.1-0.5mdv2007.1
+ Revision: 147457
- update all docs

* Fri Mar 16 2007 Camille Bégnis <camille@mandriva.com> 2007.1-0.4mdv2007.1
+ Revision: 145195
- Add PT-BR
  fix FR

* Fri Mar 16 2007 Camille Bégnis <camille@mandriva.com> 2007.1-0.3mdv2007.1
+ Revision: 144731
- fix images

* Thu Mar 15 2007 Camille Bégnis <camille@mandriva.com> 2007.1-0.2mdv2007.1
+ Revision: 143963
- Add new installer-help package
  Update all manuels (still beta)

* Wed Mar 07 2007 Camille Bégnis <camille@mandriva.com> 2007.1-0.1mdv2007.1
+ Revision: 134190
- Import mandriva-doc

* Tue Sep 05 2006 Camille Begnis <camille@mandriva.com> 2007-0.4mdv2007.0
- Fix XDG menu (%%longtitle) (Thx Nicolas Lecureuil <neoclust@mandriva.org>)

* Wed Aug 30 2006 Camille Begnis <camille@mandriva.com> 2007-0.3mdv2007.0
- Update content, use correct DTD in sources

* Tue Aug 29 2006 Camille Begnis <camille@mandriva.com> 2007-0.2mdv2007.0
- Buildrequires DocBook DTD 4.4 and not 4.3

* Tue Aug 29 2006 Camille Begnis <camille@mandriva.com> 2007-0.1mdv2007.0
- First Alpha release for 2007 doc
- New Xdg menus system

* Sat Sep 17 2005 Camille Begnis <camille@mandriva.com> 2006-6mdk
- Update Portuguese

* Fri Sep 16 2005 Camille Begnis <camille@mandriva.com> 2006-5mdk
- Update Portuguese

* Thu Sep 15 2005 Camille Begnis <camille@mandriva.com> 2006-4mdk
- Add reference manual in Portuguese

* Wed Sep 14 2005 Camille Begnis <camille@mandriva.com> 2006-3mdk
- Add missing Server Guides

* Tue Sep 13 2005 Camille Begnis <camille@mandriva.com> 2006-2mdk
- slight fix in ES
- fix menu entry for Server Guide

* Tue Sep 13 2005 Camille Begnis <camille@mandriva.com> 2006-1mdk
- Final release for Mandriva 2006
- Removed manuals not ready

* Sun Sep 11 2005 Camille Begnis <camille@mandriva.com> 2006-0.6mdk
- Work in progress

* Thu Sep 08 2005 Camille Begnis <camille@mandriva.com> 2006-0.5mdk
- Work in progress

* Tue Aug 30 2005 Camille Begnis <camille@mandriva.com> 2006-0.4mdk
- Work in progress

* Thu Aug 18 2005 Camille Begnis <camille@mandriva.com> 2006-0.3mdk
- Work in progress

* Wed Aug 17 2005 Camille Begnis <camille@mandriva.com> 2006-0.2mdk
- Work in progress

* Tue Aug 09 2005 Camille Begnis <camille@mandriva.com> 2006-0.1mdk
- First Mandriva 2006 alpha doc
- Added Brazilian Portuguese
- Added Discovery manual in EN, FR
- Mandriva name changes
- Open Publication License

