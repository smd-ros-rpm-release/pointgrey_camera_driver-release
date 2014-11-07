Name:           ros-hydro-pointgrey-camera-driver
Version:        0.11.0
Release:        0%{?dist}
Summary:        ROS pointgrey_camera_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pointgrey_camera_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       libraw1394-devel
Requires:       libusbx-devel
Requires:       ros-hydro-camera-info-manager
Requires:       ros-hydro-diagnostic-updater
Requires:       ros-hydro-driver-base
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-image-exposure-msgs
Requires:       ros-hydro-image-proc
Requires:       ros-hydro-image-transport
Requires:       ros-hydro-nodelet
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-wfov-camera-msgs
BuildRequires:  dpkg
BuildRequires:  libraw1394-devel
BuildRequires:  libusbx-devel
BuildRequires:  ros-hydro-camera-info-manager
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-diagnostic-updater
BuildRequires:  ros-hydro-driver-base
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-image-exposure-msgs
BuildRequires:  ros-hydro-image-transport
BuildRequires:  ros-hydro-nodelet
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-roslint
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-wfov-camera-msgs

%description
Point Grey camera driver based on libflycapture2.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Fri Nov 07 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.11.0-0
- Autogenerated by Bloom

* Mon Aug 18 2014 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.10.0-0
- Autogenerated by Bloom

