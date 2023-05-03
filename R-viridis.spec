#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-viridis
Version  : 0.6.3
Release  : 51
URL      : https://cran.r-project.org/src/contrib/viridis_0.6.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/viridis_0.6.3.tar.gz
Summary  : Colorblind-Friendly Color Maps for R
Group    : Development/Tools
License  : MIT
Requires: R-ggplot2
Requires: R-gridExtra
Requires: R-viridisLite
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-viridisLite
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
common forms of color blindness and/or color vision deficiency. The color 
    maps are also perceptually-uniform, both in regular form and also when 
    converted to black-and-white for printing. This package also contains 
    'ggplot2' bindings for discrete and continuous color and fill scales. A lean
    version of the package called 'viridisLite' that does not include the 
    'ggplot2' bindings can be found at

%prep
%setup -q -n viridis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683149290

%install
export SOURCE_DATE_EPOCH=1683149290
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/viridis/CITATION
/usr/lib64/R/library/viridis/DESCRIPTION
/usr/lib64/R/library/viridis/INDEX
/usr/lib64/R/library/viridis/LICENSE
/usr/lib64/R/library/viridis/Meta/Rd.rds
/usr/lib64/R/library/viridis/Meta/data.rds
/usr/lib64/R/library/viridis/Meta/features.rds
/usr/lib64/R/library/viridis/Meta/hsearch.rds
/usr/lib64/R/library/viridis/Meta/links.rds
/usr/lib64/R/library/viridis/Meta/nsInfo.rds
/usr/lib64/R/library/viridis/Meta/package.rds
/usr/lib64/R/library/viridis/Meta/vignette.rds
/usr/lib64/R/library/viridis/NAMESPACE
/usr/lib64/R/library/viridis/NEWS.md
/usr/lib64/R/library/viridis/R/viridis
/usr/lib64/R/library/viridis/R/viridis.rdb
/usr/lib64/R/library/viridis/R/viridis.rdx
/usr/lib64/R/library/viridis/data/Rdata.rdb
/usr/lib64/R/library/viridis/data/Rdata.rds
/usr/lib64/R/library/viridis/data/Rdata.rdx
/usr/lib64/R/library/viridis/doc/index.html
/usr/lib64/R/library/viridis/doc/intro-to-viridis.R
/usr/lib64/R/library/viridis/doc/intro-to-viridis.Rmd
/usr/lib64/R/library/viridis/doc/intro-to-viridis.html
/usr/lib64/R/library/viridis/help/AnIndex
/usr/lib64/R/library/viridis/help/aliases.rds
/usr/lib64/R/library/viridis/help/figures/logo.png
/usr/lib64/R/library/viridis/help/figures/maps.png
/usr/lib64/R/library/viridis/help/figures/viridis-scales.png
/usr/lib64/R/library/viridis/help/paths.rds
/usr/lib64/R/library/viridis/help/viridis.rdb
/usr/lib64/R/library/viridis/help/viridis.rdx
/usr/lib64/R/library/viridis/html/00Index.html
/usr/lib64/R/library/viridis/html/R.css
/usr/lib64/R/library/viridis/tests/figs/colorandfill/a.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/b.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/c.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/d.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/e.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/f.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/g.svg
/usr/lib64/R/library/viridis/tests/figs/colorandfill/h.svg
/usr/lib64/R/library/viridis/tests/figs/deps.txt
/usr/lib64/R/library/viridis/tests/testthat.R
/usr/lib64/R/library/viridis/tests/testthat/test-viridis.R
