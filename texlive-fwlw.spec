# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/fwlw
# catalog-date 2012-06-04 11:02:08 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-fwlw
Version:	20180303
Release:	2
Summary:	Get first and last words of a page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fwlw
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fwlw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fwlw.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extracts the first and last words of a page,
together with the first word of the next page, just before the
page is formed into the object to print. The package defines a
couple of page styles that use the words that have been
extracted.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fwlw/fwlw.sty
%doc %{_texmfdistdir}/doc/latex/fwlw/README
%doc %{_texmfdistdir}/doc/latex/fwlw/fwlw.pdf
%doc %{_texmfdistdir}/doc/latex/fwlw/fwlw.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
