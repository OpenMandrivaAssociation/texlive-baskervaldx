%global tl_name baskervaldx
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.08
Release:	%{tl_revision}.1
Summary:	Extension and modification of BaskervaldADF with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/baskervaldx
License:	gpl2+ lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervaldx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervaldx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extends and modifies the BaskervaldADF font (a Baskerville substitute)
with more accented glyphs, with small caps and oldstyle figures in all
shapes. Includes OpenType and PostScript fonts, as well as LaTeX support
files.

