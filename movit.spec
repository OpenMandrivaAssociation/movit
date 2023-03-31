%define major 8
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%global optflags %{optflags} -O3

Summary:	High-performance, high-quality video filters for the GPU
Name:		movit
Version:	1.6.3
Release:	3
License:	GPLv2+
Group:		Video
Url:		http://movit.sesse.net/
Source0:	http://movit.sesse.net/%{name}-%{version}.tar.gz
Patch0:		movit-1.3.2-disable-tests.patch
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(x11)

%description
Movit is the Modern Video Toolkit, notwithstanding that anything that's
called "modern" usually isn't, and it's really not a toolkit.

Movit aims to be a high-quality, high-performance, open-source library
for video filters.

%files
%doc NEWS README
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*.comp
%{_datadir}/%{name}/*.frag
%{_datadir}/%{name}/*.vert

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Requires:	%{name}

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/libmovit.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%dir %{_includedir}/movit/
%{_includedir}/movit/*.h
%{_libdir}/libmovit.so
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
./autogen.sh
CXXFLAGS="%{optflags} -std=gnu++1z" %configure
%make_build

%install
%make_install
