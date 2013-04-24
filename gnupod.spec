Name:		gnupod		
Summary:	Command-line tools for the iPod
Version:	0.99.8
Release:	%mkrel 2
Source:		ftp://ftp.gnu.org/gnu/gnupod/%{name}-%{version}.tgz
URL:		http://www.gnu.org/software/gnupod/
License:	GPLv3+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	perl-MP3-Info perl-Unicode-String
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww-perl
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-TimeDate
Requires:	perl-MP3-Info perl-Unicode-String
Requires:	perl-XML-Parser
BuildArch:	noarch
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


%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc CHANGES doc/*
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/*
%{_infodir}/*


%changelog
* Fri Apr 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.99.8-2mdv2011.0
+ Revision: 538315
- just don't define name, version, and release on top of spec
- don't bumping release, not needed

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.99.8-2mdv2010.1
+ Revision: 515565
- Fix url
- provides: gnupod-tools
- Fix 3 of 4 rpmlint's warning
- remove spaces for tabulations, line 5
- update to 0.99.8

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.99.7-2mdv2010.0
+ Revision: 437796
- rebuild

* Tue Jan 20 2009 Funda Wang <fwang@mandriva.org> 0.99.7-1mdv2009.1
+ Revision: 331669
- add BR

  + Jérôme Soyer <saispo@mandriva.org>
    - New upstream release

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.99.6-3mdv2009.0
+ Revision: 246499
- rebuild

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 0.99.6-1mdv2008.1
+ Revision: 161625
- New version 0.99.6

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.99.5-1mdv2008.1
+ Revision: 96129
- Add BR
- New release 0.99.5
- New release 0.99.5

* Sun Sep 02 2007 Funda Wang <fwang@mandriva.org> 0.99.3-1mdv2008.0
+ Revision: 77743
- New version 0.99.3

* Mon May 21 2007 Jérôme Soyer <saispo@mandriva.org> 0.99.2-1mdv2008.0
+ Revision: 29224
- Add BuildRequires
- New release 0.99.2
- Import gnupod



* Tue May 23 2006 Lenny Cartier <lenny@mandriva.com> 0.99-1mdk
- 0.99

* Sun Jun 26 2005 Austin Acton <austin@mandriva.org> 0.98.1-1mdk
- 0.98.1
- source URL

* Sun Feb 27 2005 Austin Acton <austin@mandrake.org> 0.98-1mdk
- 0.98

* Wed Sep 1 2004 Austin Acton <austin@mandrake.org> 0.96-1mdk
- 0.96

* Wed Jun 30 2004 Austin Acton <austin@linux.ca> 0.95-1mdk
- 0.95
- configure 2.5

* Sun Dec 14 2003 Austin Acton <austin@linux.ca> 0.93-1mdk
- 0.93

* Mon Oct 6 2003 Austin Acton <aacton@yorku.ca> 0.92-1mdk
- 0.92
- no need parser-simple, file-ncopy
- drop patch

* Thu Jul 24 2003 Michael Scherer <scherer.michael@free.fr> 0.29-0.3mdk 
- Fix unpackaged files

* Thu Jul 17 2003 David Walser <luigiwalser@yahoo.com> 0.29-0.2mdk
- use Getopt::Long instead of Getopt::Mixed

* Wed Jul 16 2003 David Walser <luigiwalser@yahoo.com> 0.29-0.1mdk
- 0.29 RC1
- drop patch (better way of fixing installation)
- update URL

* Sun Mar 16 2003 Austin Acton <aacton@yorku.ca> 0.28-1mdk
- 0.28

* Sun Feb 9 2003 Austin Acton <aacton@yorku.ca> 0.27-1mdk
- initial package
