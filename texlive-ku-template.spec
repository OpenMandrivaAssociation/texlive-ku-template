Name:		texlive-ku-template
Version:	45935
Release:	1
Summary:	Copenhagen University or faculty logo for front page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ku-template
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ku-template.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ku-template.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A comprehensive package for adding University of Copenhagen or
faculty logo to your front page. For use by student or staff at
University of Copenhagen (Kobenhavns Universitet).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ku-template
%doc %{_texmfdistdir}/doc/latex/ku-template

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
