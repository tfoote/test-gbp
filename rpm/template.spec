Name:           ros-jade-tf2-geometry-msgs
Version:        0.5.12
Release:        0%{?dist}
Summary:        ROS tf2_geometry_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-orocos-kdl
Requires:       ros-jade-tf2
Requires:       ros-jade-tf2-ros
BuildRequires:  ros-jade-catkin >= 0.5.68
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-orocos-kdl
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-tf2
BuildRequires:  ros-jade-tf2-ros

%description
tf2_geometry_msgs

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Aug 05 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.12-0
- Autogenerated by Bloom

* Wed Apr 22 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.11-0
- Autogenerated by Bloom

* Tue Apr 21 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.10-0
- Autogenerated by Bloom

* Wed Mar 25 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.9-0
- Autogenerated by Bloom

* Tue Mar 17 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.8-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Tully Foote <tfoote@osrfoundation.org> - 0.5.7-0
- Autogenerated by Bloom

