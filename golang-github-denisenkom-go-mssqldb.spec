# https://github.com/denisenkom/go-mssqldb

%global goipath github.com/denisenkom/go-mssqldb
%global commit  242fa5aa1b45aeb9fcdfeee88822982e3f548e22

%global common_description %{expand:
A pure Go MSSQL driver for the database/sql package.}

%gometa -i

# gometa strips the leading "go-" off the name
%global goname golang-github-denisenkom-go-mssqldb

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Microsoft SQL server driver for Go
License:        BSD
URL:            %{gourl}
Source:         %{gosource}

# https://github.com/denisenkom/go-mssqldb/pull/403
Patch0:         go-mssqldb-badStreamPanicf-args.patch

%description
%{common_description}


%package devel
Summary:       %{summary}

BuildRequires: golang(golang.org/x/crypto/md4)
BuildRequires: golang(cloud.google.com/go/civil)

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
# Sadly, tests expect a running MSSQL instance.
%gochecks -d .


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md examples


%changelog
* Wed Jul 25 2018 Ed Marshall <esm@logic.net> - 0-0.4.20180725git242fa5a
- Switch to forge-specific packaging.
- Update to latest upstream commit.
- Fix build failure with Go 1.11 beta.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20180314git94099f0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 16 2018 Ed Marshall <esm@logic.net> - 0-0.2.20180314git94099f0
- Bump release. Whoops!

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.1.20180314git94099f0
- Switch to upstream version with patch applied.

* Wed Mar 14 2018 Ed Marshall <esm@logic.net> - 0-0.1.20180314gitb2a6258
- Update to latest git commit, for Go 1.10 test fixes

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170919gitc7ee415
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Ed Marshall <esm@logic.net> - 0-0.1.20170919gitc7ee415
- First package for Fedora
