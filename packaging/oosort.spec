Name:           oosort
Version:        0.1.0
Release:        1%{?dist}
Summary:        Memory-bounded external merge sort with radix optimization and numeric comparator.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosort
Source0:        oosort-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosort is a sovereign, capability-bounded STREAM SORTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosort
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosort-uninstall

%files
/usr/bin/oosort
/usr/bin/oosort-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
