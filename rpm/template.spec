Name:           ros-indigo-tf2-tools
Version:        0.5.13
Release:        0%{?dist}
Summary:        ROS tf2_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/tf2_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-msgs
Requires:       ros-indigo-tf2-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-msgs
BuildRequires:  ros-indigo-tf2-ros

%description
tf2_tools

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Mar 04 2016 Tully Foote <tfoote@osrfoundation.org> - 0.5.13-0
- Autogenerated by Bloom

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

* Tue Dec 23 2014 Tully Foote <tfoote@osrfoundation.org> - 0.5.7-0
- Autogenerated by Bloom

* Thu Sep 18 2014 Tully Foote <tfoote@osrfoundation.org> - 0.5.6-0
- Autogenerated by Bloom

