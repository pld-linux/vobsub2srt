%define commit 0ba6e25
%define subver	pre7
%define rel	2
Summary:	VobSub2SRT .sub/.idx to .srt subtitle converter
Summary(pl.UTF-8):	VobSub2SRT - konwerter podpisów .sub/.idx do .srt
Name:		vobsub2srt
Version:	1.0
Release:	%{rel}.%{subver}+g%{commit}
License:	GPL v3+
Group:		Applications/Multimedia
Source0:	https://github.com/ruediger/VobSub2SRT/archive/%{commit}/%{name}-%{version}%{subver}+g%{commit}.tar.gz
# Source0-md5:	e291abe6f4fca5dd8df4db98e97c69bb
Patch0:		https://github.com/ruediger/VobSub2SRT/pull/72.patch
# Patch0-md5:	fd20b401b96fc646c74c399b57a07b65
Patch1:		%{name}-includes.patch
URL:		https://github.com/ruediger/VobSub2SRT
BuildRequires:	cmake >= 2.6.4
BuildRequires:	libtiff-devel
BuildRequires:	tesseract-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VobSub2SRT is a simple command line program to convert .idx / .sub
subtitles into .srt text subtitles by using OCR. It is based on code
from the MPlayer project.

%description -l pl.UTF-8
VobSub2SRT to prosty, działający z linii poleceń program do konwersji
podpisów .idx/.sub do podpisów tekstowych .srt przy użyciu OCR. Jest
oparty na kodzie z projektu MPlayer.

%prep
%setup -qc
%{__mv} VobSub2SRT-%{commit}*/* .
%patch -P0 -p1
%patch -P1 -p1

%build
install -d build
cd build
%cmake \
	-DBASH_COMPLETION_PATH=%{bash_compdir} \
	-DINSTALL_DOC_DIR=%{_docdir}/%{name}-%{version} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/copyright .
%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README copyright
%attr(755,root,root) %{_bindir}/vobsub2srt
%{_mandir}/man1/vobsub2srt.1*
%{bash_compdir}/vobsub2srt
