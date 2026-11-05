Name:           moonwitness-ide
Version:        0.4.6.{{{ git_dir_version }}}
Release:        1
Summary:        The Engineering Observatory for evidence-driven software development
License:        Apache-2.0
URL:            https://github.com/BRIDGE-ALLAH/MOONWITNESS-IDE

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}

BuildRequires:  cargo libxkbcommon-x11-devel libxcb-devel vulkan-loader-devel wayland-devel openssl-devel pkgconf libxkbcommon-x11-devel

%description
MOONWITNESS IDE is an evolving, Lapce-based engineering workspace. Its current native editor foundation uses Rust, Floem, rope-based editing, and wgpu rendering.

%prep
{{{ git_dir_setup_macro }}}
cargo fetch --locked

%build
cargo build --profile release-lto --package lapce-app --frozen

%install
install -Dm755 target/release-lto/lapce %{buildroot}%{_bindir}/lapce
install -Dm644 extra/linux/dev.lapce.lapce.desktop %{buildroot}/usr/share/applications/dev.lapce.lapce.desktop
install -Dm644 extra/linux/dev.lapce.lapce.metainfo.xml %{buildroot}/usr/share/metainfo/dev.lapce.lapce.metainfo.xml
install -Dm644 extra/images/logo.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/moonwitness-ide.svg

%files
%license LICENSE*
%doc *.md
%{_bindir}/lapce
/usr/share/applications/dev.lapce.lapce.desktop
/usr/share/metainfo/dev.lapce.lapce.metainfo.xml
/usr/share/icons/hicolor/scalable/apps/moonwitness-ide.svg

%changelog
* Mon Jan 01 2024 Jakub Panek
- See full changelog on GitHub
