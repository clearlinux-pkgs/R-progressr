#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-progressr
Version  : 0.13.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/progressr_0.13.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/progressr_0.13.0.tar.gz
Summary  : An Inclusive, Unifying API for Progress Updates
Group    : Development/Tools
License  : GPL-3.0
Requires: R-digest
BuildRequires : R-digest
BuildRequires : R-future
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n progressr
cd %{_builddir}/progressr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673371049

%install
export SOURCE_DATE_EPOCH=1673371049
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
/usr/lib64/R/library/progressr/DESCRIPTION
/usr/lib64/R/library/progressr/INDEX
/usr/lib64/R/library/progressr/Meta/Rd.rds
/usr/lib64/R/library/progressr/Meta/demo.rds
/usr/lib64/R/library/progressr/Meta/features.rds
/usr/lib64/R/library/progressr/Meta/hsearch.rds
/usr/lib64/R/library/progressr/Meta/links.rds
/usr/lib64/R/library/progressr/Meta/nsInfo.rds
/usr/lib64/R/library/progressr/Meta/package.rds
/usr/lib64/R/library/progressr/Meta/vignette.rds
/usr/lib64/R/library/progressr/NAMESPACE
/usr/lib64/R/library/progressr/NEWS.md
/usr/lib64/R/library/progressr/R/progressr
/usr/lib64/R/library/progressr/R/progressr.rdb
/usr/lib64/R/library/progressr/R/progressr.rdx
/usr/lib64/R/library/progressr/WORDLIST
/usr/lib64/R/library/progressr/demo/mandelbrot.R
/usr/lib64/R/library/progressr/doc/index.html
/usr/lib64/R/library/progressr/doc/progressr-intro.html
/usr/lib64/R/library/progressr/doc/progressr-intro.md
/usr/lib64/R/library/progressr/help/AnIndex
/usr/lib64/R/library/progressr/help/aliases.rds
/usr/lib64/R/library/progressr/help/figures/handler_cli-default.svg
/usr/lib64/R/library/progressr/help/figures/handler_cli-format-1.svg
/usr/lib64/R/library/progressr/help/figures/handler_pbcol-adjust-mid.svg
/usr/lib64/R/library/progressr/help/figures/handler_pbcol-adjust-right-complete.svg
/usr/lib64/R/library/progressr/help/figures/handler_pbcol-default.svg
/usr/lib64/R/library/progressr/help/figures/handler_pbmcapply-default.svg
/usr/lib64/R/library/progressr/help/figures/handler_progress-complete.svg
/usr/lib64/R/library/progressr/help/figures/handler_progress-default.svg
/usr/lib64/R/library/progressr/help/figures/handler_progress-format-1.svg
/usr/lib64/R/library/progressr/help/figures/handler_progress-format-2.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-1.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-char-ansi.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-char-width-2.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-char.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-default.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-style-1.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-style-2.svg
/usr/lib64/R/library/progressr/help/figures/handler_txtprogressbar-style-3.svg
/usr/lib64/R/library/progressr/help/figures/lifecycle-maturing-blue.svg
/usr/lib64/R/library/progressr/help/paths.rds
/usr/lib64/R/library/progressr/help/progressr.rdb
/usr/lib64/R/library/progressr/help/progressr.rdx
/usr/lib64/R/library/progressr/html/00Index.html
/usr/lib64/R/library/progressr/html/R.css
/usr/lib64/R/library/progressr/tests/debug.R
/usr/lib64/R/library/progressr/tests/demo.R
/usr/lib64/R/library/progressr/tests/exceptions.R
/usr/lib64/R/library/progressr/tests/globals,relay.R
/usr/lib64/R/library/progressr/tests/handler_cli.R
/usr/lib64/R/library/progressr/tests/handler_make_progression.R
/usr/lib64/R/library/progressr/tests/handler_pbmcapply.R
/usr/lib64/R/library/progressr/tests/handler_progress.R
/usr/lib64/R/library/progressr/tests/handler_rstudio.R
/usr/lib64/R/library/progressr/tests/handler_shiny.R
/usr/lib64/R/library/progressr/tests/handler_tkprogressbar.R
/usr/lib64/R/library/progressr/tests/handler_txtprogressbar.R
/usr/lib64/R/library/progressr/tests/handlers.R
/usr/lib64/R/library/progressr/tests/incl/end.R
/usr/lib64/R/library/progressr/tests/incl/start,load-only.R
/usr/lib64/R/library/progressr/tests/incl/start.R
/usr/lib64/R/library/progressr/tests/progress_aggregator.R
/usr/lib64/R/library/progressr/tests/progression.R
/usr/lib64/R/library/progressr/tests/progressor.R
/usr/lib64/R/library/progressr/tests/utils.R
/usr/lib64/R/library/progressr/tests/with_progress,delay.R
/usr/lib64/R/library/progressr/tests/with_progress,relay.R
/usr/lib64/R/library/progressr/tests/with_progress.R
/usr/lib64/R/library/progressr/tests/without_progress.R
/usr/lib64/R/library/progressr/tests/zzz,doFuture.R
/usr/lib64/R/library/progressr/tests/zzz,foreach_do.R
/usr/lib64/R/library/progressr/tests/zzz,furrr.R
/usr/lib64/R/library/progressr/tests/zzz,future.apply.R
/usr/lib64/R/library/progressr/tests/zzz,plyr.R
/usr/lib64/R/library/progressr/tests/zzz,purrr.R
/usr/lib64/R/library/progressr/tests/zzz,shiny.R
