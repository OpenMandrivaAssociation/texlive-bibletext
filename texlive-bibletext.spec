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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows to insert Bible texts in a document by specifying
references.

