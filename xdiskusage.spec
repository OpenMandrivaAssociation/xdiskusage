%define name	xdiskusage
%define version	1.48
%define release	%mkrel 1

Summary: 	Graphical display of disk usage
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		File tools
Source0: 	http://xdiskusage.sourceforge.net/%{name}-%{version}.tgz
URL: 		http://xdiskusage.sourceforge.net
BuildRequires: 	fltk-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	xdu
Provides:	xdu

%description
xdiskusage is a user-friendly program to show you what is using up all
your disk space. It is based on the design of xdu written by Phillip
C. Dykstra. Changes have been made so it runs "du" for you, and can 
display the free space left on the disk, and produce a PostScript 
version of the display.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall
ln -s %{name} %{buildroot}%{_bindir}/xdu

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/xdu
%{_mandir}/man1/%{name}.1*
