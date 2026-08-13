%global tl_name baskervaldx
%global tl_revision 78931
%global tl_version 1.08

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Extension and modification of BaskervaldADF with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/baskervaldx
License:	gpl2+ lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervaldx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervaldx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Extends and modifies the BaskervaldADF font (a Baskerville substitute)
with more accented glyphs, with small caps and oldstyle figures in all
shapes. Includes OpenType and PostScript fonts, as well as LaTeX support
files.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from baskervaldx:
Map Baskervaldx.map
TL_DROPIN_EOF
