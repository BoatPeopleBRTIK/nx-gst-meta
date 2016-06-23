Name:    nx-gst-meta
Version: 0.0.1
Release: 0
License: Apache 2.0
Summary: Nexell GStreamer Meta Data
Group: Development/Libraries
Source:  %{name}-%{version}.tar.gz

BuildRequires:	pkgconfig automake autoconf libtool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gstreamer1-devel
BuildRequires:	glibc-devel

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Nexell GStreamer Meta Data

%package devel
Summary: Nexell GStreamer Meta Data development
Group: Development/Libraries
License: Apache 2.0
Requires: %{name} = %{version}-%{release}

%description devel
Nexell scaler (devel)

%prep
%setup -q

%build
autoreconf -v --install || exit 1
%configure
make %{?_smp_mflags}

%postun -p /sbin/ldconfig

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -name "*.la" -delete

%files
%{_libdir}/libnxgstmeta.so*

%files devel
%{_includedir}/*