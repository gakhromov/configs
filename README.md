# configs
Config files for some apps that I use. Instructions are made for Arch Linux.

For more info, refer to [Arch Wiki](https://wiki.archlinux.org/).

## Xorg config
### Requirements
*	`xorg` package group (`pacman -S xorg`)
*	`libinput` package (`pacman -S xf86-input-libinput`)
### Files
*	`/usr/share/X11/xorg.conf.d/*`

## System daemon config (`systemd` as the super-daemon)
### Requirements
*	System daemons installed and enabled/started:
	-	`iwd` (for network control via `iwctl`)
	-	`acpi` (battery control)
	-	`pulseaudio` (for audio)
	> To work properly, `pulseaudio` service and socket has to be enabled/started by user with `--user` flag
	-	`pulseaudio-alsa` (also for audio)
	-	`tlp` (daemon that saves battery (useful for notebooks))
	-	`ufw` (Uncomplicated firewall)
	> Default config would be `ufw default deny` + `ufw enable`
### Files
*	`/etc/systemd/logind.conf`

## Desktop and App configs
### Requirements
*	Xorg installed and configured
*	System daemons installed and configured
*	Command line system control apps:
	-	`brightnessctl` (Brightness control)
	-	`htop` (process control)
	-	`pamixer` (`pulseaudio` audio control)
	-	`alsa-lib`, `alsa-utils` (other audio control)
*	Fonts:
	-	`adobe-source-sans-pro-fonts` (default font)
	-	`ttf-ubuntu-font-family` (`qtile` bar font)
	-	`noto-fonts-emoji` (emoji)
	-	`texlive-fontsextra` (math fonts)
	-	`powerline-fonts` (powerline fonts)
	-	`ttf-font-awesome` (fixes powerlines in `qtile` bar and also provides icons)
	-	`ttf-inconsolata` (`alacritty` font)
	-	`ttf-roboto` (Roboto font, used in `awesome`)
*	Utils:
	-	`sudo` (you all know what this is for)
	-	`vim` (text editor)
	-	`alacritty` (terminal emulator)
	-	`nitrogen` (wallpapers)
	-	`git` (Version control system. Required to install AUR packages)
	-	`base-devel` (Required to install packages from AUR)
	-	`yay` (great AUR helper. Installes from AUR)
	-	`zsh` (bash alternative)
	-	[oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) (for zsh customization, `oh-my-zsh-git` in AUR)
	-	`lxappearance` (for changing gtk themes)
	> Unpack the theme in `~/.themes/` using `tar -xvf ...`, then apply the theme in LXAppearance
	-	`picom` (window composer. Used for window animations + transparency)

*	Window manager (you can choose `qtile` or `awesome`)
  	For `qtile`:
	-	`powerline` (powerline plugin for `vim`, `qtile` and other stuff)
	-	`powerline-vim` (powerline plugin for `vim`)
	-	`python` (for `qtile` to work)
	-	`python-iwlib`, `python-psutil` (for some `qtile` widgets to work)
	-	`qtile` (Dynamic tyling window manager written in `python`)
	-	`dmenu` (app launcher)
	
	For `awesome` (Config forked from @ChrisTitusTech [repo](https://github.com/ChrisTitusTech/material-awesome)):
	-	`awesome` (Dynamic tyling window manager written in `lua`, more powerful than `qtile`)
	-	`rofi` (app launcher)
	-	`i3lock-fancy` (fancy lockscreen)
	-	`polkit-gnome` (for graphical auth)
	-	`materia-gtk-theme` (GTK theme)
	-	`network-manager-applet` (network icon)
	-	[Papirus Dark](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme) icon theme (install via `wget -qO- https://git.io/papirus-icon-theme-install | sh`)
	-	`qt5-styleplugins` (AUR package)
	> After installing the package above, add the following to the `/etc/environment`
	
### Recommendations
*	Other apps:
	-	`chromium` (browser. Also can be used as an image viewer)
	-	`flameshot` (tool for screenshots)
	-	`pacman-contrib` (`pactree` and other useful stuff)
	-	`nautilus` (file manager)
	-	`nautilus-share` and `gvfs-smb` (for nautilus smb support)
	-	`vlc` (music + video player)
	-	`lxrandr-gtk3` (program to manage monitor setups using `xrandr`)
	-	`windscribe-cli` (VPN, AUR package)
	-	`pamac-aur` (Pamac, graphical package installer, AUR package)


### Files
*	`~/.xinitrc` (use this file to switch between qtile and awesome)
*	`~/.themes/*`
*	`~/.zshrc`
*	`~/.oh-my-zsh/custom/themes/*`
*	`~/.config/alacritty/*`
*	`~/.config/picom/*`
For qtile:
*	`~/.config/qtile/*`
For awesome:
*	`~/.config/awesome/*`

