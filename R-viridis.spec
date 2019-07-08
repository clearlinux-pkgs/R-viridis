#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-viridis
Version  : 0.5.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/viridis_0.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/viridis_0.5.1.tar.gz
Summary  : Default Color Maps from 'matplotlib'
Group    : Development/Tools
License  : MIT
Requires: R-ggplot2
Requires: R-gridExtra
Requires: R-rasterVis
Requires: R-viridisLite
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-rasterVis
BuildRequires : R-viridisLite
BuildRequires : buildreq-R

%description
'inferno', and 'cividis' color maps for 'R'. 'viridis', 'magma', 'plasma',

%prep
%setup -q -c -n viridis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562620904

%install
export SOURCE_DATE_EPOCH=1562620904
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library viridis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library viridis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library viridis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc viridis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/viridis/DESCRIPTION
/usr/lib64/R/library/viridis/INDEX
/usr/lib64/R/library/viridis/LICENSE
/usr/lib64/R/library/viridis/Meta/Rd.rds
/usr/lib64/R/library/viridis/Meta/features.rds
/usr/lib64/R/library/viridis/Meta/hsearch.rds
/usr/lib64/R/library/viridis/Meta/links.rds
/usr/lib64/R/library/viridis/Meta/nsInfo.rds
/usr/lib64/R/library/viridis/Meta/package.rds
/usr/lib64/R/library/viridis/Meta/vignette.rds
/usr/lib64/R/library/viridis/NAMESPACE
/usr/lib64/R/library/viridis/R/viridis
/usr/lib64/R/library/viridis/R/viridis.rdb
/usr/lib64/R/library/viridis/R/viridis.rdx
/usr/lib64/R/library/viridis/doc/index.html
/usr/lib64/R/library/viridis/doc/intro-to-viridis.R
/usr/lib64/R/library/viridis/doc/intro-to-viridis.Rmd
/usr/lib64/R/library/viridis/doc/intro-to-viridis.html
/usr/lib64/R/library/viridis/help/AnIndex
/usr/lib64/R/library/viridis/help/aliases.rds
/usr/lib64/R/library/viridis/help/figures/sample-palette.png
/usr/lib64/R/library/viridis/help/figures/samplepalette.pdf
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
/usr/lib64/R/library/viridis/tests/figs/deps.txt
/usr/lib64/R/library/viridis/tests/testthat.R
/usr/lib64/R/library/viridis/tests/testthat/Rplots.pdf
/usr/lib64/R/library/viridis/tests/testthat/test-viridis.R
