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
