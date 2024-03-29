#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-logback-core
Version  : 1.2.1
Release  : 4
URL      : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.jar
Source0  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.jar
Source1  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.1.2/logback-core-1.1.2.jar
Source2  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.1.2/logback-core-1.1.2.pom
Source3  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.1.3/logback-core-1.1.3.jar
Source4  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.1.3/logback-core-1.1.3.pom
Source5  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.pom
Source6  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.jar
Source7  : https://repo1.maven.org/maven2/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.pom
Source8  : https://repo1.maven.org/maven2/ch/qos/logback/logback-parent/1.1.2/logback-parent-1.1.2.pom
Source9  : https://repo1.maven.org/maven2/ch/qos/logback/logback-parent/1.1.3/logback-parent-1.1.3.pom
Source10  : https://repo1.maven.org/maven2/ch/qos/logback/logback-parent/1.2.1/logback-parent-1.2.1.pom
Source11  : https://repo1.maven.org/maven2/ch/qos/logback/logback-parent/1.2.3/logback-parent-1.2.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1-only
Requires: mvn-logback-core-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-logback-core package.
Group: Data

%description data
data components for the mvn-logback-core package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.2/logback-core-1.1.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.2/logback-core-1.1.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.3
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.3/logback-core-1.1.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.3/logback-core-1.1.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.3
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.1.2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.1.2/logback-parent-1.1.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.1.3
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.1.3/logback-parent-1.1.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.2.1
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.2.1/logback-parent-1.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.2.3
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.2.3/logback-parent-1.2.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.2/logback-core-1.1.2.jar
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.2/logback-core-1.1.2.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.3/logback-core-1.1.3.jar
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.1.3/logback-core-1.1.3.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.jar
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.1/logback-core-1.2.1.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.jar
/usr/share/java/.m2/repository/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.1.2/logback-parent-1.1.2.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.1.3/logback-parent-1.1.3.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.2.1/logback-parent-1.2.1.pom
/usr/share/java/.m2/repository/ch/qos/logback/logback-parent/1.2.3/logback-parent-1.2.3.pom
