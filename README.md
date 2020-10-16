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
	-	`pulseaudio` (for audio)
	> To work properly, `pulseaudio` service and socket has to be enabled/started by user with `--user` flag
	-	`pulseaudio-alsa` (also for audio)
	-	`tlp` (daemon that saves battery (useful for notebooks))
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
*	Fonts:
	-	`adobe-source-sans-pro-fonts` (default font)
	-	`powerline-fonts` (powerline fonts)
	-	`ttf-font-awesome` (fixes powerlines in `qtile` bar and also provides icons)
	-	`ttf-inconsolata` (`alacritty` font)
	-	`ttf-ubuntu-font-family` (`qtile` bar font)
	-	`noto-fonts-emoji` (emoji)
	-	`texlive-fontsextra` (math fonts)
*	Window manager + utils:
	-	`vim` (text editor)
	-	`powerline` (powerline plugin for `vim`, `qtile` and other stuff)
	-	`powerline-vim` (powerline plugin for `vim`)
	-	`python` (for `qtile` to work)
	-	`python-iwlib`, `python-psutil` (for some `qtile` widgets to work)
	-	`alacritty` (terminal emulator)
	-	`qtile` (Dynamic tyling window manager)
	-	`dmenu` (app launcher)
	-	`nitrogen` (wallpapers)
	-	`zsh` (bash alternative)
	-	[oh-my-zsh](https://github.com/ohmyzsh/ohmyzsh) (for zsh customization)
	-	`lxappearance` (for changing gtk themes)
	> Unpack the theme in `~/.themes/` using `tar -xvf ...`, then apply the theme in LXAppearance
	-	`picom` (window composer. Used for window animations + transparency)
	
### Recommendations
*	Other apps:
	-	`sudo` (you all know what this is for)
	-	`chromium` (browser. Also can be used as an image viewer)
	-	`flameshot` (tool for screenshots)
	-	`pacman-contrib` (`pactree` and other useful stuff)
	-	`nautilus` (file manager)
	-	`vlc` (music + video player)


### Files
*	`~/.themes/*`
*	`~/.zshrc`
*	`~/.oh-my-zsh/custom/themes/*`
*	`~/.config/alacritty/*`
*	`~/.config/qtile/*`
*	`~/.config/picom/*`

