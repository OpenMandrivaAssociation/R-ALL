%global packname  ALL
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4.11
Release:          1
Summary:          A data package
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              None
Source0:          http://bioconductor.org/packages/data/experiment/src/contrib/ALL_1.4.11.tar.gz
Requires:         R-Biobase 
Requires:         R-rpart 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase
BuildRequires:    R-rpart 

%description
Data of T- and B-cell Acute Lymphocytic Leukemia from the Ritz Laboratory
at the DFCI (includes Apr 2004 versions)

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
