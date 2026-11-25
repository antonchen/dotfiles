# Dotfiles

Personal Linux dotfiles managed with [chezmoi](https://www.chezmoi.io/), covering the shell, editor, terminal, desktop environment, and applications.

[简体中文](README_zh.md)

## Configurations

- **Shell:** Zsh configuration, aliases, plugins, command completion, history, key bindings, and prompt; user profile and X session startup files.
- **Editor:** Vim configuration, One Dark color scheme, and syntax and indentation files.
- **Terminal:** Kitty configuration, custom tab bar, and X resources.
- **Desktop (X11):** bspwm, sxhkd, Polybar, Rofi, Dunst, and Picom settings, plus session autostart entries.
- **Applications:** Git, GTK, fontconfig, CopyQ, Fcitx 5, Go, container image registries, browser and VS Code startup flags, and smart-go-dl.
- **Private configuration:** GPG, SSH, and selected application configurations are stored as encrypted files.

## Usage

Initialize chezmoi with this repository and apply the configuration:

```sh
chezmoi init https://github.com/antonchen/dotfiles.git
chezmoi apply
```

Review pending changes before applying updates:

```sh
chezmoi diff
chezmoi apply
```

Some settings are tailored to this machine and desktop environment. Install the required applications before applying or using the configurations.

## License

This project is licensed under the [MIT License](LICENSE).
