%define name	gnupod
%define version	0.99.7
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Command-line tools for the iPod
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.gnu.org/download/gnupod/%{name}-%{version}.tgz
URL:		http://www.gnu.org/software/gnupod/
License:	GPLv3
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:  perl-MP3-Info perl-Unicode-String
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-libwww-perl
BuildRequires:  perl-Digest-SHA1
BuildRequires:	perl-TimeDate
Requires:  	perl-MP3-Info perl-Unicode-String
Requires:  	perl-XML-Parser
BuildArch:	noarch
Obsoletes:	gnupod-tools
Provides:	gnupod-tools

%description
gnuPod is a collection of tools which allow you to use your iPod under Linux.
HFS+ and FAT32 formatted iPods are supported.

%prep
%setup -q

%build
%{__perl} -pi -e 's/test \$PERL/test "\$PERL"/' configure
export PERL="%{__perl} -I$RPM_BUILD_ROOT%{perl_vendorlib}"
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{perl_vendorlib}
mkdir -p $RPM_BUILD_ROOT/%{_infodir}
%makeinstall
cp doc/%name.info $RPM_BUILD_ROOT/%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc CHANGES doc/*
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/*
%{_infodir}/*
