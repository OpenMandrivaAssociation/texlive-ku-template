%global tl_name ku-template
%global tl_revision 45935

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.02
Release:	%{tl_revision}.1
Summary:	Copenhagen University or faculty logo for front page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ku-template
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ku-template.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ku-template.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A comprehensive package for adding University of Copenhagen or faculty
logo to your front page. For use by student or staff at University of
Copenhagen (Kobenhavns Universitet).

