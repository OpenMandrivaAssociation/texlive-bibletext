%global tl_name bibletext
%global tl_revision 45196

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.2
Release:	%{tl_revision}.1
Summary:	Insert Bible passages by their reference
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibletext
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibletext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibletext.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows to insert Bible texts in a document by specifying
references.

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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibletext
%dir %{_datadir}/texmf-dist/tex/latex/bibletext
%doc %{_datadir}/texmf-dist/doc/latex/bibletext/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/bibletext/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bibletext/bibletext.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibletext/bibletext.tex
%{_datadir}/texmf-dist/tex/latex/bibletext/bibletext.sty
