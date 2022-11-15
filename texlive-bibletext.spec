Name:		texlive-bibletext
Version:	45196
Release:	1
Summary:	Insert Bible passages by their reference
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibletext
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibletext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibletext.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows to insert Bible texts in a document by
specifying references.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bibletext
%doc %{_texmfdistdir}/doc/latex/bibletext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
