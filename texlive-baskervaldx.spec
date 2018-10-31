Name:		texlive-baskervaldx
Version:	1.072
Release:	2
Summary:	Extension and modification of BaskervaldADF with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/baskervaldx
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervaldx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/baskervaldx.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extends and modifies the BaskervaldADF font (a Baskerville
substitute) with more accented glyphs, with small caps and
oldstyle figures in all shapes. Includes OpenType and
PostScript fonts, as well as LaTeX support files.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/baskervaldx
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx
%{_texmfdistdir}/fonts/map/dvips/baskervaldx
%{_texmfdistdir}/fonts/opentype/public/baskervaldx
%{_texmfdistdir}/fonts/tfm/public/baskervaldx
%{_texmfdistdir}/fonts/type1/public/baskervaldx
%{_texmfdistdir}/fonts/vf/public/baskervaldx
%{_texmfdistdir}/tex/latex/baskervaldx
%doc %{_texmfdistdir}/doc/fonts/baskervaldx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
