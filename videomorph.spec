Name:       videomorph
Version:    1.4.1
Release:    6%{?dist}
Summary:    Small GUI wrapper for FFMPEG based on PyQt5
License:    ASL 2.0
URL:        https://github.com/videomorph-dev/videomorph
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python3-rpm-macros
BuildRequires:  ffmpeg

Requires:       ffmpeg
Requires:       python3-setuptools
Requires:       python3-qt5

%description
VideoMorph is a video converter based on ffmpeg, and written with Python 3,
and PyQt5. With VideoMorph you can convert your favorite videos to the
currently more popular video formats, like MPG, MP4, AVI, WEBM, DVD, VCD,
FLV, MOV, OGV, and also extract the audio to a file with MP3 format.


%prep
%autosetup
pathfix.py -pni "%{__python3}" setup.py bin/videomorph tests/*


%build
%{py3_build}

%install
%{py3_install}

rm -rf %{buildroot}%{_datadir}/doc/
rm -f share/doc/videomorph/manual/*.pdfE

desktop-file-validate %{buildroot}%{_datadir}/applications/videomorph.desktop

%files
%doc README.md share/doc/videomorph/manual changelog.gz
%license LICENSE
%{_bindir}/videomorph
%{_datadir}/applications/videomorph.desktop
%{_datadir}/icons/videomorph.png
%{_datadir}/videomorph/
%{_mandir}/man1/videomorph.*
%{python3_sitelib}/videomorph-*-py%{python3_version}.egg-info
%{python3_sitelib}/videomorph/


%changelog
* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-6
- Rebuild for python-3.10

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Leigh Scott <leigh123linux@gmail.com> - 1.4.1-3
- Rebuild for python-3.9

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.4.1-1
- Initial build

