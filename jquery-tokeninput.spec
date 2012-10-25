%define		plugin	tokeninput
Summary:	jQuery Tokenizing Autocomplete Text Entry
Name:		jquery-%{plugin}
Version:	1.6.0
Release:	2
License:	MIT / GPL
Group:		Applications/WWW
#Source0:	https://github.com/loopj/jquery-tokeninput/tarball/jquery-tokeninput-%{version}#/%{plugin}-%{version}.tgz
Source0:	https://github.com/loopj/jquery-tokeninput/tarball/master/%{plugin}-%{version}-master.tgz
# Source0-md5:	0896f48b52c6461de98002b4e0738c47
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

# unify filenames
for a in styles/*.css; do
	dir=${a%/*}
	mv $a $dir/%{plugin}${a#*/token-input}
done

%build
install -d build/styles

# compress .js
for src in src/*.js; do
	fname=${src#*/jquery.}
	out=build/$fname
	out=${out%.js}-%{version}.min.js
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $src -o $out
	js -C -f $out
%else
	cp -p $src $out
%endif
	outdir=${out%/*}
	ln -s ${out##*/} $outdir/$fname
done

# pack .css
for src in styles/*.css; do
	out=build/${src#*/jquery.}
	out=${out%.css}-%{version}.min.css
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $src -o $out
%else
	cp -p $src $out
%endif
	outdir=${out%/*}
	ln -s ${out##*/} $outdir/${src##*/}
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -p src/jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -a build/*.js  $RPM_BUILD_ROOT%{_appdir}

cp -a styles/* $RPM_BUILD_ROOT%{_appdir}
cp -a build/styles/* $RPM_BUILD_ROOT%{_appdir}

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
