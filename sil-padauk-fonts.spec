%global fontname sil-padauk
%global fontconf 65-%{fontname}.conf
%global archivename ttf-sil-padauk-2.6.1

Name:    %{fontname}-fonts
Version: 2.6.1
Release: 1%{?dist}
Summary: A font for Burmese and the Myanmar script

Group:   User Interface/X
License: OFL
URL:     http://scripts.sil.org/Padauk
# The source link is a redirect and is not directly accessible
Source0: %{archivename}.tar.gz
Source1: %{name}-fontconfig.conf

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem

Obsoletes:     padauk-fonts < 2.4-6

%description
Padauk is a Myanmar font covering all currently used characters
in the Myanmar block. The font aims to cover all minority language needs.
At the moment, these do not extend to stylistic variation needs.
The font is a smart font using a Graphite description.


%prep
%setup -q -c
for txt in doc/*.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done


%build
# Nothing there


%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -fr %{buildroot}

%_font_pkg -f %{fontconf} *.ttf

%doc doc/*.txt



%changelog
* Tue Feb 16 2010 Parag <pnemade AT redhat.com> - 2.6.1-1
- Resolves:rh#565779:- please correct the source checksum issue

* Mon May 26 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-6
- Changed the URL

* Mon May 25 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-5
- Cleaned up the spec file
- Used Obsoletes for upgrade path from padauk-fonts

* Tue Mar 24 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-4
- Cleaned up the spec file as per new font packaging guidelines
- Replaced padauk-src.ttf and padaukbold-src.ttf with Padauk.ttf and Padauk-Bold.ttf [490583]
- Renamed the package to sil-padauk-fonts

* Sun Feb 22 2009 Minto Joseph <mvaliyav at redhat.com> - 2.4-3
- Changed the package as per new font packaging guidelines 


* Fri Jul 15 2008 Minto Joseph <mvaliyav at redhat.com> - 2.4-2
- Changed setup macro and fontconfig rules
- Changed fontconfig prefix


* Fri Jul 15 2008 Minto Joseph <mvaliyav at redhat.com> - 2.4-1
- Changed versioning
- Added configuration file
- Added more description
- Added license file

* Fri Jul 11 2008 Minto Joseph <mvaliyav at redhat.com> - 20080617-1
- initial package

