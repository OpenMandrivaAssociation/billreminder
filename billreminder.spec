Summary:	Simple application to remind you to pay your bills
Name:		billreminder
Version:	0.3.0
Release:	%{mkrel 1}
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
License:	BSD
Group:		Graphical desktop/GNOME
URL:		http://billreminder.gnulinuxbrasil.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	python-devel
BuildRequires:	pygtk2
BuildRequires:	python-sqlite2
BuildRequires:	python-dbus
Requires:	pygtk2
Requires:	python-sqlite2
Requires:	python-dbus
Requires:	python-imaging

%description
BillReminder is a small and quick accounting application designed to
allow for easy tracking of bills.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%post
%{update_icon_cache hicolor}
%{update_menus}
%postun
%{clean_icon_cache hicolor}
%{clean_menus}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_sysconfdir}/xdg/autostart/%{name}d.desktop
%{py_puresitedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/%{name}.service
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_mandir}/man1/*.1*
%{_datadir}/pixmaps/%{name}.png

