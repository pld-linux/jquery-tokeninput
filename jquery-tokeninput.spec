%define		plugin	tokeninput
Summary:	jQuery Tokenizing Autocomplete Text Entry
Name:		jquery-%{plugin}
Version:	1.4.2
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/loopj/jquery-tokeninput/tarball/jquery-tokeninput-%{version}#/%{plugin}-%{version}.tgz
# Source0-md5:	30e7582fb7d929c31e6ad9036b899288
URL:		http://loopj.com/jquery-tokeninput/
BuildRequires:	js
BuildRequires:	rpmbuild(macros) > 1.268
BuildRequires:	yuicompressor
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Tokeninput is a jQuery plugin which allows your users to select
multiple items from a predefined list, using autocompletion as they
type to find each item.

You may have seen a similar type of text entry when filling in the
recipients field sending messages on facebook.

%package demo
Summary:	Demo for jQuery.tokeninput
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.tokeninput.

%prep
%setup -qc
mv *-%{name}-*/* .

%build
install -d build/styles
# compress .js
yuicompressor --charset UTF-8 src/jquery.%{plugin}.js -o build/jquery.%{plugin}.js
js -C -f build/jquery.%{plugin}.js

for css in styles/*.css; do
	yuicompressor --charset UTF-8 $css -o build/$css
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a build/* $RPM_BUILD_ROOT%{_appdir}

cp -a demo.html examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.md README.md
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
