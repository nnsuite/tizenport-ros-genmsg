Name:           ros-kinetic-genmsg
Version:        0.5.8
Release:        0
Summary:        ROS genmsg package
Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/genmsg
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  gcc-c++
BuildRequires:  ros-kinetic-catkin >= 0.5.74

%description
Standalone Python library for generating ROS message and service data structures
for various languages.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__ros_setup}
%{__ros_build}

%install
%{__ros_setup}
%{__ros_install}

%files -f build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)
%{__ros_install_path}/lib/python2.7/site-packages/*

%changelog
