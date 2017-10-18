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
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX="$CMAKE_PREFIX_PATH" \
        -DCMAKE_PREFIX_PATH="$CMAKE_PREFIX_PATH" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/usr/setup.sh" ]; then . "/usr/setup.sh"; fi
pushd build
make install DESTDIR=%{buildroot}

%define local_install_dir  $(pwd)
make install DESTDIR=%{local_install_dir}/installed
find installed -type f  | sed 's/installed//' >  install_manifest.txt
popd

%files -f build/install_manifest.txt
%manifest %{name}.manifest
%defattr(-,root,root)

%changelog
