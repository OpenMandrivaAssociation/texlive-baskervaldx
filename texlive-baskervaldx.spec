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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extends and modifies the BaskervaldADF font (a Baskerville substitute)
with more accented glyphs, with small caps and oldstyle figures in all
shapes. Includes OpenType and PostScript fonts, as well as LaTeX support
files.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/opentype
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/opentype/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/afm/public/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/map/dvips/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/opentype/public/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/type1/public/baskervaldx
%dir %{_datadir}/texmf-dist/fonts/vf/public/baskervaldx
%doc %{_datadir}/texmf-dist/doc/fonts/baskervaldx/COPYING
%doc %{_datadir}/texmf-dist/doc/fonts/baskervaldx/NOTICE.txt
%doc %{_datadir}/texmf-dist/doc/fonts/baskervaldx/README
%doc %{_datadir}/texmf-dist/doc/fonts/baskervaldx/baskervaldx-doc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/baskervaldx/baskervaldx-doc.tex
%doc %{_datadir}/texmf-dist/doc/fonts/baskervaldx/baskervaldxmatheg-crop.pdf
%{_datadir}/texmf-dist/fonts/afm/public/baskervaldx/Baskervaldx-Bol.afm
%{_datadir}/texmf-dist/fonts/afm/public/baskervaldx/Baskervaldx-BolIta.afm
%{_datadir}/texmf-dist/fonts/afm/public/baskervaldx/Baskervaldx-Ita.afm
%{_datadir}/texmf-dist/fonts/afm/public/baskervaldx/Baskervaldx-Reg-old.afm
%{_datadir}/texmf-dist/fonts/afm/public/baskervaldx/Baskervaldx-Reg.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/bvalph.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/bvtabosf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_23jm4j.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_2445cl.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_2kku7k.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_2n2qka.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_2xv27p.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_2zeho7.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_34qyyt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_4f5bev.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_524fcc.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_556rta.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_5p6atn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_5zt4ml.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_6dnovg.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_6lr3v3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_6rdtju.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_6xreh4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_7d54ky.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_7i75ol.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_7nnme4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ahc6ab.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ak7beg.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_aorlch.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_auq4k5.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_awcfcx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ax2yo2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ax7osu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_c3asvt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ck4t6h.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_cl2iyt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_clcsgf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_coqtyh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_cv7nez.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_d7elqy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_d7lahw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_dbb2hd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_dw7i6y.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_edkp5z.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ezfzzx.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_feassy.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_g4f2qe.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_g5xsbp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_gar3zb.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_gjwmpg.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_h4nqsn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ik76ei.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ilkd46.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_itooof.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_jwmruw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_k3ascw.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_k6hbcl.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_kq7kv3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_l44ess.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_lewyuf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_lozoyg.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_lxdjmd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_m4qttc.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_m5lkgj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_mu6kzn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_mvsyl4.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_mys6kl.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_nt5h45.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_nwv7yn.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ofzzxu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_pqcihf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_puztjr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_riybhr.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_rosua2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_scthrl.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_sv3nex.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_teykvl.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_tfcpq3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_tnmdy3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_tv7w6k.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_uguye6.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_untte3.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_upot5e.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_uy4eps.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_v577lu.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_wg6wcc.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_wvrs5w.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_xbckbj.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_xebzk2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_xjuza2.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_xotpaa.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_y62qbt.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_y77okd.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_yk4dqp.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_ymibyh.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_zag37q.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_zb3hlf.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_zey2cz.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/baskervaldx/zbv_zkqdv4.enc
%{_datadir}/texmf-dist/fonts/map/dvips/baskervaldx/Baskervaldx.map
%{_datadir}/texmf-dist/fonts/opentype/public/baskervaldx/Baskervaldx-Bol.otf
%{_datadir}/texmf-dist/fonts/opentype/public/baskervaldx/Baskervaldx-BolIta.otf
%{_datadir}/texmf-dist/fonts/opentype/public/baskervaldx/Baskervaldx-Ita.otf
%{_datadir}/texmf-dist/fonts/opentype/public/baskervaldx/Baskervaldx-Reg.otf
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-alph.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-alph.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ot1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ot1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-ly1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-ly1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-t1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ts1--base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/Baskervaldx-osf.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/zbvbmi.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/baskervaldx/zbvmi.tfm
%{_datadir}/texmf-dist/fonts/type1/public/baskervaldx/Baskervaldx-Bol.pfb
%{_datadir}/texmf-dist/fonts/type1/public/baskervaldx/Baskervaldx-BolIta.pfb
%{_datadir}/texmf-dist/fonts/type1/public/baskervaldx/Baskervaldx-Ita.pfb
%{_datadir}/texmf-dist/fonts/type1/public/baskervaldx/Baskervaldx-Reg.pfb
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-sup-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-sup-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ot1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-sc-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-swash-ly1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-swash-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/zbvbmi.vf
%{_datadir}/texmf-dist/fonts/vf/public/baskervaldx/zbvmi.vf
%{_datadir}/texmf-dist/tex/latex/baskervaldx/Baskervaldx.sty
%{_datadir}/texmf-dist/tex/latex/baskervaldx/LY1Baskervaldx-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/LY1Baskervaldx-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/LY1Baskervaldx-Sup.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/LY1Baskervaldx-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/LY1Baskervaldx-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/OT1Baskervaldx-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/OT1Baskervaldx-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/OT1Baskervaldx-Sup.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/OT1Baskervaldx-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/OT1Baskervaldx-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/T1Baskervaldx-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/T1Baskervaldx-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/T1Baskervaldx-Sup.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/T1Baskervaldx-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/T1Baskervaldx-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/TS1Baskervaldx-LF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/TS1Baskervaldx-OsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/TS1Baskervaldx-TLF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/TS1Baskervaldx-TOsF.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/baskervaldx.fontspec
%{_datadir}/texmf-dist/tex/latex/baskervaldx/ly1minbaskervaldx.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/ot1minbaskervaldx.fd
%{_datadir}/texmf-dist/tex/latex/baskervaldx/t1minbaskervaldx.fd
