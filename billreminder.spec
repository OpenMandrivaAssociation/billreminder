Summary:	Simple application to remind you to pay your bills
Name:		billreminder
Version:	0.4.0
Release:	%mkrel 3
Source0:	http://download.gnome.org/sources/billreminder/0.3/%{name}-%{version}.tar.bz2
License:	GPLv3
Group:		Graphical desktop/GNOME
URL:		http://billreminder.gnulinuxbrasil.org/
BuildArch:	noarch
BuildRequires:	GConf2
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	python-devel
BuildRequires:	pygtk2
BuildRequires:	python-sqlite2
BuildRequires:	python-dbus
BuildRequires:	desktop-file-utils
Requires:	pygtk2
Requires:	python-sqlite2
Requires:	python-dbus
Requires:	python-imaging
Requires:	python-sqlalchemy

%description
BillReminder is a small and quick accounting application designed to
allow for easy tracking of bills.

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install \
  --add-category="GTK" \
  --add-category="Finance" \
  --remove-category="Application" \
  --remove-category="Miscellaneous" \
  --remove-key="Encoding" \
  --remove-key="Version" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_sysconfdir}/xdg/autostart/%{name}d.desktop
%{py_puresitedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/%{name}.service
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}.png


%changelog
* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 0.4.0-3mdv2011.0
+ Revision: 677107
- rebuild to add gconf2 as req

* Sat Apr 02 2011 Jani Välimaa <wally@mandriva.org> 0.4.0-2
+ Revision: 649945
- require python-sqlalchemy

* Sat Apr 02 2011 Jani Välimaa <wally@mandriva.org> 0.4.0-1
+ Revision: 649861
- new version 0.4.0
- fix license
- drop support for old mdv releases
- drop buildroot definition

* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.3.2-4mdv2011.0
+ Revision: 592379
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2-3mdv2010.0
+ Revision: 436820
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.3.2-2mdv2009.1
+ Revision: 323364
- rebuild

* Sat Oct 11 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.2-1mdv2009.1
+ Revision: 292583
- drop the usr/local workaround: apparently no longer needed
- adjust for the fact it uses gconf schema now
- new release 0.3.2

* Fri Sep 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.1-2mdv2009.0
+ Revision: 288429
- fix bad path set in a config file which was breaking start (#43775)

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 275593
- New version 0.3.1

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.3.0-1mdv2009.0
+ Revision: 218430
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 03 2008 Adam Williamson <awilliamson@mandriva.org> 0.3.0-1mdv2008.1
+ Revision: 177856
- fix up menu entry (categories)
- import billreminder


