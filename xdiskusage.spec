%define name	xdiskusage
%define version	1.48
%define release	%mkrel 6

Summary: 	Graphical display of disk usage
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		File tools
Source0: 	http://xdiskusage.sourceforge.net/%{name}-%{version}.tgz
# fixes x86_64 build errors: by AdamW 2007/07
Patch0:		xdiskusage-1.48-x86_64.patch
URL: 		http://xdiskusage.sourceforge.net
BuildRequires: 	fltk-devel
BuildRequires:	mesaglu-devel
BuildRequires:	libxinerama-devel
BuildRequires:	libxext-devel
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
%patch0 -p1 -b .x86_64

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall
ln -s %{name} %{buildroot}%{_bindir}/xdu

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/xdu
%{_mandir}/man1/%{name}.1*
